@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')  # URL-dən id-ni götürürük
    
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

    # --- FİLTRLƏMƏ HİSSƏSİ BURADIR ---
    if product_id:
        # Siyahının içindən yalnız həmin ID-yə uyğun olanı tapırıq
        # ID-ləri müqayisə edərkən hər ikisini string-ə (str) çevirmək daha təhlükəsizdir
        data = [p for p in data if str(p.get('id')) == str(product_id)]
        
        if not data:
            return render_template('product_display.html', error="Product not found")
    # ---------------------------------

    return render_template('product_display.html', products=data)
