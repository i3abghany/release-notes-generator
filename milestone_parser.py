import logging
from parse_html import TracHTMLParser


class MilestoneParser():
    def __init__(self, milestone_id, rtems_url_base="https://devel.rtems.org", milestone="milestone"):
        self._setup_logging()
        self.milestone_id = milestone_id
        self.rtems_url_base = rtems_url_base
        self.milestone = milestone

    def get_milestone_stats(self):
        milestone_stats = {}
        milestone_url = "/".join([self.rtems_url_base, self.milestone, self.milestone_id])
        trac_html_parser = TracHTMLParser()
        self.logger.info("Start parsing milestone page: {milestone_url} ...".format(milestone_url=milestone_url))
        bs = trac_html_parser.parse_page(milestone_url)

        # Parse milestone meta info: title, id and timeline
        self.logger.info("Parsing milestone meta info (title, id, timeline) ...")
        milestone_stats["meta"] = self._get_milestone_meta(bs)

        # Extract overall progress of milestone: percent, total, closed, in progress, new etc.
        self.logger.info("Parsing milestone progress (percent, number of total/closed/new tickets) ...")
        milestone_stats["progress"] = self._get_milestone_progress(bs)

        # Get tickets list
        self.logger.info("Parsing milestone tickets list ...")
        milestone_stats["tickets_list"] = self._get_tickets_list(bs)

        # Get tickets stats by category
        self.logger.info("Parsing tickets status by category (reporter, owner, severity, type etc.) ...")
        milestone_stats["by_category"] = self._get_tickets_status_by_category(bs)
        return milestone_stats

    def _get_milestone_progress(self, bs):
        milestone_progress = {}
        percent_tag = bs.find(name="p", attrs={"class": "percent"})
        milestone_progress["percent"] = percent_tag.string if percent_tag else None

        nums_tag = bs.find(name="span", attrs={"class": "first interval"})
        milestone_progress["total_tickets_num"] = nums_tag.find(name="a").string if nums_tag else None

        closed_tag = nums_tag.find_next_sibling(name="span", attrs={"class": "interval"}) if nums_tag else None
        milestone_progress["closed"] = closed_tag.find(name="a").string if closed_tag else None

        in_progress_tag = closed_tag.find_next_sibling(name="span", attrs={"class": "interval"}) if closed_tag else None
        milestone_progress["in_progress"] = in_progress_tag.find(name="a").string if in_progress_tag else None

        new_tag = in_progress_tag.find_next_sibling(name="span",
                                                    attrs={"class": "interval"}) if in_progress_tag else None
        milestone_progress["new"] = new_tag.find(name="a").string if new_tag else None
        return milestone_progress

    def _get_milestone_meta(self, bs):
        milestone_meta = {}
        milestone_meta["milestone_id"] = self.milestone_id

        title_tag = bs.find(name="div", attrs={"id": "content", "class": "milestone"}).find(name="h1")
        milestone_meta["title"] = title_tag.text if title_tag else None

        timeline_tag = bs.find(name="p", attrs={"class": "date"})
        milestone_meta["timeline"] = timeline_tag.contents[-1].strip() if timeline_tag else None
        return milestone_meta

    def _get_tickets_list(self, bs):
        tickets_list = []
        nums_tag = bs.find(name="span", attrs={"class": "first interval"})
        tickets_list_url = "/".join([self.rtems_url_base, nums_tag.find(name="a")["href"]])

        trac_html_parser = TracHTMLParser()
        self.logger.info("Start parsing tickets list url {tickets_list_url} ...")
        bs = trac_html_parser.parse_page(tickets_list_url)
        all_rows = bs.find(name="table", attrs={"class": "listing tickets"}).find(name="tbody").find_all(name="tr")

        # parse each row to get ticket id, summary, owner, type etc.
        for row in all_rows:
            id = row.find(name="td", attrs={"class": "id"}).string.strip()
            summary = row.find(name="td", attrs={"class": "summary"}).find(name="a").string.strip()
            owner_tag = row.find(name="td", attrs={"class": "owner"})
            span_tag = owner_tag.find(name="span", attrs={"class": "usernamedecorate-anonymous"}) if owner_tag else None
            owner = span_tag.string.strip() if span_tag else None
            type = row.find(name="td", attrs={"class": "type"}).string.strip()
            priority = row.find(name="td", attrs={"class": "priority"}).string.strip()
            component = row.find(name="td", attrs={"class": "component"}).string.strip()
            version = row.find(name="td", attrs={"class": "version"}).string.strip()
            tickets_list.append({"id": id, "summary": summary, "owner": owner, "type": type, "priority": priority, "component": component, "version": version})
        return tickets_list

    def _get_tickets_stats_by_category(self, category):
        category_status_dict = {}
        trac_html_parser = TracHTMLParser()
        status_by_category_url = "/".join([self.rtems_url_base, self.milestone, self.milestone_id]) + "?by=" + category

        self.logger.info("Start parsing 'by {category}' url {status_by_category_url} ...".format(category=category, status_by_category_url=status_by_category_url))
        bs = trac_html_parser.parse_page(status_by_category_url)
        all_rows = bs.find(name="form", attrs={"id": "stats"}).find(name="table").find_all(name="tr", recursive=False)
        for row in all_rows:
            if category in {"reporter", "owner"}:
                option_tag = row.find(name="th", attrs={"scope": "row"}).find(name="span")
            elif category in {"type", "priority", "component", "version", "severity"}:
                option_tag = row.find(name="th", attrs={"scope": "row"}).find(name="a")
            else:
                raise Exception("Unexpected category {category}")

            option = option_tag.string.strip() if option_tag else None
            status = row.find(name="td").find(name="p", attrs={"class": "percent"}).string.strip()
            category_status_dict[option] = status

        return category_status_dict

    def _get_tickets_status_by_category(self, bs):
        milestone_stats_by_category = {}

        status_categories_tag = bs.find(name="select", attrs={"id": "by", "name": "by"})
        status_categories = [option["value"] for option in status_categories_tag.find_all(name="option")]

        for category in status_categories:
            milestone_stats_by_category[category] = self._get_tickets_stats_by_category(category)
        return milestone_stats_by_category

    def _setup_logging(self):
        self.logger = logging.getLogger(__name__)
        self.logger.addHandler(logging.NullHandler())


# This is for test purpose
log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=log_format)
mtp = MilestoneParser(milestone_id="4.11.3")
import pprint
pp = pprint.PrettyPrinter(indent=4)
milestone_stats = mtp.get_milestone_stats()
#pp.pprint(milestone_stats)