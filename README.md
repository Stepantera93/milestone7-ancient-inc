# Milestone 7 — Ancient, Inc.

This project exposes an API for generating employee birthday and hiring anniversary reports.

## Features

- `GET /birthdays?month=april&department=HR` — lists birthdays by month and department
- `GET /anniversaries?month=april&department=HR` — lists hire date anniversaries

## How to Run

1. Run the Flask server:

   
   python3 server.py

   ## Files

- `server.py` — Flask API server
- `fetch_report.py` — CLI tool to fetch reports
- `employees.json` — Sample employee data
- `README.md` — Project description

## Check the report using the fetch tool:
Run this command to get a birthday report for a given month and department:
   python3 fetch_report.py april HR 