# SafeConnect
---

## Overview
**SafeConnect** is a secure, accessible platform designed to help women and girls report incidents of gender-based violence (GBV), access emergency support, and connect with verified resources.  
It prioritizes **privacy, safety, and confidentiality**, enabling survivors or witnesses of GBV to report incidents safely, as well as to receive timely information/referral to rescue organisations such as Usikimye.

**Live deployment:** https://safeconnect-cxy3.onrender.com/

**Product Pitch Deck Link:** https://gamma.app/docs/SafeConnect-ryaqaonwybcn6v3

## Purpose & Impact
SafeConnect aims to:
- Provide a safe channel for GBV reporting.
- Offer immediate access to helplines, safe houses, and support centers.
- Facilitate connections with legal aid, counseling, and rescue organizations.
- Support data-driven insights for GBV response (through admin dashboards).

This project aligns with **SDG 5 & 16**: promoting gender equality, ending violence, and strengthening institutions to ensure justice.

## Scope
- **Frontend & Backend Application:** Submit reports safely.
- **Information & Resources:** Display information, statistics, and resources related to gender-based violence such as helplines and rescue centres.
- **Referral System:** The app connects survivors with legal aid, counseling, and rescue organizations. Reports and contacts are routed securely the relevant organsations.
- **Not an emergency service:** SafeConnect provides referral and reporting tools, not direct rescue operations.

---

## Key Features
### **1. Incident Reporting**
- Confidential GBV reporting form  
- Supports multiple incident categories  
- Allows selection of required support services  
- Secure POST request to backend

### **2. Emergency Resources**
- Quick access to hotline numbers (999, 1195)  
- Support center directory  
- Help tabs with safety tips

### **3. Modern Frontend**
- Responsive and mobile-first design
- Built with Tailwind CSS, Bootstrap, and JavaScript
- Smooth UI interactions for enhanced user experience

### **4. Backend API (Flask)**
- RESTful API endpoints for report submission
- CRUD operations for admin responders:
    a) GET /api/reports → view all reports
    b) PUT /api/report/<id> → update report (resolved or notes)
    c) DELETE /api/report/<id> → delete a report
- JWT-based admin authentication
- Simple admin dashboard that can fetch submissions via JS + token.
- JSON-based structured data storage
- CORS enabled for frontend-backend communication
- Logs and stores reports for partner organisation access

---

## Tech Stack
**Frontend:**  
- HTML5  
- Tailwind CSS  
- Bootstrap  
- JavaScript  

**Backend:**  
- Python Flask  
- REST API Endpoints
- CORS Support
- JSON storage (expandable)

**Tools:**  
- Git & GitHub  
- Fetch API for frontend-backend integration
- Render for deployment

---
## Project Structure
SafeConnect/
│── app.py                # Backend Flask application
│── index.html            # Main frontend page
│── static/
│    ├── css/             # Stylesheets
│    └── js/              # JavaScript files
│── reports/              # Auto-created directory to store submissions
│── requirements.txt      # Python dependencies
│── package.json          # Node package info (if using JS packages)
│── package-lock.json
│── README.md

## Running the Project Locally
### 1. Clone Repository
```bash
git clone https://github.com/vlmwangi/Final-project.git
cd SafeConnect
```

### 2. Backend Setup
Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the Flask server
```bash
python app.py
```

Backend runs at: http://127.0.0.1:5000
Frontend: Open index.html in browser, or visit live site: https://safeconnect-cxy3.onrender.com/


## Future Enhancements
- SQL/NoSQL database integration
- Geolocation-based help center lookup
- Real emergency alert system
