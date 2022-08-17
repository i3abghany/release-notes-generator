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

import m2r
from joblib import Parallel, delayed

from markdown_generator import MarkdownGenerator
from rst_generator import RstGenerator
from text_justifier import TextJustifier


class ReportsGenerator:
    def __init__(self, fmt='markdown'):
        self.format = fmt
        self.generator = MarkdownGenerator() if fmt == 'markdown' or fmt == 'trac' else RstGenerator()

    def gen_overall_progress(self, overall_progress):
        self.generator.gen_heading('Overall Progress', 1)
        self.generator.gen_table([k.capitalize() for k in overall_progress.keys()], [overall_progress.values()], align='left')
        return self.generator.content

    def gen_tickets_summary(self, tickets):
        self.generator.gen_line_break()
        self.generator.gen_heading('Tickets Summary', 1)

        keys = tickets.keys()
        id_summary_mapping = [(k, tickets[k]['meta']['summary']) for k in keys]
        cols = ['ID', 'Summary']
        self.generator.gen_table(cols, id_summary_mapping, align='left', max_col_width=-1)
        self.generator.gen_line_break()
        return self.generator.content

    @staticmethod
    def _convert_to_bulleted_link(name: str, generator):
        level = name.count('#')
        stripped_name = name.replace('#', '').strip()
        if isinstance(generator, MarkdownGenerator):
            stripped_name = f"**<font size=4.5>{stripped_name}</font>**"
        linked_name = name.lower().replace(' ', '-').replace('-', '', 1).replace('#', '', level - 1)
        if isinstance(generator, MarkdownGenerator):
            linked_name = linked_name.replace('.', '')
        else:
            linked_name = linked_name.replace('.', '-')

        return f"{('    ' * (level - 1)) + '* '}[{stripped_name}]({linked_name})"

    def gen_toc(self, top_headings, categories):
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
            bulleted_links.append(self._convert_to_bulleted_link(c, self.generator))

        self.generator.gen_heading('Table of Content', 1)
        for b in bulleted_links:
            self.generator.gen_unwrapped_line(b)

        self.generator.gen_page_break()

    def gen_tickets_stats_by_category(self, by_category):
        self.generator.gen_heading('Tickets By Category', 1)
        self.generator.gen_line('')

        for category in by_category:
            self.generator.gen_heading(category.capitalize(), 2)

            # Get header and all rows to generate table, set category as first col
            header = [category.capitalize()]
            rows = []
            ticket_stats_list = list(by_category[category].values())
            if len(ticket_stats_list) > 0:
                header += [k.capitalize() for k in ticket_stats_list[0].keys()]

            for category_value in by_category[category]:
                ticket_stats = by_category[category][category_value]
                rows.append([category_value] + list(ticket_stats.values()))

            self.generator.gen_table(header, rows, align='left')
            self.generator.gen_line('')
        return self.generator.content

    @staticmethod
    def get_ticket_md_content(tickets, ticket_id, description_width, fmt='markdown'):
        md = MarkdownGenerator()
        ticket_meta = tickets[ticket_id]['meta']

        ticket_link = tickets[ticket_id].get('comment_attachment', {}).get('link', None)
        if ticket_link is not None:
            md.gen_heading(md.gen_hyperlink(ticket_id, ticket_link), 2)

        description = ticket_meta.get('description', None)
        summary = ticket_meta.get('summary', None)
        ticket_meta.pop('description', None)
        ticket_meta.pop('summary', None)

        md.gen_heading('Meta', 3)
        meta_headers = [k.capitalize() for k in ticket_meta.keys()]
        meta_vals = [[v if v != '' else 'N.A.' for v in ticket_meta.values()]]
        md.gen_wrapped_table(header=meta_headers, rows=meta_vals)

        ReportsGenerator._format_description(description, description_width, fmt, md, ticket_id)
        ReportsGenerator._format_summary(md, summary)

        # Generate markdown for ticket's comments or attachments
        items = tickets[ticket_id]['comment_attachment']['items']
        comments = items.get('comments', None)
        comments = ReportsGenerator._remove_unnecessary_columns(comments)
        attachments = items.get('attachments', None)
        attachments = ReportsGenerator._remove_unnecessary_columns(attachments)

        ReportsGenerator._format_comments(comments, fmt, md)
        ReportsGenerator._format_attachments(attachments, fmt, md)

        return md.content

    @staticmethod
    def _format_summary(md, summary):
        if summary is None:
            return
        md.gen_raw_text(md.gen_bold('Summary'))
        md.gen_line('')
        summary = summary.replace('{{{', '```')
        summary = summary.replace('}}}', '```')
        md.gen_raw_text(summary)
        md.gen_line('')

    @staticmethod
    def _format_description(description, description_width, fmt, md, ticket_id):
        if description is None:
            return
        description = description.replace('\r\n', '\n')

        md.gen_raw_text(md.gen_bold('Description'))
        md.gen_line('')

        if ticket_id == '3384':
            description = re.sub('%s}}}', '%s}\n}\n}', description)

        # TODO: Make sure Trac [url description] syntax is on a single line in the generated Markdown
        # description = re.sub(r"\[([^ ]*) ([^]]*)]", r"[\1](\2)", description)

        description = description.replace('{{{\n', '```\n')
        description = description.replace('\n}}}', '\n```')

        if fmt == 'markdown':
            description = re.sub(r'{{{(?!\n)', '`', description)
            description = re.sub(r'(?!\n)}}}', '`', description)
        else:
            description = re.sub(r'{{{(?!\n)', ':code:`', description)
            description = re.sub(r'(?!\n)}}}', '`', description)

        markdown_link_format_pattern = '[{}]({})'
        if fmt == 'markdown':
            description = TextJustifier('\n', markdown_link_format_pattern).wrap(description, width=description_width)

        # Two lines after the opening (and after the ending) back-ticks misses up with the text area rendering.
        description = re.sub('```\n\n', '```\n', description)
        description = re.sub('\n\n```', '\n```', description)

        # For ticket 2624 where the opening three curly braces are not on a separate line.
        description = re.sub(r'```(?!\n)', '```\n', description)
        description = re.sub(r'(?!\n)```', '\n```', description)

        # For ticket 2993 where the defective closing curly brackets miss up with text area rendering.
        description = re.sub('}}:', '```\n', description)

        # Ticket 3771 has code that's not written in a code block, which is interpretted by the Markdown generator
        # as headers (#define)... Hence, we fix that manually.

        if ticket_id == '3771':
            description = re.sub('#define', '```\n#define', description, count=1)
            description = re.sub('Problem facing on writing', '```\nProblem facing on writing', description, count=1)
            description = re.sub(r'[ ]{8,}', ' ', description)

        md.gen_raw_text(description)
        md.gen_line('')

    @staticmethod
    def _format_comments(comments, fmt, md):
        if len(comments) == 0:
            return
        comments_header = comments[0].keys()
        comments_rows = []
        if fmt == 'markdown':
            justifier = TextJustifier('<br />', '[{}]({})')
            for comment in comments:
                comment['description'] = justifier.wrap(comment['description'], width=57)
            md.gen_heading('Comments', 3)
        else:
            md.gen_line(md.gen_bold('Comments'))
            md.gen_line('')

        for comment in comments:
            comments_rows.append(list(comment.values()))
        if fmt == 'markdown':
            md.gen_table(comments_header, comments_rows, max_col_width=-1)
        else:
            for c in comments_rows:
                md.gen_comment_card(comments_header, c)
        md.gen_line('')

    @staticmethod
    def _format_attachments(attachments, fmt, md):
        if len(attachments) == 0:
            return
        attachments_header = attachments[0].keys()
        attachments_rows = []
        for attachment in attachments:
            attachments_rows.append(list(attachment.values()))
            attachments_rows[-1][3] = '[{}]({})'.format("link", attachments_rows[-1][3])

        if fmt == 'markdown':
            md.gen_heading('Attachments', 3)
        else:
            md.gen_line(md.gen_bold('Attachments'))
            md.gen_line('')
        md.gen_table(attachments_header, attachments_rows, max_col_width=-1)
        md.gen_line('')

    def gen_individual_tickets_info(self, tickets):
        self.generator.gen_line_break()
        self.generator.gen_heading('Tickets', 1)
        description_width = 100 if self.format == 'markdown' else 75

        generated_content = Parallel(n_jobs=8)(
            delayed(self.get_ticket_md_content)(tickets, ticket_id, description_width, self.format) for ticket_id in tickets)
        if self.format == 'markdown' or self.format == 'trac':
            for ticket_content in generated_content:
                self.generator.gen_raw_md(ticket_content)
        else:
            for ticket_content in generated_content:
                rst_content = m2r.convert(ticket_content)
                self.generator.gen_raw_rst(rst_content)

    @staticmethod
    def _remove_unnecessary_columns(addenda):
        for el in addenda:
            el.pop('link', None)
            el.pop('guid', None)
            el.pop('title', None)
            el.pop('category', None)
        return addenda

    def gen_top_level_notes(self, top_level_notes_md):
        if self.format == 'markdown' or self.format == 'trac':
            self.generator.gen_raw_md(top_level_notes_md)
            self.generator.gen_page_break()
        else:
            rst_notes = m2r.convert(top_level_notes_md)
            self.generator.gen_raw_rst(rst_notes)
