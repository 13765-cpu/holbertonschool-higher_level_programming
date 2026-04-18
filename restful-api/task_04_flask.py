from flask import Flask, jsonify, request

app = Flask(__name__)

# Yaddaşda saxlanılan istifadəçilər
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def get_data():
    # Səndən yalnız istifadəçi adlarını (keys) siyahı şəklində qaytarmaq istənilir
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=['POST'])
def add_user():
    # 1. JSON-un düzgünlüyünü yoxla
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    
    # 2. Username-in olub-olmadığını yoxla
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    # 3. Dublikat yoxlaması
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    
    # 4. Əlavə et və 201 (Created) qaytar
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
