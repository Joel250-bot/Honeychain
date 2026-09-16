# HoneyChain – Smart Beekeeping & Honey Traceability System

HoneyChain is a full-stack, real-time web application and IoT simulation prototype for smart beekeeping management, AI-driven hive anomaly detection, Random Forest honey yield prediction, cryptographic blockchain traceability, and QR-code-based consumer product verification.

---

## 🌟 Project Highlights

1. **Realistic IoT Sensor Simulator**: Generates continuous real-time telemetry for temperature (°C), humidity (%), hive weight (kg), bee activity (%), CO2, sound, and battery levels across multiple beehives.
2. **Interactive Anomaly Control Panel**: Allows on-demand injection of realistic hive environmental stress scenarios (Overheating, Cold Drop, Excessive Dampness, Swarming Weight Loss, Low Activity, Multiple Anomalies) and reset to normal.
3. **AI Anomaly & Yield Intelligence**:
   - **Isolation Forest Classifier**: Detects environmental anomalies in real-time, calculates anomaly confidence scores (0–100%), and generates diagnostic alerts.
   - **Random Forest Regressor**: Predicts expected honey yield harvest (in kg) based on environmental telemetry and day progression.
4. **Private SHA-256 Blockchain Ledger**: Cryptographically links all beehive monitoring and honey batch events into immutable blocks with parent hash validation and real-time audit verification ("Blockchain verified ✓").
5. **Honey Batch Management & Base64 QR Generation**: Mints batch codes (`HONEY-2026-0001`), packages quality testing reports, generates scanned QR codes, and appends events to the blockchain ledger.
6. **Consumer Verification Portal**: Dedicated public consumer verification view (`/verify/:batchCode`) showing origin apiary, harvest details, quality pass certificate, supply chain timeline, and cryptographic blockchain integrity status.

---

## 🏗️ Recommended Technology Stack

- **Frontend**: React 18, Vite, Tailwind CSS, Recharts, Lucide Icons, WebSockets API
- **Backend**: Python 3.14+, FastAPI, Uvicorn, SQLAlchemy ORM, Pydantic v2, Python-Dotenv, QRCode (Pillow)
- **Database**: PostgreSQL (Supported via `DATABASE_URL`) / SQLite (`honeychain.db` out-of-the-box fallback)
- **Machine Learning**: Scikit-Learn (Isolation Forest & Random Forest Regressor), Pandas, NumPy

---

## 📁 Project Folder Structure

```
Honeyai/
├── backend/
│   ├── app/
│   │   ├── ai/
│   │   │   └── model_service.py      # Isolation Forest & Random Forest Regressor
│   │   ├── blockchain/
│   │   │   └── ledger.py             # SHA-256 Block Hashing & Verification
│   │   ├── models/
│   │   │   └── models.py             # SQLAlchemy Database Models
│   │   ├── routers/
│   │   │   └── api_router.py         # REST API Endpoints
│   │   ├── schemas/
│   │   │   └── schemas.py            # Pydantic Schemas
│   │   ├── services/
│   │   │   └── qr_service.py         # Base64 QR Code Generator
│   │   ├── simulator/
│   │   │   └── sensor_simulator.py   # IoT Telemetry Simulator Engine
│   │   ├── database.py               # Database Engine & Session
│   │   └── main.py                   # FastAPI Application & WebSockets
│   ├── .env.example
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Header.jsx            # Live Telemetry & Alert Header
│   │   │   └── Sidebar.jsx           # Application Navigation
│   │   ├── hooks/
│   │   │   └── useWebSocket.js       # Live IoT Stream Hook
│   │   ├── pages/
│   │   │   ├── Dashboard.jsx         # Main Telemetry & Fleet Overview
│   │   │   ├── HiveMonitoring.jsx    # Fleet Telemetry & Scenario Triggers
│   │   │   ├── HiveDetails.jsx       # Single Hive Deep Dive & Charts
│   │   │   ├── AIAnalytics.jsx       # AI Model Metrics & Fleet Summary
│   │   │   ├── HoneyBatches.jsx      # Batch Creator & QR Code Generator
│   │   │   ├── Traceability.jsx      # Hive-to-Consumer Supply Chain Timeline
│   │   │   ├── BlockchainExplorer.jsx# Ledger Block Inspector & Auditor
│   │   │   ├── ConsumerVerification.jsx # Public Consumer Provenance Page
│   │   │   └── SimulationControls.jsx # Anomaly Control Panel
│   │   ├── services/
│   │   │   └── api.js                # Frontend REST API Client
│   │   ├── App.jsx                   # Main React Router Component
│   │   ├── index.css                 # Tailwind CSS Styles
│   │   └── main.jsx                  # React DOM Entrypoint
│   ├── package.json
│   ├── tailwind.config.js
│   └── vite.config.js
│
├── data/                             # Synthetic datasets & exports
├── models/                           # Trained scikit-learn model pickles
├── scripts/
│   ├── run_backend.py                # Server launcher script
│   └── test_workflow.py             # End-to-End system verification test
└── README.md
```

---

## ⚡ Quick Start & Installation

### 1. Backend Setup

```bash
# Navigate to workspace root
cd Honeyai

# Install Python requirements
pip install -r backend/requirements.txt

# Run End-to-End Workflow Verification Test
python scripts/test_workflow.py

# Start FastAPI Backend Server (Runs on http://localhost:8000)
python scripts/run_backend.py
```

### 2. Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install Node dependencies
npm install

# Start Vite Development Server (Runs on http://localhost:5173)
npm run dev
```

---

## 🎯 Demonstration Workflow (College Project Presentation)

1. **Open Dashboard** (`http://localhost:5173`):
   - View 5 active beehives, real-time temperature/humidity/weight/activity streaming charts, total yield predictions, and live WebSocket connection indicator.
2. **Inspect Beehive Telemetry**:
   - Navigate to **Hive Monitoring** or click `HIVE-003` to open **Hive Details**. View live gauges and historical trends.
3. **Trigger Anomaly Scenario**:
   - Go to **Simulation Controls** (or inline button on Hive card). Select `HIVE-003` and click **"High Temperature Spike"** or **"Sudden Weight Drop"**.
4. **Observe Real-time AI Anomaly Detection**:
   - The WebSocket streams abnormal sensor values to the dashboard within 3 seconds.
   - The **Isolation Forest AI** flags `HIVE-003` as `ABNORMAL`, updates the anomaly score to ~99%, and displays a diagnostic alert banner with recommended actions.
5. **Harvest & Create Honey Batch**:
   - Navigate to **Honey Batches** page. Click **"Create New Batch"** for `HIVE-001`.
   - Set harvest date, quantity (15.0 kg), quality grade, and click **"Create Batch"**.
6. **Verify Blockchain Ledger & Minting**:
   - Click **"Show QR Code"** for the new batch.
   - Navigate to **Blockchain Ledger** page. View newly appended SHA-256 blocks.
   - Click **"Verify Blockchain Integrity"** to perform hash audit verification, resulting in **"Blockchain verified ✓"**.
7. **Consumer Provenance Verification**:
   - Click **"Open Consumer Verification"** or scan the batch QR code to load the public consumer verification page (`/verify/HONEY-2026-0001`).
   - View verified origin hive, certified beekeeper details, harvest date, quality certificate, supply-chain timeline, and cryptographic blockchain authenticity stamp.
