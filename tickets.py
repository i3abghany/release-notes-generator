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
import codecs
import pprint

try:
    import urllib.request as urllib_request
except ImportError:
    import urllib2 as urllib_request
import rtems_trac
import xml.etree.ElementTree as ElementTree
import markdown


class tickets:
    """This class load all tickets data for a milestone."""

    def __init__(self, milestone_id):
        self.tickets_id = milestone_id
        self.tickets = {}

    def get_ticket_ids(self):
        return self.tickets.keys()

    def load(self):
        # Read entire trac table as DictReader (iterator)
        tickets_dict_iter = self._get_tickets_table_as_dict()
        self._pre_process_tickets_stats()
        # Parse ticket data
        for ticket in tickets_dict_iter:
            print('processing ticket {t} ...'.format(t=ticket['id']))
            self.tickets['tickets'][ticket['id']] \
                = self._parse_ticket_data(ticket)
        self._post_process_ticket_stats()

    def _pre_process_tickets_stats(self):
        self.tickets['overall_progress'] = {}
        self.tickets['by_category'] \
            = {col: {} for col in rtems_trac.aggregate_cols}

        self.tickets['overall_progress']['total'] = 0
        self.tickets['overall_progress']['closed'] = 0
        self.tickets['overall_progress']['in_progress'] = 0
        self.tickets['overall_progress']['new'] = 0
        self.tickets['overall_progress']['assigned'] = 0
        self.tickets['tickets'] = {}

    def _post_process_ticket_stats(self):
        # (number of closed tickets) / (number of total tickets)
        self.tickets['overall_progress']['percentage'] \
            = "{0:.0%}".format(self.tickets['overall_progress'].get('closed', 0)
                               / self.tickets['overall_progress'].get('total', 0))
        # Get progress (closed/total) for each category
        for col in self.tickets['by_category']:
            for key in self.tickets['by_category'][col]:
                closed = self.tickets['by_category'][col][key].get('closed', 0)
                total = self.tickets['by_category'][col][key]['total']
                self.tickets['by_category'][col][key]['progress'] \
                    = '{c}/{t}'.format(c=closed, t=total)

    def _get_tickets_table_as_dict(self):
        csv_url = rtems_trac.gen_trac_query_csv_url(
            rtems_trac.all_cols, milestone=self.tickets_id)
        return rtems_trac.parse_csv_as_dict_iter(csv_url)

    def _parse_ticket_data(self, ticket):
        self.tickets['overall_progress']['total'] += 1
        if ticket['Status'] == 'closed':
            self.tickets['overall_progress']['closed'] += 1
        if ticket['Status'] == 'assigned':
            self.tickets['overall_progress']['assigned'] += 1
        if ticket['Status'] == 'new':
            self.tickets['overall_progress']['new'] += 1

        for col in rtems_trac.aggregate_cols:
            col_value = ticket[col.capitalize()]
            self.tickets['by_category'][col][col_value] \
                = self.tickets['by_category'][col].get(col_value, {})
            if ticket['Status'] == 'closed':
                self.tickets['by_category'][col][col_value]['closed'] \
                    = self.tickets['by_category'][col][col_value] \
                          .get('closed', 0) + 1
            self.tickets['by_category'][col][col_value]['total'] \
                = self.tickets \
                      ['by_category'][col][col_value].get('total', 0) + 1

        return {'meta': self._parse_ticket_csv(ticket['id']),
                'comment_attachment': self._parse_ticket_rss(ticket['id'])}

    @staticmethod
    def _parse_ticket_csv(ticket_id):
        ticket_csv_url = rtems_trac.gen_ticket_csv_url(ticket_id)
        csv_rows_iter = rtems_trac.parse_csv_as_dict_iter(ticket_csv_url)
        return dict(next(csv_rows_iter, {}))

    def _parse_ticket_rss(self, ticket_id):
        # Read xml data as ElementTree, and parse all tags
        ticket_rss_dict = {}
        ns = {'dc': '{http://purl.org/dc/elements/1.1/}'}
        ticket_rss_url = rtems_trac.gen_ticket_rss_url(ticket_id)
        rss_response = urllib_request.urlopen(ticket_rss_url)
        ticket_xml_root = ElementTree.parse(rss_response).getroot()

        ticket_rss_dict['title'] = self._remove_tags(
            ticket_xml_root.find('channel/title').text
        )
        ticket_rss_dict['link'] = self._remove_tags(
            ticket_xml_root.find('channel/link').text
        )
        ticket_rss_dict['description'] = self._remove_tags(
            ticket_xml_root.find('channel/description').text
        )
        ticket_rss_dict['generator'] = self._remove_tags(
            ticket_xml_root.find('channel/generator').text
        )
        ticket_rss_dict['items'] \
            = self._parse_ticket_comments_and_attachments(
            ticket_id, ticket_xml_root, ns
        )

        return ticket_rss_dict

    @staticmethod
    def _remove_tags(text):
        try:
            wrapped_text = '<a>' + (text or '') + '</a>'
            # construct an element tree from string
            xml_tree = ElementTree.fromstring(wrapped_text.encode('utf-8'))
            # leave out tags
            xml_text = ''.join(xml_tree.itertext())
            # replace multiple whitespaces,
            # newlines and tabs with one whitespace
            return ' '.join(xml_text.split()).strip()
        except ElementTree.ParseError:
            return text

    def _parse_ticket_comments_and_attachments(
            self,
            ticket_id,
            ticket_xml_root,
            ns,
    ):
        items_dict = {'comments': [], 'attachments': []}
        for item in ticket_xml_root.findall('channel/item'):
            item_dict = {}
            description = ''
            is_attachment = item.find('title').text == rtems_trac.attachment_set

            for element in item.findall('*'):
                if element.tag.startswith(ns['dc']):
                    tag_name = element.tag[len(ns['dc']):]
                else:
                    tag_name = element.tag

                if is_attachment and element.tag == 'description':
                    description = element.text
                item_dict[tag_name] = self._remove_tags(element.text)

            # if current item is an attachment
            if item_dict.get('title') == rtems_trac.attachment_set:
                attachment_name \
                    = tickets._get_attachment_name_from_description(description)
                item_dict['attachment_link'] = rtems_trac.gen_attachment_link(
                    attachment_name, ticket_id
                )
                items_dict['attachments'].append(item_dict)
            else:
                items_dict['comments'].append(item_dict)
        return items_dict

    @staticmethod
    def _get_attachment_name_from_description(description):
        try:
            wrapped_text = '<a>' + (description or '') + '</a>'
            xml_tree_root = ElementTree.fromstring(wrapped_text.encode('utf-8'))
            attachment_name = next(xml_tree_root.iter('em'), '').text
            return attachment_name
        except ElementTree.ParseError:
            return ''


if __name__ == '__main__':
    tickets = tickets(milestone_id='4.11.3')
    pp = pprint.PrettyPrinter(indent=4)
    tickets.load()
    pp.pprint(tickets.tickets)

    import json2html

    with open('tickets.html', 'w', encoding='utf-8') as html_file:
        html_file.write(json2html.json2html.convert(tickets.tickets))
