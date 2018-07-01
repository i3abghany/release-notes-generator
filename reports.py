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
    md.gen_heading('Tickets', 1)
    md.gen_line('')

    for ticket_id in tickets:
        # Generate markdown for ticket meta data
        ticket_meta = tickets[ticket_id]['meta']

        ticket_link = tickets[ticket_id].get('comment_attachment', {})\
            .get('link', None)
        if ticket_link:
            md.gen_heading(md.gen_hyperlink(ticket_id, ticket_link), 2)
            md.gen_line('')

        md.gen_heading('meta', 3)
        md.gen_line('')

        description = ticket_meta.get('description', None)
        summary = ticket_meta.get('summary', None)

        ticket_meta.pop('description', None)
        ticket_meta.pop('summary', None)

        md.gen_table(header=ticket_meta.keys(), rows=[ticket_meta.values()])
        md.gen_line('')

        if description:
            md.gen_bullet_point(md.gen_bold('description'))
            md.gen_raw_text(description)
            md.gen_line('')

        if summary:
            md.gen_bullet_point(md.gen_bold('summary'))
            md.gen_raw_text(summary)
            md.gen_line('')

        # Generate markdown for ticket's comments or attachments
        items = tickets[ticket_id]['comment_attachment']['items']
        comments = items.get('comments', None)
        attachments = items.get('attachments', None)

        if len(comments) > 0:
            comments_header = comments[0].keys()
            comments_rows = []
            for comment in comments:
                comments_rows.append(list(comment.values()))
            md.gen_heading('comments', 3)
            md.gen_line('')
            md.gen_table(comments_header, comments_rows)
            md.gen_line('')

        if len(attachments) > 0:
            attachments_header = attachments[0].keys()
            attachments_rows = []
            for attachment in attachments:
                attachments_rows.append(list(attachment.values()))
            md.gen_heading('attachments', 3)
            md.gen_line('')
            md.gen_table(attachments_header, attachments_rows)
            md.gen_line('')
