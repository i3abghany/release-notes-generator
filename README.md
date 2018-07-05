# ReleaseNotesGenerator
This repo contains code for generating RTEMS release notes.

## Current Markdown Version
tickets.py is currently supported by Python 3.6, I am still working on it to make it compatiable with Python 2.7.

To run `release_notes.py` to get a realease note, use this command line:
```
python3 release_notes.py --milestone_id 4.11.3
```
In this example, running this command, you will get a realse note which contains tickets info from milestone 4.11.3
