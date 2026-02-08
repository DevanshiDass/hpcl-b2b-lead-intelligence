# HPCL B2B Lead Intelligence Agent

## 1. Executive Overview
HPCL’s Direct Sales (DS) / Bulk Fuels & Specialties business serves large industrial customers across sectors such as **power, chemicals, infrastructure, shipping, mining, and manufacturing**.  

While the sales motion is strong, **early-stage discovery** of new plants, capacity expansions, tenders, and procurement signals remains largely manual and relationship-driven.

This project delivers a **B2B Lead Intelligence Agent** that continuously converts **public web signals** into **actionable, explainable, sales-ready leads** for HPCL’s field sales teams.

---

## 2. Problem Statement
Design and build a system that can:
1. Discover potential B2B customers (new and existing) using public web signals.
2. Infer likely product requirements from HPCL’s Direct Sales portfolio.
3. Generate a structured **Lead Dossier** with urgency, confidence, and next-best-action.
4. Notify local sales officers through a mobile-friendly workflow.
5. Enable feedback capture for continuous improvement.

---

## 3. Solution Overview
We implemented an **end-to-end, explainable B2B Lead Intelligence prototype** that:

- Ingests public signals such as tenders, news articles, and website text
- Extracts industrial and operational cues (equipment, processes, sector indicators)
- Maps signals to HPCL Direct Sales products using rule-based inference
- Scores leads on urgency and confidence
- Generates a structured Lead Dossier
- Exposes a **mobile-first (PWA-style)** interface for sales officers
- Provides executive-level visibility via a dashboard
- Is designed for scalable, enterprise deployment

---

## 4. System Architecture
The solution follows an **event-driven, modular pipeline**:

Public Web Signals
↓
Signal Ingestion & Extraction
↓
Product-Need Inference Engine
↓
Lead Scoring Engine
↓
Lead Dossier Generator
↓
Mobile Sales UI + Notifications
↓
Executive Dashboard & Feedback Loop


Detailed deployment and scalability considerations are documented in **`ARCHITECTURE.md`**.

---

## 5. Core Components

### 5.1 Backend API (FastAPI)
- **File:** `main.py`
- Responsible for:
  - Accepting public signal input
  - Orchestrating inference and scoring
  - Generating structured Lead Dossiers
- Exposes a REST endpoint: `/analyze`

---

### 5.2 Product-Need Inference Engine
- **File:** `rules.py`
- Implements explainable, rule-based inference using:
  - **Keyword detection:** FO, LSHS, HSD, Bitumen, Solvents, Marine fuels, etc.
  - **Operational cues:** boilers, furnaces, captive power plants, ports, road projects, jute mills, solvent usage
- Outputs:
  - Top 3 recommended HPCL DS products
  - Human-readable **reason codes** for transparency

---

### 5.3 Lead Scoring Engine
- **File:** `scorer.py`
- Scores leads based on:
  - Intent strength (explicit tender vs indirect mention)
  - Signal clarity and relevance
- Outputs:
  - Urgency classification (High / Medium / Low)
  - Confidence score for sales prioritization

---

### 5.4 Mobile Sales UI (PWA-style)
- **File:** `ui.py`
- Browser-based, mobile-friendly interface designed for field sales officers
- Key features:
  - New lead discovery
  - Full lead dossier view
  - One-tap action to notify sales officer
- WhatsApp notifications are **sandboxed (mocked)** as explicitly allowed

---

### 5.5 Executive Dashboard
- **File:** `dashboard.py`
- Provides management-level insights including:
  - Leads per week
  - Conversion funnel
  - Top products
  - Top sectors
  - Geographic concentration

---

## 6. Expected Deliverables Mapping

### 6.1 Working Prototype ✅
- Source ingestion + extraction: Public signal input
- Product inference + scoring: `rules.py`, `scorer.py`
- Lead dossier generation: API output
- Mobile UI: Streamlit-based, PWA-style interface
- Notifications: Sandbox mock implementation

---

### 6.2 Model Card ✅
- **File:** `MODEL_CARD.md`
- Documents:
  - Inference logic
  - Limitations
  - Bias risks and mitigation strategies

---

### 6.3 Demo Dataset ✅
- **File:** `demo_dataset.csv`
- Contains labelled sample company signals and mapped product needs
- Designed for validation and future ML training

---

### 6.4 Executive Dashboard ✅
- **File:** `dashboard.py`
- Demonstrates leadership-level KPIs and insights

---

### 6.5 Deployment Architecture ✅
- **File:** `ARCHITECTURE.md`
- Covers:
  - Event-driven design
  - Monitoring approach
  - Cost estimation
  - Cloud-readiness

---

## 7. How to Run Locally (Optional)

### Install Dependencies
```bash
pip install -r requirements.txt
Run Backend API
uvicorn main:app --reload
Run Mobile UI
streamlit run ui.py
Run Executive Dashboard
streamlit run dashboard.py
8. Design Principles
Explainability-first over black-box ML

Policy-safe use of public data sources

Sales-centric workflows aligned with field operations

Modular, scalable architecture for enterprise deployment

9. Future Enhancements
Machine learning–based inference models

Live web crawling and RSS ingestion

CRM and ERP integration

Territory-based lead routing

Feedback-driven model retraining

10. Notes
External integrations (WhatsApp) are sandboxed as permitted

Prototype prioritizes clarity, correctness, and scalability over overengineering


---

## ✅ WHY THIS VERSION IS STRONG

- Sounds like an **enterprise architecture document**
- Easy for judges to **scan section headers**
- Explicitly maps to **every deliverable**
- Uses **HPCL’s vocabulary**, not generic AI buzzwords
- Defends design choices (rules, explainability, sandboxing)

This README can **replace your pitch entirely**.

---

---

## 📸 UI Screenshots & Demo Assets

To support review without a live demo, the repository includes a comprehensive set of **application screenshots** covering all major system components.

All screenshots are available in the **`/screenshots`** folder at the root of this repository.

### Included Screenshots

#### 📱 Mobile Sales Application (PWA-style)
- New Lead Discovery screen
- Lead Dossier detail view
- Sales notification / outreach action flow

These screens demonstrate the mobile-first workflow designed for HPCL field sales officers, enabling rapid lead review and action.

---

#### 📊 Executive Dashboard
- Executive KPIs and conversion funnel
- Product-wise and sector-wise insights

This view provides leadership with macro-level visibility into demand trends and sales pipeline health.

---

#### 🛢️ Product Intelligence
- Inferred product recommendations
- Explainable reason codes mapped to industrial signals

This illustrates how public signals are converted into HPCL Direct Sales product insights.

---

#### 🌍 Regional Performance Insights
- Geographic distribution of leads
- Regional concentration of demand signals

Designed to support territory planning and resource allocation.

---

#### 📄 Lead Dossier Output
- Generated structured Lead Dossier
- Consolidated view of company profile, inferred demand, urgency, and next-best-action

This represents the final sales-ready output consumed by the field sales team.

> **Note:** Reviewers are encouraged to open the `screenshots/` folder to view all UI and dashboard visuals corresponding to the above components.

