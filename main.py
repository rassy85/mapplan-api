from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Serveren kører! Prøv /fetch_receipts"

@app.route('/fetch_receipts', methods=['GET'])
def get_receipts():
    receipts = [
        {"id": 1, "store": "Netto", "items": ["Mælk", "Brød", "Smør"], "total": 55.00},
        {"id": 2, "store": "Føtex", "items": ["Kylling", "Rugbrød"], "total": 75.50}
    ]
    return jsonify({"receipts": receipts})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
