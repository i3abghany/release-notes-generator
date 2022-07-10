# release-notes-generator
This repo contains code for generating RTEMS release notes.

# Introduction
This project aims to automatically create the RTEMS release notes for a release from the Trac data by using XML parser (Python). Since all changes on a release branch must have a ticket, the ticket is assigned the Version and Milestone. Therefore, web pages are converted to a PDF as the release notes pertaining to a format and a set of styles.

# Usage

To download and install python dependencies, please run `pip install -r requirements.txt`

Currently, the generator supports two set of styles that can be used for the final produced PDF file.
Those are `trac` and `markdown`. The style set to use is an invocation-time parameter.
An example usage, which produces the release notes PDF file for 4.11.3 milestone using
GitHub-Markdown-like styles would be:

```commandline
python ./release_notes.py --milestone_id=4.11.3 --style=markdown
```