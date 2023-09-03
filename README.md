# Job Search and Data Extraction Script

## Overview
This Python script is designed to scrape job information from the TimesJobs website and export the results to an Excel file. It uses the BeautifulSoup library for web scraping and the openpyxl library to create and manipulate Excel files.

## Features
- Searches for job listings in Pune related to "Back Office" with various filter options.
- Filters out job listings containing certain banned words (e.g., "voice" or "call").
- Extracts job details including the company name, required skills, and a link to apply.
- Stores the collected data in an Excel spreadsheet.

## Prerequisites
Before using this script, make sure you have the following installed:

1. Python (3.7+)
2. Required Python packages (beautifulsoup4, openpyxl, requests)

You can install the required packages using pip:
```bash
pip install beautifulsoup4 openpyxl requests
