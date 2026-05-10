# 📈 SQL Business Intelligence Automator

An automated data engineering pipeline that connects to a relational SQL database, executes complex JOIN queries, and automatically generates monthly financial reports and visualizations using Python.

## ⚠️ The Business Problem
Business managers often need to manually export data from their sales systems into Excel, write complex VLOOKUPs to match product IDs to prices, and spend hours building charts for monthly revenue meetings.

## 💡 The Solution
This project acts as an automated Data Analyst. It safely queries the SQL database, computes the financial metrics, and outputs highly polished CSV reports and PNG charts instantly. 

### Core Features:
- **Relational SQL Queries:** Uses `sqlite3` to perform `JOIN` operations across relational tables (Sales and Products).
- **Date Filtering:** Uses SQL date functions to dynamically isolate sales from the trailing 30 days.
- **Pandas Integration:** Directly pipes SQL output into a Pandas DataFrame for final structuring.
- **Automated Visualization:** Uses `Matplotlib` to render and save a professional bar chart of revenue distribution.

## 🚀 How to Run
1. Run `python database_setup.py` to initialize the database and inject dummy relational data.
2. Run `python report_gen.py` to execute the SQL query, generate the CSV, and create the visual charts in the `/reports` folder.