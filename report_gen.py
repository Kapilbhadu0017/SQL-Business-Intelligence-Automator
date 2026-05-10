import sqlite3
import pandas as pd 
import matplotlib.pyplot as plt 
import os

def generate_report():
    os.makedirs('reports', exist_ok=True)
    conn = sqlite3.connect('business.db')
    
    # Join-SQL Query
    sql_query = '''
        SELECT 
            p.product_name,
            SUM(s.quantity) as total_units_sold,
            SUM(s.quantity * p.price) as total_revenue
        FROM Sales s
        JOIN Products p ON s.product_id = p.product_id
        WHERE s.sale_date >= date('now', '-30 days')
        GROUP BY p.product_name
        ORDER BY total_revenue DESC;
    '''

    df = pd.read_sql_query(sql_query, conn)

    if df.empty:
        print("No Sales Data Found for Last 30 Days.")
        return

    csv_path = 'reports/monthly_revenue_report.csv'
    df.to_csv(csv_path, index=False)
    print(f"CSV Report Generated : {csv_path}")

    plt.figure(figsize=(10,6))
    bars = plt.bar(df['product_name'], df['total_revenue'], color = '#2ca02c')

    plt.title('Total Revenue by Product (Last 30 Days)', fontsize = 16)
    plt.xlabel('Product', fontsize = 12)
    plt.ylabel('Revenue ($)', fontsize = 12)
    plt.xticks(rotation = 45, ha='right')

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval+ 100, f"${yval:,.2f}", ha="center", va="bottom")
    
    plt.tight_layout()
    image_path = 'reports/revenue_chart.png'
    plt.savefig(image_path)
    print(f"Visual Chart Generated: {image_path}")

if __name__ == '__main__':
    generate_report()