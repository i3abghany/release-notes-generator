# ReleaseNotesGenerator
This repo contains code for generating RTEMS release notes.
Introduction: This project aims to automatically create the RTEMS release notes for a release from the Trac data by using XML parser (Python). Since all changes on a release branch must have a ticket, the ticket is assigned the Version and Milestone. Therefore, web pages are converted to a PDF as the release notes.

## Current Markdown Version
tickets.py is currently supported by Python 2.7 and Python 3.6.

To run `release_notes.py` to get a realease note, use this command line:
```
python2 release_notes.py --milestone_id 4.11.3
```
In this example, running this command, you will get a realse note which contains tickets info from milestone 4.11.3
