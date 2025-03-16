import requests
from flask import Flask, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, JWTManager

app = Flask(__name__)

# 🔑 Secret key for JWT
app.config["JWT_SECRET_KEY"] = "supersecretkey"  
jwt = JWTManager(app)

# Dummy users
USERS = {"testuser": "password123"}

# Dummy data til kvitteringer
RECEIPTS = [
    {"id": 1, "store": "Netto", "items": ["Mælk", "Brød", "Smør"], "total": 55.00},
    {"id": 2, "store": "Føtex", "items": ["Kylling", "Rugbrød"], "total": 75.50}
]

# Dummy Netto API (skal senere erstattes med rigtig API-kald)
NETTO_OFFERS = [
    {"item": "Æg", "discount": "10%", "price": 15.00},
    {"item": "Ost", "discount": "20%", "price": 25.00},
    {"item": "Kartofler", "discount": "15%", "price": 10.00}
]

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
    return jsonify({"receipts": RECEIPTS})

@app.route('/fetch_netto_offers', methods=['GET'])
def get_netto_offers():
    return jsonify({"offers": NETTO_OFFERS})

@app.route('/generate_meal_plan', methods=['GET'])
@jwt_required()
def generate_meal_plan():
    # Hent brugernes kvitteringer
    user_receipts = RECEIPTS  # Simuleret

    # Hent Netto-tilbud
    netto_offers = NETTO_OFFERS  # Simuleret (kan erstattes med API-kald)

    # Forslag til madplan baseret på kvitteringer + tilbud
    meal_plan = [
        {"day": "Mandag", "meal": "Rugbrød med ost", "ingredients": ["Rugbrød", "Ost"]},
        {"day": "Tirsdag", "meal": "Omelet med kartofler", "ingredients": ["Æg", "Kartofler"]},
        {"day": "Onsdag", "meal": "Kylling med brød", "ingredients": ["Kylling", "Brød"]}
    ]

    return jsonify({"meal_plan": meal_plan})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
