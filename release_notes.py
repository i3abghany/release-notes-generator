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

import argparse
import io
import sys

import pickle

import markdown_generator
import reports
import tickets
from html_generator import HTMLGenerator


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
    if notes_file == '':
        return ''
    else:
        return open(notes_file, 'r').read()


if __name__ == '__main__':
    args = parse_args()
    css_file = ''
    if args.style_format == 'trac':
        css_file = 'rtems_trac.css'
    elif args.style_format == 'markdown' or args.style_format == 'md':
        css_file = 'markdown.css'
    else:
        print(f'Unsupported style format: {args.style}\n')
        sys.exit(1)

    # Fetch tickets data
    t = tickets.tickets(milestone_id=args.milestone_id)
    t.load()
    tickets_stats = t.tickets
    with open('tickets_5.1.pkl', 'wb') as pf:
        pickle.dump(tickets_stats, pf, pickle.HIGHEST_PROTOCOL)

    print('Generating the release notes PDF file')
    top_level_headings = get_notes_headings(args.notes_file)
    top_level_notes_md = get_notes_file_content(args.notes_file)
    # Generate Markdown for data
    md = markdown_generator.MarkdownGenerator()
    reports.gen_toc(top_level_headings, tickets_stats['by_category'], md)
    reports.gen_top_level_notes(top_level_notes_md, md)
    reports.gen_overall_progress(tickets_stats['overall_progress'], md)
    reports.gen_tickets_summary(tickets_stats['tickets'], md)
    reports.gen_tickets_stats_by_category(tickets_stats['by_category'], md)
    reports.gen_individual_tickets_info(tickets_stats['tickets'], md, 95 if args.style_format == 'markdown' else 75)

    with io.open('tickets.md', 'w', encoding='utf-8') as file:
        try:
            file.write(md.content.encode('utf-8'))
        except TypeError:  # For Python 3
            file.write(md.content)

    html_gen = HTMLGenerator(css_file)
    with io.open('gen/tickets.html', 'w', encoding='utf-8') as html_file:
        html_file.write(html_gen.from_markdown(md.content, args.milestone_id))
    html_output_file = 'gen/tickets.html'
    import pdfkit

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
        'disable-smart-shrinking': None,
        'enable-local-file-access': None
    }

    if args.style_format == 'trac':
        wk_options['print-media-type'] = None
    pdfkit.from_file(html_output_file, args.out_file, options=wk_options)
