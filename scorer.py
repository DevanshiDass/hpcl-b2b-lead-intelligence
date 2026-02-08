# scorer.py

def score_lead(text: str):
    text = text.lower()

    if "tender" in text or "rfp" in text:
        return "High", 0.9, "Explicit procurement signal"

    if "new plant" in text or "expansion" in text:
        return "Medium", 0.7, "Capacity expansion signal"

    return "Low", 0.4, "General informational signal"
