import json
from schema import EnrichedProduct

class CatalogValidator:
    def __init__(self, raw_text: str, product):
        self.raw_text = raw_text
        self.product = product
        self.audit_logs = []
        self.confidence_score = 1.0

    def run_guardrails(self):
        
        if not self.product.brand or self.product.brand.lower() in ["unbranded", "no brand", "-- unbranded --"]:
            self.audit_logs.append("Rule Failed: Brand is missing or unbranded.")
            self.confidence_score -= 0.20

        if not self.product.standardized_title:
            self.audit_logs.append("Rule Failed: Missing standardized product title.")
            self.confidence_score -= 0.15

        
        for attr in getattr(self.product, "attributes", []):
            val_str = str(attr.value).lower()
           
            if val_str and val_str not in self.raw_text.lower():
                self.audit_logs.append(f"Grounding Warning: Attribute '{attr.key}' value '{attr.value}' not explicitly found in source text.")
                self.confidence_score -= 0.05

        
        self.confidence_score = max(0.0, min(1.0, self.confidence_score))

    def get_report(self) -> dict:
        self.run_guardrails()

       
        is_flagged = len(self.audit_logs) > 0 or self.confidence_score < 0.90

        return {
            "validated_product": self.product.model_dump() if hasattr(self.product, "model_dump") else self.product.dict(),
            "final_confidence_score": round(self.confidence_score, 2),
            "is_flagged_for_review": is_flagged,
            "audit_logs": self.audit_logs,
            "raw_input_text": self.raw_text
        }
