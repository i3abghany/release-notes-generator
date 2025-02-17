#
# RTEMS Tools Project (http://www.rtems.org/)
# Copyright 2018 Danxue Huang (danxue.huang@gmail.com)
# All rights reserved.
#
# This file is part of the RTEMS Tools package in 'rtems-tools'.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#

import io
import sys

import argparse
import pickle
import m2r

import tickets
from html_generator import HTMLGenerator
from markdown_generator import MarkdownGenerator
from reports import ReportsGenerator
from rst_generator import RstGenerator


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--milestone_id', dest='milestone_id',
                        help='The milestone id to be parsed', default='4.11.3')
    parser.add_argument('-s', '--style', dest='style_format',
                        help='Generated document style (currently either: trac or markdown)', default='trac')
    parser.add_argument('-o', '--outfile', dest='out_file',
                        help='Name of the generated output PDF file', default='out.pdf')
    parser.add_argument('-n', '--notes-file', dest='notes_file',
                        help='A file with top-level, manually-written release notes', default='')
    return parser.parse_args()


def get_notes_headings(file_name):
    if file_name == '':
        return []
    lines = [line.rstrip() for line in open(file_name, 'r').readlines()]
    headings = [line for line in lines if line.startswith('#')]
    return headings


def get_notes_file_content(notes_file):
    return open(notes_file, 'r').read() if notes_file != '' else ''


def dump_gen_content(gen_content, fname):
    with io.open(fname, 'w', encoding='utf-8') as ff:
        try:
            ff.write(gen_content.encode('utf-8'))
        except TypeError:  # For Python 3
            ff.write(gen_content)


def generate_from_rst(gen_content, milestone_id):
    gen_content = RstGenerator.prepend_header(gen_content, milestone_id)
    dump_gen_content(gen_content, 'tickets.rst')
    import subprocess, shutil
    try:
        shutil.which('rst2pdf')
    except shutil.Error:
        print('rst2pdf is not found, please install it and then rerun the generator.')
        sys.exit(1)
    subprocess.run(['rst2pdf', 'tickets.rst', '-o', args.out_file, '--raw-html'], stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL)


def generate_from_html(gen_content):
    dump_gen_content(gen_content, 'tickets.rst')
    html_gen = HTMLGenerator(css_file)
    with io.open('gen/tickets.html', 'w', encoding='utf-8') as html_file:
        html_file.write(html_gen.from_markdown(gen_content, args.milestone_id))
    wk_options = {
        'page-size': 'A4',
        'margin-top': '0.40in',
        'margin-right': '0.40in',
        'margin-bottom': '0.40in',
        'margin-left': '0.40in',
        'encoding': 'UTF-8',
        '--footer-font-size': '8',
        '--footer-left': f'RTEMS {args.milestone_id} release notes',
        '--footer-right': '[page]',
        'enable-local-file-access': None,
        'enable-internal-links': None,
        'disable-smart-shrinking': None,
        'print-media-type': None
    }

    import pdfkit
    try:
        pdfkit.configuration()
    except OSError:
        print('wkhtmltopdf is not found, please install it and then rerun the generator.')
        sys.exit(1)
    html_output_file = 'gen/tickets.html'
    pdfkit.from_file(html_output_file, args.out_file, options=wk_options)


if __name__ == '__main__':
    args = parse_args()
    css_file = ''
    if args.style_format == 'trac':
        css_file = 'rtems_trac.css'
    elif args.style_format == 'markdown':
        css_file = 'markdown.css'
    elif args.style_format == 'rst':
        pass  # TODO: add custom CSS file for rst if needed
    else:
        print(f'Unsupported style format: {args.style_format}\n')
        sys.exit(1)

    # Fetch tickets data
    t = tickets.tickets(milestone_id=args.milestone_id)
    t.load()
    tickets_stats = t.tickets

    print('Generating the release notes PDF file...')
    top_level_headings = get_notes_headings(args.notes_file)
    top_level_notes_md = get_notes_file_content(args.notes_file)
    gen = ReportsGenerator(fmt=args.style_format)
    gen.gen_toc(top_level_headings, tickets_stats['by_category'])
    gen.gen_top_level_notes(top_level_notes_md)
    gen.gen_overall_progress(tickets_stats['overall_progress'])
    gen.gen_tickets_summary(tickets_stats['tickets'])
    gen.gen_tickets_stats_by_category(tickets_stats['by_category'])
    gen.gen_individual_tickets_info(tickets_stats['tickets'])

    if args.style_format == 'rst':
        generate_from_rst(gen.generator.content, args.milestone_id)
    else:
        generate_from_html(gen.generator.content)
