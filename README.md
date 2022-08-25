# release-notes-generator
This repo contains code for generating RTEMS release notes.

# Introduction
This project aims to automatically create the RTEMS release notes for a release from the Trac data by using XML parser (Python). Since all changes on a release branch must have a ticket, the ticket is assigned the Version and Milestone. Therefore, web pages are converted to a PDF as the release notes pertaining to a format and a set of styles.

# Usage

To download and install python dependencies, please run `pip install -r
requirements.txt`

For the `markdown` and `trac` styles, `wkhtmltopdf` is used to generate the
final release notes PDF file. Hence, a `wkhtmltopdf` **with patched qt**
version is required on the system before attempting to run and generate release
notes files using those styles. The generator was mainly tested using
`wkhtmltopdf` version `0.12.5`.

Currently, the generator supports three set of styles that can be used for the
final produced PDF file. Those are `trac` and `markdown`, and `rst` (which is
still W.I.P.).

An example usage, which produces the release notes PDF file for 4.11.3
milestone using GitHub-Markdown-like styles would be:

```commandline
python ./release_notes.py --milestone_id=4.11.3 --style=markdown
```
