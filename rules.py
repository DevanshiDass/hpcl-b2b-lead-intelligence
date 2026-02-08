# rules.py

PRODUCT_RULES = {
    "boiler": ["FO", "LSHS"],
    "furnace": ["FO", "LSHS"],
    "captive power": ["FO", "HSD"],
    "genset": ["HSD"],
    "diesel generator": ["HSD"],
    "road project": ["Bitumen"],
    "highway": ["Bitumen"],
    "solvent": ["Hexane", "Solvent 1425"],
    "chemical plant": ["Hexane", "Solvent 1425"],
    "jute": ["Jute Batch Oil"],
    "bunker": ["Marine Fuel"],
    "port": ["Marine Fuel"],
    "shipping": ["Marine Fuel"]
}

def infer_products(text: str):
    text = text.lower()
    products = []
    reasons = []

    for keyword, mapped_products in PRODUCT_RULES.items():
        if keyword in text:
            products.extend(mapped_products)
            reasons.append(f"Matched keyword: {keyword}")

    # remove duplicates, keep top 3
    products = list(dict.fromkeys(products))[:3]

    return products, reasons
