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
from joblib import Parallel, delayed

import markdown_generator
from text_justifier import TextJustifier


def gen_overall_progress(overall_progress, md):
    md.gen_heading('Overall Progress', 1)
    md.gen_line('')

    md.gen_table([k.capitalize() for k in overall_progress.keys()], [overall_progress.values()], align='left')
    return md.content


def gen_tickets_summary(tickets, md):
    md.gen_line_break()
    md.gen_heading('Tickets Summary', 1)
    md.gen_line('')

    keys = tickets.keys()
    id_summary_mapping = [(k, tickets[k]['meta']['summary']) for k in keys]
    cols = ['ID', 'Summary']
    md.gen_table(cols, id_summary_mapping, align='left', max_col_width=-1)
    md.gen_line_break()
    return md.content


def _convert_to_bulleted_link(name: str, generator):
    level = name.count('#')
    stripped_name = name.replace('#', '').strip()
    if isinstance(generator, markdown_generator.MarkdownGenerator):
        stripped_name = f"**<font size=3>{stripped_name}</font>**"
    linked_name = name.lower().replace(' ', '-').replace('-', '', 1).replace('#', '', level - 1).replace('.', '')
    return f"{('    ' * (level - 1)) + '* '}[{stripped_name}]({linked_name})"


def gen_toc(top_headings, categories, md):
    toc_headers = [h[1:] for h in top_headings]
    toc_headers.extend([
        '# Overall Progress',
        '# Tickets Summary',
        '# Tickets By Category'
    ])

    toc_headers.extend(["## " + c.capitalize() for c in categories])
    toc_headers.append('# Tickets')

    bulleted_links = []
    for c in toc_headers:
        bulleted_links.append(_convert_to_bulleted_link(c, md))

    md.gen_heading('Table of Content', 1)
    for b in bulleted_links:
        md.gen_unwrapped_line(b)

    md.gen_page_break()


def gen_tickets_stats_by_category(by_category, md):
    md.gen_heading('Tickets By Category', 1)
    md.gen_line('')

    for category in by_category:
        md.gen_heading(category.capitalize(), 2)
        md.gen_line('')

        # Get header and all rows to generate table, set category as first col
        header = [category.capitalize()]
        rows = []
        ticket_stats_list = list(by_category[category].values())
        if len(ticket_stats_list) > 0:
            header += [k.capitalize() for k in ticket_stats_list[0].keys()]

        for category_value in by_category[category]:
            ticket_stats = by_category[category][category_value]
            rows.append([category_value] + list(ticket_stats.values()))

        md.gen_table(header, rows, align='left')
        md.gen_line('')
    return md.content


def get_ticket_md_content(tickets, ticket_id, description_width):
    md = markdown_generator.MarkdownGenerator()
    ticket_meta = tickets[ticket_id]['meta']

    ticket_link = tickets[ticket_id].get('comment_attachment', {}).get('link', None)
    if ticket_link is not None:
        md.gen_heading(md.gen_hyperlink(ticket_id, ticket_link), 2)
        md.gen_line('')

    md.gen_heading('Meta', 3)
    md.gen_line('')

    description = ticket_meta.get('description', None)
    summary = ticket_meta.get('summary', None)

    ticket_meta.pop('description', None)
    ticket_meta.pop('summary', None)

    md.gen_wrapped_table(header=[k.capitalize() for k in ticket_meta.keys()], rows=[ticket_meta.values()])
    md.gen_line('')

    if description:
        md.gen_raw_text(md.gen_bold('Description'))
        md.gen_line('')

        if ticket_id == '3384':
            description = re.sub('%s}}}', '%s}\n}\n}', description)

        # TODO: Make sure Trac [url description] syntax is on a single line in the generated Markdown
        # description = re.sub(r"\[([^ ]*) ([^]]*)]", r"[\1](\2)", description)

        description = description.replace('{{{', '```')
        description = description.replace('}}}', '```')

        markdown_link_format_pattern = '[{}]({})'
        description = TextJustifier('\n', markdown_link_format_pattern).wrap(description, width=description_width)

        # Two lines after the opening (and after the ending) back-ticks misses up with the text area rendering.
        description = re.sub('```\n\n', '```\n', description)
        description = re.sub('\n\n```', '\n```', description)

        # For ticket 2624 where the opening three curly braces are not on a separate line.
        description = re.sub(r'```(?!\n)', '```\n', description)
        description = re.sub(r'(?!\n)```', '\n```', description)

        # For ticket 2993 where the defective closing curly brackets miss up with text area rendering.
        description = re.sub('}}:', '```\n', description)

        # A bit hacky, but resolves the issue of ticket 3771 that contains whitespace-composed lines.
        description = re.sub(r'[ ]{8,}', ' ', description)

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
            comment['description'] = justifier.wrap(comment['description'], width=57)
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

    return md.content


def gen_individual_tickets_info(tickets, md, description_width):
    md.gen_line_break()
    md.gen_heading('Tickets', 1)
    md.gen_line('')

    mds = Parallel(n_jobs=8)(
        delayed(get_ticket_md_content)(tickets, ticket_id, description_width) for ticket_id in tickets)
    for tmd in mds:
        md.gen_raw_md(tmd)


def remove_unnecessary_columns(addenda):
    for el in addenda:
        el.pop('link', None)
        el.pop('guid', None)
        el.pop('title', None)
        el.pop('category', None)
    return addenda


def gen_top_level_notes(top_level_notes_md, md):
    md.gen_raw_md(top_level_notes_md)
    md.gen_page_break()
