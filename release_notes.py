import markdown
import reports
import tickets


# Fetch tickets data
t = tickets.tickets(milestone_id='4.11.3')
t.load()
tickets_stats = t.tickets

# Generate markdown format for data
md = markdown.markdown()
reports.gen_overall_progress(tickets_stats['overall_progress'], md)
reports.gen_tickets_stats_by_category(tickets_stats['by_category'], md)
reports.gen_individual_tickets_info(tickets_stats['tickets'], md)

with open('tickets.md', 'w', encoding='utf-8') as file:
    file.write(md.content)
