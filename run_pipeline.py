import os
import json
import pdfplumber
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from schema import EnrichedProduct
from catalog_validator import CatalogValidator

load_dotenv()

def process_pdf(pdf_path: str, llm):
    filename = os.path.basename(pdf_path)
    print(f"\n==========================================")
    print(f"⚙️ Processing Document: {filename}")
    print(f"==========================================")

  
    raw_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                raw_text += text + "\n"

   
    structured_llm = llm.with_structured_output(EnrichedProduct)
    prompt = f"Analyze the following raw technical datasheet text and extract accurate, structured product intelligence.\n\n{raw_text}"
    
    raw_extracted: EnrichedProduct = structured_llm.invoke(prompt)

   
    validator = CatalogValidator(raw_text, raw_extracted)
    audit_report = validator.get_report()

    
    output_dir = "data/processed_json"
    os.makedirs(output_dir, exist_ok=True)
    output_filename = f"{output_dir}/{os.path.splitext(filename)[0]}_validated.json"
    
    with open(output_filename, "w") as f:
        json.dump(audit_report, f, indent=2)

    print(f"✅ Extraction & Validation Complete!")
    print(f"📊 Final Confidence: {audit_report['final_confidence_score']}")
    print(f"🚩 Human Review Required: {audit_report['is_flagged_for_review']}")
    if audit_report['audit_logs']:
        print("📋 Audit Logs:")
        for log in audit_report['audit_logs']:
            print(f"   {log}")
    print(f"💾 Saved to: {output_filename}")

if __name__ == "__main__":
    llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash", temperature=0)
    pdf_folder = "data/raw_pdfs"
    
    for file in os.listdir(pdf_folder):
        if file.endswith(".pdf"):
            process_pdf(os.path.join(pdf_folder, file), llm)
