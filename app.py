from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes

@app.route('/api/health')
def health():
    return jsonify({"status": "OK", "message": "Backend is running"})

@app.route('/api/bookings/user/<user_id>')
def get_bookings(user_id):
    return jsonify({
        "user": user_id,
        "bookings": [
            {"id": 1, "date": "2026-06-20", "status": "Booked"},
            {"id": 2, "date": "2026-06-25", "status": "Booked"}
        ]
    })

if __name__ == '__main__':
    # Only run the Flask dev server when executed directly.
    # This prevents accidental startup if the module is imported.
    app.run(port=5006, debug=True)
