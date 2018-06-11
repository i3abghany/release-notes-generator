import codecs
import csv
from retry import retry
import urllib.request as request


trac_base = 'https://devel.rtems.org'
ticket_base = trac_base + '/ticket'
format_rss = 'format=rss'
format_csv = 'format=csv'
query = 'query'
attachment_set = 'attachment set'

# TODO Generate csv url for 'reporter' and 'owner' columns
cols_of_interest = ['type', 'priority', 'component', 'version', 'severity']


def ticket_url(number):
    return ticket_base + '/' + str(number)


def ticket_rss(number):
    return ticket_url(number) + '?' + format_rss


def ticket_csv(number):
    return ticket_url(number) + '?' + format_csv


def trac_query_csv(cols, **filters):
    return gen_trac_query_url(cols, **filters) + '&' + format_csv


def gen_attachment_link(attachment_name, ticket_number):
    return '/'.join([trac_base, 'attachment', 'ticket', str(ticket_number), attachment_name])


def gen_trac_query_url(cols, **filters):
    constraints = []
    for col in cols:
        constraints.append('col={c}'.format(c=col))
    for key, value in filters.items():
        constraints.append('{k}={v}'.format(k=key, v=value))
    constraints_str = '&'.join(constraints)
    return trac_base + '/' + query + '?' + constraints_str


def count(**filters):
    csv_url = trac_query_csv(['id'], **filters)
    csv_rows = parse_csv(csv_url)
    next(csv_rows, None)  # skip header

    num_rows = 0
    for _ in csv_rows:
        num_rows += 1
    return num_rows


@retry(exceptions=(ConnectionError, TimeoutError), delay=1, tries=6, backoff=2)
def parse_csv(url):
    csv_response = request.urlopen(url)
    return csv.reader(codecs.iterdecode(csv_response, 'utf-8-sig'))
