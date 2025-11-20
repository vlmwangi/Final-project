import os
from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo
from datetime import datetime, timedelta
from dotenv import load_dotenv
from functools import wraps
import jwt
from bson import ObjectId

load_dotenv()

app = Flask(__name__, static_folder="static", template_folder="templates")

#Config
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret")

mongo = PyMongo(app)  # db access: mongo.db

# Helper: JWT 
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"error": "Token missing"}), 401
        try:
            jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
        except Exception as e:
            return jsonify({"error": "Invalid token"}), 401
        return f(*args, **kwargs)
    return decorated

# Public Routes 
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

        report = {
            "name": data.get("name", "").strip(),
            "location": location,
            "incident": incident,
            "contact": data.get("contact", "").strip(),
            "urgency_level": data.get("urgency_level"),
            "support_needed": data.get("supportOptions", []),
            "anonymous": data.get("anonymous", False),
            "description": data.get("description", "").strip(),
            "created_at": datetime.utcnow()
        }

        result = mongo.db.reports.insert_one(report)
        return jsonify({"message": "Report received", "id": str(result.inserted_id)}), 201

    except Exception as e:
        app.logger.error(f"Error saving report: {e}")
        return jsonify({"error": "Server error"}), 500

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

# Admin Authentication 
@app.route("/api/admin/register", methods=["POST"])
def register_admin():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    if mongo.db.users.find_one({"username": username}):
        return jsonify({"error": "User already exists"}), 400

    mongo.db.users.insert_one({"username": username, "password": password})
    return jsonify({"message": "Admin registered"}), 201

@app.route("/api/admin/login", methods=["POST"])
def admin_login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    user = mongo.db.users.find_one({"username": username})
    if not user or user["password"] != password:
        return jsonify({"error": "Invalid credentials"}), 401

    token = jwt.encode({
        "username": username,
        "exp": datetime.utcnow() + timedelta(hours=2)
    }, app.config["SECRET_KEY"], algorithm="HS256")

    return jsonify({"token": token})

# Admin CRUD 
@app.route("/api/reports", methods=["GET"])
@token_required
def get_reports():
    reports = list(mongo.db.reports.find())
    for r in reports:
        r["_id"] = str(r["_id"])
    return jsonify(reports), 200

@app.route("/api/report/<report_id>", methods=["PUT"])
@token_required
def update_report(report_id):
    data = request.get_json()
    update_data = {}
    if "resolved" in data:
        update_data["resolved"] = data["resolved"]
    if "notes" in data:
        update_data["notes"] = data["notes"]

    mongo.db.reports.update_one({"_id": ObjectId(report_id)}, {"$set": update_data})
    return jsonify({"message": "Report updated"}), 200

@app.route("/api/report/<report_id>", methods=["DELETE"])
@token_required
def delete_report(report_id):
    mongo.db.reports.delete_one({"_id": ObjectId(report_id)})
    return jsonify({"message": "Report deleted"}), 200

# Admin Dashboard 
@app.route("/admin")
def admin_dashboard():
    return render_template("admin.html")  # Admin HTML will fetch /api/reports with token

# Run 
if __name__ == "__main__":
    app.run(debug=True)
