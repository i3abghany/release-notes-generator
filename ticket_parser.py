# Add Copyright

import codecs
import csv
import json
import pprint
import urllib.request as request
import rtems_trac
import xml.etree.ElementTree as ElementTree


class TicketParser:
    def __init__(self, number):
        self.ticket_number = number
        self.ticket_rss = rtems_trac.ticket_rss(number)
        self.ticket_csv = rtems_trac.ticket_csv(number)

    def parse_ticket_meta(self):
        return {'csv': self._parse_ticket_csv(), 'rss': self._parse_ticket_rss()}

    def _parse_ticket_csv(self):
        ticket_csv_url = request.urlopen(self.ticket_csv)
        csv_table = csv.DictReader(codecs.iterdecode(ticket_csv_url, 'utf-8-sig'))
        try:
            return dict(next(csv_table))
        except StopIteration:
            pass  # use RTEMS toolkit's error.general()

    def _parse_ticket_rss(self):
        ticket_rss_dict = {}
        ns = {'dc': '{http://purl.org/dc/elements/1.1/}'}
        rss_response = request.urlopen(self.ticket_rss)
        ticket_xml_root = ElementTree.parse(rss_response).getroot()

        ticket_rss_dict['title'] = self._remove_tags(ticket_xml_root.find('channel/title').text)
        ticket_rss_dict['link'] = self._remove_tags(ticket_xml_root.find('channel/link').text)
        ticket_rss_dict['description'] = self._remove_tags(ticket_xml_root.find('channel/description').text)
        ticket_rss_dict['generator'] = self._remove_tags(ticket_xml_root.find('channel/generator').text)
        ticket_rss_dict['comments'] = self._parse_ticket_comments_and_attachments(ticket_xml_root, ns)

        return ticket_rss_dict

    @staticmethod
    def _remove_tags(text):
        try:
            wrapped_text = '<a>' + (text or '') + '</a>'
            # construct an element tree from string
            xml_tree = ElementTree.fromstring(wrapped_text)
            # leave out tags
            xml_text = ''.join(xml_tree.itertext())
            # replace multiple whitespaces, newlines and tabs with one whitespace
            return ' '.join(xml_text.split()).strip()
        except ElementTree.ParseError:
            return text

    def _parse_ticket_comments_and_attachments(self, ticket_xml_root, ns):
        items_dict = {'comments': [], 'attachments': []}
        for item in ticket_xml_root.findall('channel/item'):
            item_dict = {}
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
                attachment_name = TicketParser._get_attachment_name_from_description(description)
                item_dict['attachment_link'] = rtems_trac.gen_attachment_link(attachment_name, self.ticket_number)
                items_dict['attachments'].append(item_dict)
            else:
                items_dict['comments'].append(item_dict)
        return items_dict

    @staticmethod
    def _get_attachment_name_from_description(description):
        try:
            wrapped_text = '<a>' + (description or '') + '</a>'
            xml_tree_root = ElementTree.fromstring(wrapped_text)
            attachment_name = next(xml_tree_root.iter('em'), '').text
            return attachment_name
        except ElementTree.ParseError:
            return ''


tp = TicketParser(2802)
pp = pprint.PrettyPrinter(indent=4)
output = tp.parse_ticket_meta()

pp.pprint(output)
with open('ticket_parsing_output.json', 'w') as f:
    json.dump(output, f, indent=4)


# # print xml tree
# import xml.dom.minidom
# xml = xml.dom.minidom.parseString(request.urlopen(rtems_trac.ticket_rss(2988)).read())
# pretty_xml_as_string = xml.toprettyxml()
# print(pretty_xml_as_string)
