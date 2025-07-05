from flask import Flask, jsonify
from datetime import datetime
import random

app = Flask(__name__)

# Dummy airline data
airlines = [
    {"id": 1, "name": "Air India", "code": "AI"},
    {"id": 2, "name": "Emirates", "code": "EK"},
    {"id": 3, "name": "Qatar Airways", "code": "QR"}
]

# Generate dummy demand data dynamically
def generate_demand():
    routes = ["SYD-MEL", "SYD-BNE", "MEL-PER"]
    demand = []
    for i, airline in enumerate(airlines):
        demand.append({
            "airline": airline["name"],
            "flights_today": random.randint(50, 150),
            "tickets_sold": random.randint(1000, 5000),
            "avg_price": random.randint(100, 500),
            "route": routes[i % len(routes)],
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    return demand

@app.route('/api/demand', methods=['GET'])
def get_demand():
    data = generate_demand()
    return jsonify({"demand": data})

if __name__ == '__main__':
    app.run(debug=True)
