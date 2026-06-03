import pandas as pd
import sqlite3

df = pd.read_csv('data/Sample - Superstore.csv', encoding = 'latin1')

df = df.drop_duplicates()

for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].str.strip()

new_header = list(df.columns)

for i in range(len(new_header)):
    new_header[i] = new_header[i].lower()
    new_header[i] = new_header[i].strip()
    new_header[i] = new_header[i].replace(' ','_').replace('-','_')

df.columns = new_header

df['order_date'] = pd.to_datetime(df['order_date'])
df['ship_date'] = pd.to_datetime(df['ship_date'])

conn = sqlite3.connect('business.db')

df.to_sql('data', conn, if_exists='replace', index=False)

q1 = pd.read_sql_query("""
    SELECT product_id,
        product_name,
        category,
        ROUND(SUM(sales)/SUM(quantity), 2) AS price
        FROM data
        GROUP BY product_id
""", conn)

q2 = pd.read_sql_query("""
    SELECT order_id,
        product_id,
        quantity,
        order_date
        FROM data      
""", conn)

q1.to_sql('products', conn, if_exists='replace', index=False)
q2.to_sql('sales', conn, if_exists='replace', index=False)

print("Created products table with rows:",pd.read_sql_query("SELECT count(*) FROM products", conn))
print("Create sales table with rows:",pd.read_sql_query("SELECT count(*) FROM sales", conn))

conn.close()
