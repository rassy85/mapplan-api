from flask import Flask, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, JWTManager

app = Flask(__name__)

# 🔑 Secret key for JWT
app.config["JWT_SECRET_KEY"] = "supersecretkey"  
jwt = JWTManager(app)

# Dummy users (du kan erstatte dette med en database senere)
USERS = {"testuser": "password123"}

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in USERS and USERS[username] == password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)

    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/fetch_receipts', methods=['GET'])
@jwt_required()
def get_receipts():
    receipts = [
        {"id": 1, "store": "Netto", "items": ["Mælk", "Brød", "Smør"], "total": 55.00},
        {"id": 2, "store": "Føtex", "items": ["Kylling", "Rugbrød"], "total": 75.50}
    ]
    return jsonify({"receipts": receipts})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
