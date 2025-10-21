from __future__ import annotations

from flask import Flask, jsonify, request


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/")
    def home():
        return jsonify({"message": "Welcome to the Flask App"}), 200

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"}), 200

    @app.post("/data")
    def data():
        # Accept JSON or form-encoded input
        payload = request.get_json(silent=True)
        if payload is None:
            # Fallback to form data
            payload = request.form.to_dict() or None
        if payload is None:
            return jsonify({"error": "No data provided"}), 400
        # Echo back with a simple transformation
        return jsonify({"received": payload, "count": len(payload)}), 200

    return app


if __name__ == "__main__":
    app = create_app()
    # Bind to port from env if present (e.g., Render/Heroku), else default 5000
    import os

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
