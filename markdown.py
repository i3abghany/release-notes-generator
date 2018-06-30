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


class markdown():
    def __init__(self):
        self.content = ''

    def gen_line(self, text):
        self.content += str(text) + '\n'

    def gen_heading(self, text, level):
        self.content += '#' * level + ' ' + str(text)

    def gen_table(self, header, rows, col_width = 80, align ='center'):
        num_columns = len(header)
        header = [self._insert_newline(h, col_width) for h in header]
        rows = [[self._insert_newline(str(r) or ' ', col_width) for r in row]
                for row in rows]

        header_str = '|' + '|'.join(header) + '|'
        column_format = '---'

        if align == 'left':
            column_format = ':' + column_format
        elif align == 'right':
            column_format = column_format + ':'
        elif align == 'center':
            column_format = ':' + column_format + ':'

        split_line = column_format.join(['|'] * (num_columns + 1))
        rows_str = '\n'.join(['|' + '|'.join(row) + '|' for row in rows])
        self.content += '\n'.join([header_str, split_line, rows_str])

    @classmethod
    def _insert_newline(cls, line, col_width):
        newline = '<br>'
        if len(line) > col_width > len(newline):
            line = line[:col_width - len(newline)] \
                   + newline \
                   + line[col_width - len(newline)]
        return line
