#
# RTEMS Tools Project (http://www.rtems.org/)
# Copyright 2022 Mahmoud Abumandour (ma.mandourr@gmail.com)
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

import markdown2


class HTMLGenerator:
    CSS_TABLE_CLASSES = 'listing tickets'
    CSS_TRAC_CONTENT_CLASS = 'trac-content'
    CSS_NEW_PAGE_CLASS = 'new-page'

    HTML_TICKET_NUMBER_TAG_PATTERN = '<h2><a'
    HTML_TICKET_NUMBER_WITH_NEW_PAGE = '<h2 class="new-page"><a'
    HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="{}" type="text/css" />
    </head>
    <body>
        <div class="{}">
            {}
        </div>
    </body>
</html>
"""

    def __init__(self, stylesheet_path):
        self.stylesheet_path = stylesheet_path
        self.code_area_threshold = 20

    def from_markdown(self, markdown_str):
        html = markdown2.markdown(markdown_str, extras=['tables', 'code-friendly', 'fenced-code-blocks'])
        html = self._insert_style_classes(html)
        op = self.HTML_TEMPLATE.format(self.stylesheet_path,
                                       self.CSS_TRAC_CONTENT_CLASS,
                                       html.replace('\n', '\n\t\t'))
        return op

    def _insert_style_classes(self, html):
        html = html.replace('<table>', '<table class="{}" />'.format(self.CSS_TABLE_CLASSES))

        # Inserting a page break before all tickets but for the first.
        html = html.replace(self.HTML_TICKET_NUMBER_TAG_PATTERN, self.HTML_TICKET_NUMBER_WITH_NEW_PAGE) \
                   .replace(self.HTML_TICKET_NUMBER_WITH_NEW_PAGE, self.HTML_TICKET_NUMBER_TAG_PATTERN, 1)
        start = 0
        for _ in range(html.count('<code>')):
            open_idx = html.find('<code>', start)
            close_idx = html.find('</code>', start)

            if html.find('\n', open_idx, close_idx) == -1 or (close_idx - open_idx < self.code_area_threshold):
                start = close_idx + len('</code>')
                continue

            html = html[:close_idx] + '</pre>' + html[close_idx + len('</code>'):]
            html = html[:open_idx] + '<pre class="wiki">' + html[open_idx + len('<code>'):]
            start = close_idx + len('</pre>')
        return html
