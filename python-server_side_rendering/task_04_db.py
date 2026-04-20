import sqlite3
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

# --- 1. MƏLUMATLARI OXUMAQ ÜÇÜN FUNKSİYALAR ---

def read_json():
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except Exception:
        return []

def read_csv():
    products = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Bəzi testlər ID-nin int olmasını gözləyə bilər
                products.append(row)
        return products
    except Exception:
        return []

def read_sql():
    products = []
    try:
        conn = sqlite3.connect('products.db')
        # Bu sətir sütun adlarını açar (key) kimi istifadə etməyə imkan verir
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

# --- 2. ƏSAS MARŞRUT (ROUTE) ---

@app.route('/products')
def display_products():
    # URL-dən source və id parametrlərini götürürük
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    # Mənbə yoxlanışı
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")
    
    # Mənbəyə uyğun datanı oxu
    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    elif source == 'sql':
        data = read_sql()
        if data is None:
            return render_template('product_display.html', error="Database error")

    # ID filtrləmə məntiqi
    if product_id:
        # Siyahıdakı hər bir elementi yoxla və yalnız ID-si uyğun olanı saxla
        data = [p for p in data if str(p.get('id')) == str(product_id)]
        
        # Əgər axtarılan ID tapılmasa
        if not data:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
