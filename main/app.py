from flask import Flask, request, jsonify

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Welcome to the Flask Lab Project Backend!"

# Health check route
@app.route('/health')
def health():
    return "OK"

# Simple POST route
@app.route('/data', methods=['POST'])
def data():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON received"}), 400
    return jsonify({
        "message": "Data received successfully",
        "data": data
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
