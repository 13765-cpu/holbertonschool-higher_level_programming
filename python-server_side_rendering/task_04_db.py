import sqlite3
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

# --- OXUMA FUNKSİYALARI ---
def read_json():
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except: return []

def read_csv():
    products = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append(row)
        return products
    except: return []

def read_sql():
    products = []
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row 
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Products')
        rows = cursor.fetchall()
        for row in rows:
            products.append(dict(row))
        conn.close()
        return products
    except sqlite3.Error:
        return None

# --- ROUTE ---
@app.route('/products')
def display_products():
    source = request.args.get('source')
    
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")
    
    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    elif source == 'sql':
        data = read_sql()
        if data is None:
            return render_template('product_display.html', error="Database error")

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
