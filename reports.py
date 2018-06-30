import markdown


def gen_overall_progress(overall_progress, md = markdown.markdown()):
    md.gen_heading('Overall Progress', 1)
    md.gen_line('')
    md.gen_table(overall_progress.keys(), [overall_progress.values()])
    md.gen_line('')
    return md.content


def gen_tickets_stats_by_category(by_category, md = markdown.markdown()):
    md.gen_heading('By Category', 1)
    md.gen_line('')

    for category in by_category:
        md.gen_heading(category, 2)
        md.gen_line('')

        # Get header and all rows to generate table, set category as first col
        header = [category]
        rows = []
        ticket_stats_list = list(by_category[category].values())
        if len(ticket_stats_list) > 0:
            header += ticket_stats_list[0].keys()

        for category_value in by_category[category]:
            ticket_stats = by_category[category][category_value]
            rows.append([category_value] + list(ticket_stats.values()))

        md.gen_table(header, rows)
        md.gen_line('')
    return md.content


def gen_individual_tickets_info(tickets, md = markdown.markdown()):
    for ticket_id in tickets:
        # md.gen_heading(ticket_id, 2)
        # md.gen_line('')

        # Generate markdown for ticket meta data
        ticket_meta = tickets[ticket_id]['meta']
        # md.gen_heading('meta', 3)
        # md.gen_line('')

        # md.gen_table(ticket_meta.keys(), [ticket_meta.values()])
        # md.gen_line('')

        # Generate markdown for ticket's comments and attachments
        # comment_attachment = tickets[ticket_id]['comment_attachment']
