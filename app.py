# filename: app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulate knowledge base for demo purposes
mobile_prices = {
    "Samsung Galaxy S21": "$799",
    "iPhone 14": "$899",
    "Xiaomi Redmi Note 12": "$199"
}

@app.route('/ask_qwer', methods=['POST'])
def ask_qwer():
    data = request.get_json()
    mobile_name = data.get('mobile_name')

    # Search in our mini "knowledge"
    answer = mobile_prices.get(mobile_name, "Sorry, I don't know the price of that mobile.")
    
    return jsonify({
        "answer": answer
    })

# Render needs this for health check
@app.route('/')
def home():
    return "API is running!"
