import json
import pprint
import rtems_trac


class MilestoneParser(object):
    def __init__(self, number):
        self.milestone_number = number

    def parse_milestone_stats(self):
        progress_overall = self._compute_progress_overall()
        progress_by_cols = self._compute_progress_by_cols()
        milestone_stats = {'progress_overall': progress_overall, 'progress_by_cols': progress_by_cols}
        return milestone_stats

    def _compute_progress_overall(self):
        total = rtems_trac.count(milestone=self.milestone_number)
        closed = rtems_trac.count(milestone=self.milestone_number, status='closed')
        assigned = rtems_trac.count(milestone=self.milestone_number, status='assigned')
        new = rtems_trac.count(milestone=self.milestone_number, status='new')
        percentage = "{0:.0%}".format(closed / total)
        overall_progress = {'total': total, 'closed': closed, 'open': assigned, 'new': new, 'progress': percentage}
        return overall_progress

    def _compute_progress_by_cols(self):
        progress_by_cols = {}
        for col in rtems_trac.cols_of_interest:
            progress_by_cols[col] = {}
            col_values = self._get_col_values(col)
            for col_value in col_values:
                filters_total = {'milestone': self.milestone_number, col: col_value}
                total = rtems_trac.count(**filters_total)
                if total > 0:
                    filters_closed = {'milestone': self.milestone_number, col: col_value, 'status': 'closed'}
                    closed = rtems_trac.count(**filters_closed)
                    progress_by_cols[col][col_value] = '{c}/{t}'.format(c=closed, t=total)
        return progress_by_cols

    def _get_col_values(self, col):
        col_values = set()
        cols = ['id', col]

        csv_url = rtems_trac.trac_query_csv(cols, milestone=self.milestone_number)
        csv_rows = rtems_trac.parse_csv(csv_url)

        next(csv_rows, None)
        for row in csv_rows:
            col_values.add(row[len(cols) - 1])
        return col_values


mp = MilestoneParser('4.11.3')
pp = pprint.PrettyPrinter(indent=4)
output = mp.parse_milestone_stats()

pp.pprint(output)

with open('milestone_parsing_output.json', 'w') as f:
    json.dump(output, f, indent=4)

