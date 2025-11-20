# SafeConnect
---

## Overview
**SafeConnect** is a secure, accessible platform designed to help women and girls report incidents of gender-based violence, access emergency support, and connect with verified resources.  
It prioritizes **privacy, safety, confidentiality, and fast response**, enabling survivors or witnesses of GBV to report incidents safely, as well as to receive information/referral to rescue organisations such as Usikimye.

## Scope
- Build a frontend + backend app where someone can submit a safe/anonymous report.
- Display information, statistics, and resources related to gender-based violence such as helplines and rescue centres
- The app connects survivors with legal aid, counseling, and rescue organizations .
- GBV reports and contact information are routed to Usikimye via a simple database that Usikimye can query.
- This project does run the rescue operations, instead it provides a tool for referral + reporting.
- This aligns with SDG 5 & 16 (ending violence, strengthening institutions, enabling justice) and supports Usikimye’s work.

## Task
- Basic user interface for submission.
- Backend API to store submissions.
- Simple admin dashboard to view submissions or export them.
- Integrate a directory of resources (safe houses, helplines).
- Deploy on a basic host.
- Future additions: geolocation, anonymous mode, SMS alert integration.

---

## Key Features

### **Incident Reporting**
- Confidential GBV reporting form  
- Supports multiple incident categories  
- Allows selection of required support services  
- Secure POST request to backend

### **Emergency Resources**
- Quick access to hotline numbers (999, 1195)  
- Support center directory  
- Help tabs with safety tips

### **Modern Frontend**
- Tailwind CSS  
- Bootstrap  
- Responsive and mobile-first  
- JavaScript-based UI interactions

### **Backend API (Flask)**
- POST endpoint `/api/report`  
- Structured JSON data collection  
- CORS enabled  
- Logs and stores reports (directory-based storage for now)

---

## 🛠 Tech Stack

**Frontend:**  
- HTML5  
- Tailwind CSS  
- Bootstrap  
- Vanilla JavaScript  

**Backend:**  
- Python Flask  
- REST API  
- CORS  
- JSON storage (expandable)

**Tools:**  
- Git & GitHub  
- Fetch API  

---

## Running the Project Locally

### 1. Clone Repository
```bash
git clone https://github.com/vlmwangi/Final-project
cd SafeConnect
