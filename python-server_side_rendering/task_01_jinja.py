from flask import Flask, render_template

app = Flask(__name__)

# Ana səhifə marşrutu
@app.route('/')
def home():
    return render_template('index.html')

# About (Haqqımızda) səhifəsi marşrutu
@app.route('/about')
def about():
    return render_template('about.html')

# Contact (Əlaqə) səhifəsi marşrutu
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    # Tapşırıq portun 5000 olmasını tələb edir
    app.run(debug=True, port=5000)
