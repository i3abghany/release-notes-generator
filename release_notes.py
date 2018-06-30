import markdown
import reports
import tickets


t = tickets.tickets(milestone_id='4.11.3')
t.load()
tickets_stats = t.tickets

md = markdown.markdown()
reports.gen_overall_progress(tickets_stats['overall_progress'], md)
reports.gen_tickets_stats_by_category(tickets_stats['by_category'], md)
reports.gen_individual_tickets_info(tickets_stats['tickets'], md)

with open('tickets.md', 'w') as file:
    file.write(md.content)
