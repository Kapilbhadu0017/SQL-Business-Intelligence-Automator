# 📈 SQL Business Intelligence Automator

An automated data engineering pipeline that loads real retail sales data into a relational SQLite database, executes complex JOIN queries, and instantly generates financial reports and visualizations — replacing hours of manual Excel work.

---

## ⚠️ The Business Problem

Business managers often need to manually export data from their sales systems into Excel, write complex VLOOKUPs to match product IDs to prices, and spend hours building charts for monthly revenue meetings. This process is slow, error-prone, and has to be repeated every single month.

## 💡 The Solution

This pipeline acts as an automated Data Analyst. It structures raw sales data into a normalized relational database, runs SQL JOIN queries across tables, and outputs polished CSV reports and PNG charts instantly — in under 30 seconds.

---

## Pipeline Overview

```
Raw CSV  →  data_loader.py  →  SQLite DB (products + sales tables)  →  report_gen.py  →  CSV Report + Chart
```

**Run the full pipeline in 2 commands:**

```bash
python data_loader.py
python report_gen.py
```

---

## What Each Script Does

### `data_loader.py`
- Loads raw Superstore CSV with encoding handling
- Cleans column names to `snake_case`
- Converts date columns to proper datetime format
- Builds two normalized relational tables in SQLite:
  - **`products`** — unique products with `product_id`, `product_name`, `category`, and calculated unit `price`
  - **`sales`** — transaction records with `order_id`, `product_id`, `quantity`, and `order_date`

### `report_gen.py`
- Connects to `business.db`
- Executes a JOIN query across `products` and `sales` tables
- Filters to the most recent year of data (2017)
- Returns the **Top 10 products by total revenue**
- Exports results to CSV and generates a horizontal bar chart

---

## Output

### Top 10 Products by Revenue (2017)

Canon imageCLASS 2200 Advanced Copier dominates at $33,879 — nearly 3x the revenue of the second-ranked product, highlighting a strong concentration of revenue in high-ticket office equipment.

![Revenue Chart](reports/revenue_chart.png)

---

## Key Features

- **Relational SQL Design:** Two normalized tables with a proper foreign key relationship between `sales` and `products`
- **JOIN Queries:** Revenue is computed by joining sales quantities with product prices across tables — no flat-file lookups
- **Date Filtering:** SQL `WHERE` clause dynamically isolates sales from a specific time period
- **Pandas Integration:** `pd.read_sql_query()` pipes SQL output directly into a DataFrame for export
- **Automated Visualization:** Matplotlib renders and saves a professional horizontal bar chart with revenue labels

---

## Project Structure

```
SQL-Business-Intelligence-Automator/
│
├── data/
│   └── Sample - Superstore.csv    ← raw input data
│
├── reports/
│   ├── monthly_revenue_report.csv ← SQL query output
│   └── revenue_chart.png          ← automated visualization
│
├── data_loader.py                 ← builds the SQLite database
├── report_gen.py                  ← runs queries and generates reports
├── requirements.txt
└── README.md
```

---

## Setup & Usage

```bash
# Clone the repo
git clone https://github.com/Kapilbhadu0017/SQL-Business-Intelligence-Automator.git
cd SQL-Business-Intelligence-Automator

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Add the Superstore dataset to data/
# Download from: https://www.kaggle.com/datasets/vivek468/superstore-dataset-final

# Run the pipeline
python data_loader.py
python report_gen.py
```

---

## Dataset

[Superstore Sales Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final) — 9,994 retail orders across US regions (2014–2017), sourced from Kaggle. Place the CSV at `data/Sample - Superstore.csv` before running.

---

*Part of my data automation portfolio. Built with Python, SQL, and zero Excel.*