import os
import json
import pdfplumber
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from schema import EnrichedProduct


load_dotenv()


pdf_path = "data/raw_pdfs/BVAL.pdf"
raw_text = ""

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            raw_text += text + "\n"

print("📄 Text extracted successfully. Sending to LLM for structured product intelligence...\n")


llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0
)


structured_llm = llm.with_structured_output(EnrichedProduct)


prompt = f"""
You are an expert B2B Industrial Product Intelligence AI for e-commerce PIM platforms.
Analyze the following raw technical datasheet text and extract accurate, structured product intelligence.

Raw Datasheet Text:
{raw_text}
"""

try:
    
    result: EnrichedProduct = structured_llm.invoke(prompt)
    
    print("✅ Structured Data Generated Successfully!\n")
    print(json.dumps(result.model_dump(), indent=2))
    
   
    os.makedirs("data/processed_json", exist_ok=True)
    with open("data/processed_json/BVAL_enriched.json", "w") as f:
        json.dump(result.model_dump(), f, indent=2)
        
    print("\n💾 Saved output to: data/processed_json/BVAL_enriched.json")

except Exception as e:
    print("❌ Error during extraction:", e)
