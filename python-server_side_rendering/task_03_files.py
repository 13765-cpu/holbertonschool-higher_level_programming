import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

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
                # ID və Price-ı rəqəmə çevirmək yaxşı təcrübədir
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except Exception:
        return []

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    # 1. Source yoxlanılması
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")
    
    # 2. Dataya uyğun faylı oxu
    if source == 'json':
        data = read_json()
    else:
        data = read_csv()
    
    # 3. ID filtrasiyası
    if product_id:
        try:
            target_id = int(product_id)
            # Siyahıda həmin ID-ni axtar
            filtered_data = [p for p in data if p['id'] == target_id]
            if not filtered_data:
                return render_template('product_display.html', error="Product not found")
            data = filtered_data
        except ValueError:
            return render_template('product_display.html', error="Invalid ID format")

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
