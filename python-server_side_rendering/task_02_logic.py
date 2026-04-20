import json
from flask import Flask, render_template

app = Flask(__name__)

# ... digər route-lar (home, about, contact) ...

@app.route('/items')
def show_items():
    # JSON faylını oxuyuruq
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            items_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []

    # Məlumatı HTML şablonuna ötürürük
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
