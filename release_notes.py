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
import markdown
import reports
import tickets


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--milestone_id', dest='milestone_id',
                        help='The milestone id to be parsed', default='4.11.3')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    # Fetch tickets data
    t = tickets.tickets(milestone_id=args.milestone_id)
    t.load()
    tickets_stats = t.tickets

    # Generate Markdown for data
    md = markdown.markdown()
    reports.gen_overall_progress(tickets_stats['overall_progress'], md)
    reports.gen_tickets_stats_by_category(tickets_stats['by_category'], md)
    reports.gen_tickets_summary(tickets_stats['tickets'], md)
    reports.gen_individual_tickets_info(tickets_stats['tickets'], md)

    with io.open('tickets.md', 'w', encoding='utf-8') as file:
        try:
            file.write(md.content.encode('utf-8'))
        except TypeError:  # For Python 3
            file.write(md.content)
