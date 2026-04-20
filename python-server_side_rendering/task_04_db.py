import sqlite3
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

# SQL-dən məlumatları oxumaq üçün funksiya
def read_sql():
    products = []
    try:
        conn = sqlite3.connect('products.db')
        # Bu sətir nəticəni lüğət (dict) formatında almağa kömək edir
        conn.row_factory = sqlite3.Row 
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Products')
        rows = cursor.fetchall()
        for row in rows:
            products.append(dict(row))
        conn.close()
        return products
    except sqlite3.Error:
        return None # Baza xətası halında

@app.route('/products')
def display_products():
    source = request.args.get('source')
    
    # 1. Mənbə yoxlanışı
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")
    
    # 2. Mənbəyə görə datanı oxu
    if source == 'json':
        # Əvvəlki taskdakı read_json funksiyanı bura əlavə et
        data = read_json() 
    elif source == 'csv':
        # Əvvəlki taskdakı read_csv funksiyanı bura əlavə et
        data = read_csv()
    elif source == 'sql':
        data = read_sql()
        if data is None:
            return render_template('product_display.html', error="Database error")

    return render_template('product_display.html', products=data)
