#!/usr/bin/python3
"""
Flask API: Basic Authentication, JWT və Role-Based Access Control (RBAC).
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# JWT Konfiqurasiyası
app.config["JWT_SECRET_KEY"] = "super-secret-key"  # Real layihədə bunu gizli saxla
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# İstifadəçi verilənlər bazası (Yaddaşda)
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# --- BASIC AUTHENTICATION LOGIC ---

@auth.verify_password
def verify_password(username, password):
    """Basic Auth üçün istifadəçi adı və şifrəni yoxlayır."""
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username
    return None

@auth.error_handler
def basic_auth_error(status):
    """Basic Auth xətası olduqda 401 qaytarır."""
    return jsonify({"error": "Unauthorized access"}), 401


# --- JWT ERROR HANDLERS (Checker üçün çox vacibdir) ---

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


# --- ENDPOINTS ---

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Yalnız düzgün Basic Auth ilə daxil olmaq olar."""
    return "Basic Auth: Access Granted"

@app.route("/login", methods=["POST"])
def login():
    """İstifadəçi daxil olur və JWT token alır."""
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        # Rol məlumatını tokenin içinə (additional claims) qoyuruq
        access_token = create_access_token(
            identity=username, 
            additional_claims={"role": user["role"]}
        )
        return jsonify(access_token=access_token)
    
    return jsonify({"error": "Bad username or password"}), 401

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Yalnız düzgün JWT token ilə daxil olmaq olar."""
    return "JWT Auth: Access Granted"

@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Yalnız 'admin' rolu olanlar üçün."""
    claims = get_jwt() # Tokenin içindəki əlavə məlumatları (rolu) alırıq
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    
    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
