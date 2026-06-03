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
        FROM sales s
        JOIN products p ON s.product_id = p.product_id
        WHERE s.order_date >= '2017-01-01'
        GROUP BY p.product_name
        ORDER BY total_revenue DESC
        LIMIT 10;
    '''

    df = pd.read_sql_query(sql_query, conn)
    conn.close()

    if df.empty:
        print("No Sales Data Found.")
        return

    csv_path = 'reports/monthly_revenue_report.csv'
    df.to_csv(csv_path, index=False)
    print(f"CSV Report Generated : {csv_path}")

    plt.figure(figsize=(10,6))
    bars = plt.barh(df['product_name'].iloc[::-1], df['total_revenue'].iloc[::-1], color = '#2ca02c')

    plt.title('Total Revenue by Product (2017)', fontsize = 16)
    plt.xlabel('Revenue ($)', fontsize = 12)
    plt.ylabel('Product', fontsize = 12)
    plt.xticks(rotation = 45, ha='right')
    plt.tight_layout()
    for bar in bars:
        xval = bar.get_width()
        plt.text(xval + 200, bar.get_y() + bar.get_height()/2, f"${xval:,.2f}", va="center", ha="left")
    
    image_path = 'reports/revenue_chart.png'
    plt.savefig(image_path, bbox_inches='tight')
    print(f"Visual Chart Generated: {image_path}")

if __name__ == '__main__':
    generate_report()