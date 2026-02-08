# main.py

from fastapi import FastAPI
from pydantic import BaseModel
from rules import infer_products
from scorer import score_lead
from datetime import datetime

app = FastAPI(title="HPCL B2B Lead Intelligence Agent")

class LeadInput(BaseModel):
    company: str
    location: str
    text: str

@app.post("/analyze")
def analyze_lead(data: LeadInput):
    products, reasons = infer_products(data.text)
    urgency, confidence, intent = score_lead(data.text)

    next_action = (
        "Immediate sales outreach" if urgency == "High"
        else "Schedule follow-up"
        if urgency == "Medium"
        else "Monitor account"
    )

    return {
        "company": data.company,
        "location": data.location,
        "signal_summary": data.text[:120] + "...",
        "intent_type": intent,
        "recommended_products": products,
        "reason_codes": reasons,
        "urgency": urgency,
        "confidence_score": confidence,
        "suggested_next_action": next_action,
        "source": {
            "type": "Public Tender / News",
            "timestamp": datetime.now().isoformat(),
            "trust_score": 0.9
        }
    }
