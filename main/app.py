from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Home route - render frontend page
@app.route('/')
def home():
    return render_template('index.html')

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
