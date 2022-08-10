#
# RTEMS Tools Project (http://www.rtems.org/)
# Copyright 2012 Mahmoud Abumandour (ma.mandourr@gmail.com)
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
import m2r

import markdown_generator


class RstGenerator:
    def __init__(self):
        self.content = ''

    def gen_bullet_point(self, txt):
        self.content += f'* {txt}'

    def gen_line(self, txt):
        self.content += f'\n{txt}\n'

    def gen_unwrapped_line(self, txt):
        self.gen_line(txt)

    def gen_table(self, headers, rows, align='left', max_col_width=38):
        md = markdown_generator.MarkdownGenerator()
        md.gen_table(headers, rows, align=align, max_col_width=max_col_width)
        self.content += m2r.convert(md.content)

    def gen_heading(self, txt, _):
        self.content += f'\n{txt}\n'
        self.content += '=' * (len(txt) + 1)
        self.content += '\n'

    def gen_line_break(self):
        self.content += '\n|br|'

    def gen_raw_rst(self, txt):
        self.content += txt

    def gen_page_break(self):
        self.content += '\n'
        self.content += '.. raw:: html\n'
        self.content += '<div style="page-break-after: always"></div>\n'

    @staticmethod
    def gen_bold(txt):
        return f'**{txt}**'


