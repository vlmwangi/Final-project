import os
from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS #delete this line
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)  # allow calls from frontend (adjust origin in production)

app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret")

mongo = PyMongo(app)  # db access: mongo.db

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/api/report", methods=["POST"])
def create_report():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON provided"}), 400

        # Basic validation
        location = data.get("location", "").strip()
        incident = data.get("incident", "").strip()

        if not location or not incident:
            return jsonify({"error": "Missing required fields"}), 400

        # Build report document
        report = {
            "name": data.get("name", "").strip(),
            "location": location,
            "incident": incident,
            "contact": data.get("contact", "").strip(),
            "urgency_level": data.get("urgency_level"),
            "support_needed": data.get("support_needed", []),
            "anonymous": data.get("anonymous", False),
            "created_at": datetime.utcnow()
        }

        result = mongo.db.reports.insert_one(report)
        return jsonify({"message": "Report received", "id": str(result.inserted_id)}), 201

    except Exception as e:
        app.logger.error(f"Error saving report: {e}")
        return jsonify({"error": "Server error"}), 500

# Health check
@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(debug=True)
