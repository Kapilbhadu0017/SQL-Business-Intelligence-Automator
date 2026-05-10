import sqlite3
import random 
from datetime import datetime, timedelta

def setup_database():
    # connect to SQLite
    conn = sqlite3.connect('business.db')
    cursor = conn.cursor()

    # clear existing data if running script multiple times ( test data generation )
    cursor.execute('DROP TABLE IF EXISTS Sales')
    cursor.execute('DROP TABLE IF EXISTS Products')

    # create the products table
    cursor.execute('''
        CREATE TABLE Products(
                   product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   product_name TEXT NOT NULL,
                   price REAL NOT NULL
                   )
    ''')

    # create a sales table ( with a foreign key linking to products )
    cursor.execute('''
        CREATE TABLE Sales(
                   sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   product_id INTEGER,
                   quantity INTEGER,
                   sale_date DATE,
                   FOREIGN KEY(product_id) REFERENCES Products(product_id)
                   )
    ''')

    # inserting dummy products 
    products = [
        ('Laptop', 1200.00),
        ('Wireless Mouse', 45.00),
        ('Mechanical Keyboard', 150.00),
        ('4K Monitor', 300.00),
        ('USB-C Hub', 25.00)
    ]
    
    cursor.executemany("INSERT INTO Products (product_name, price) VALUES (?,?)", products)

    # generating random sales
    sales_data = []
    today = datetime.now()

    for _ in range(100):
        p_id = random.randint(1,5)
        qty = random.randint(1,4)
        days_ago = random.randint(0,45)
        s_date = (today - timedelta(days=days_ago)).strftime('%Y-%m-%d')

        sales_data.append((p_id, qty, s_date))
    
    cursor.executemany("INSERT INTO Sales (product_id, quantity, sale_date) VALUES (?,?,?)", sales_data)

    # commit and close
    conn.commit()
    conn.close()
    print("Database 'business.db' created successfully with dummy data")

if __name__ == '__main__':
    setup_database()
