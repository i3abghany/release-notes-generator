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
from text_justifier import TextJustifier


class MarkdownGenerator:
    def __init__(self, line_width=78):
        self.content = ''
        self.line_width = line_width

    def gen_bullet_point(self, text):
        self.content += '* ' + self.wrap_line(self._convert_to_unicode_str(text), self.line_width) + '\n'

    def gen_line(self, text):
        self.content += self.wrap_line(self._convert_to_unicode_str(text), self.line_width) + '\n'

    def gen_unwrapped_line(self, text, is_raw_text=True):
        self.content += text
        self.content += ('  \n' if is_raw_text else '<br />')

    def gen_heading(self, text, level):
        self.content += '\n' + ('#' * level) + ' ' + self._convert_to_unicode_str(text) + '\n\n'

    def gen_wrapped_table(self, header, rows, max_num_cols=4):
        num_cols = len(header)
        i = 0
        if num_cols > max_num_cols:
            while i < num_cols:
                self.gen_table(
                    list(header)[i:i + max_num_cols],
                    [list(row)[i:i + max_num_cols] for row in rows],
                )
                self.gen_line('\n')
                i += max_num_cols
        else:
            self.gen_table(header, rows, align='left')

    def gen_page_break(self):
        self.gen_line('<div class="new-page"></div>')

    def gen_line_break(self):
        self.gen_line('')
        self.gen_line('')
        self.gen_line('<br />')

    def gen_raw(self, content):
        self.content += content

    def gen_table(self, header, rows, align='left', max_col_width=38):
        num_columns = len(header)
        header = [self._convert_to_unicode_str(h) for h in header]

        if max_col_width == -1:
            rows = [[self._convert_to_unicode_str(r) for r in row] for row in rows]
        else:
            rows = [[(self._convert_to_unicode_str(r) if isinstance(r, int) else
                      self.wrap_line(self._convert_to_unicode_str(r), max_col_width)) or ' ' for r in row]
                    for row in rows]

        header_str = '|' + '|'.join(header) + '|'
        column_format = '---'

        if align == 'left':
            column_format = ':' + column_format
        elif align == 'right':
            column_format = column_format + ':'
        else:
            column_format = ':' + column_format + ':'

        split_line = column_format.join(['|'] * (num_columns + 1))
        rows_str = '\n'.join(['|' + '|'.join(row) + '|' for row in rows])
        self.content += '\n'.join([header_str, split_line, rows_str])

    def gen_comment_card(self, comment_headers, comment, horizontal_line=True):
        just = TextJustifier('\n', "{}({})")
        for i, h in enumerate(comment_headers):
            raw_txt = f"\n```\n{comment[i]}\n```"
            self.content += f'**{h.capitalize()}**: {comment[i] if h != "description" else just.wrap(raw_txt, 80)}'
            self.gen_line('')
            self.gen_line('')
        if horizontal_line:
            self.gen_horizontal_line()

    def gen_raw_text(self, formatted_text):
        self.content += '\n' + formatted_text + '\n'

    @staticmethod
    def gen_bold(text):
        return '**' + text + '**'

    @staticmethod
    def gen_hyperlink(text, link):
        return '[' + text + ']' + '(' + link + ')'

    @staticmethod
    def wrap_line(line, width, is_raw_text=False):
        i = 0
        str_list = []
        while i < len(line):
            str_list.append(line[i:i + width])
            i += width
        return ('  \n' if is_raw_text else '<br />').join(str_list)

    def gen_horizontal_line(self):
        self.content += '\n---\n'

    @staticmethod
    def _convert_to_unicode_str(text):
        try:
            return str(text)
        except UnicodeEncodeError:
            if isinstance(text, unicode):
                return text
            else:
                return unicode(text, "utf-8")
