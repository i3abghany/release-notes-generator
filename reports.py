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
import re

from text_justifier import TextJustifier


def gen_overall_progress(overall_progress, md):
    md.gen_heading('Overall Progress', 1)
    md.gen_line('')

    md.gen_table(overall_progress.keys(), [overall_progress.values()], align='left')
    md.gen_line_break()
    return md.content


def gen_tickets_summary(tickets, md):
    md.gen_line_break()
    md.gen_heading('Ticket Summary', 1)
    md.gen_line('')

    keys = tickets.keys()
    id_summary_mapping = [(k, tickets[k]['meta']['summary']) for k in keys]
    cols = ['id', 'summary']
    md.gen_table(cols, id_summary_mapping, align='left', max_col_width=-1)
    md.gen_line('')
    return md.content


def gen_tickets_stats_by_category(by_category, md):
    md.gen_heading('By Category', 1)
    md.gen_line('')

    for category in by_category:
        md.gen_heading(category, 2)
        md.gen_line('')

        # Get header and all rows to generate table, set category as first col
        header = [category]
        rows = []
        ticket_stats_list = list(by_category[category].values())
        if len(ticket_stats_list) > 0:
            header += ticket_stats_list[0].keys()

        for category_value in by_category[category]:
            ticket_stats = by_category[category][category_value]
            rows.append([category_value] + list(ticket_stats.values()))

        md.gen_table(header, rows, align='left')
        md.gen_line('')
    return md.content


def gen_individual_tickets_info(tickets, md):
    md.gen_line_break()
    md.gen_heading('Tickets', 1)
    md.gen_line('')

    for ticket_id in tickets:
        # Generate markdown for ticket meta data
        ticket_meta = tickets[ticket_id]['meta']

        ticket_link = tickets[ticket_id].get('comment_attachment', {}) \
            .get('link', None)
        if ticket_link is not None:
            md.gen_heading(md.gen_hyperlink(ticket_id, ticket_link), 2)
            md.gen_line('')

        md.gen_heading('Meta', 3)
        md.gen_line('')

        description = ticket_meta.get('description', None)
        summary = ticket_meta.get('summary', None)

        ticket_meta.pop('description', None)
        ticket_meta.pop('summary', None)

        md.gen_wrapped_table(header=ticket_meta.keys(), rows=[ticket_meta.values()])
        md.gen_line('')

        if description:
            md.gen_raw_text(md.gen_bold('Description'))
            md.gen_line('')
            description = description.replace('{{{', '```')
            description = description.replace('}}}', '```')
            markdown_link_format_pattern = '[{}]({})'
            description = TextJustifier('\n', markdown_link_format_pattern).wrap(description, width=70)
            description = re.sub('```\n\n', '```\n', description)
            description = re.sub('\n\n```', '\n```', description)
            md.gen_raw_text(description)
            md.gen_line('')

        if summary:
            md.gen_raw_text(md.gen_bold('Summary'))
            md.gen_line('')
            summary = summary.replace('{{{', '```')
            summary = summary.replace('}}}', '```')
            md.gen_raw_text(summary)
            md.gen_line('')

        # Generate markdown for ticket's comments or attachments
        items = tickets[ticket_id]['comment_attachment']['items']
        comments = items.get('comments', None)
        comments = remove_unnecessary_columns(comments)
        attachments = items.get('attachments', None)
        attachments = remove_unnecessary_columns(attachments)
        if len(comments) > 0:
            comments_header = comments[0].keys()
            comments_rows = []
            justifier = TextJustifier('<br />', '[{}]({})')
            for comment in comments:
                comment['description'] = justifier.wrap(comment['description'], width=60)
            for comment in comments:
                comments_rows.append(list(comment.values()))
            md.gen_heading('Comments', 3)
            md.gen_line('')
            md.gen_table(comments_header, comments_rows, max_col_width=-1)
            md.gen_line('')

        if len(attachments) > 0:
            attachments_header = attachments[0].keys()
            attachments_rows = []
            for attachment in attachments:
                attachments_rows.append(list(attachment.values()))
                attachments_rows[-1][3] = '[{}]({})'.format("link", attachments_rows[-1][3])
            md.gen_heading('attachments', 3)
            md.gen_line('')
            md.gen_table(attachments_header, attachments_rows, max_col_width=-1)
            md.gen_line('')


def remove_unnecessary_columns(addenda):
    for el in addenda:
        el.pop('link', None)
        el.pop('guid', None)
        el.pop('title', None)
        el.pop('category', None)
    return addenda


