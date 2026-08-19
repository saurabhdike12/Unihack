import os
import json
import pdfplumber
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from schema import EnrichedProduct

# Load environment variables from .env
load_dotenv()

# 1. Extract raw text from PDF
pdf_path = "data/raw_pdfs/BVAL.pdf"
raw_text = ""

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            raw_text += text + "\n"

print("📄 Text extracted successfully. Sending to LLM for structured product intelligence...\n")

# 2. Initialize Model with Structured Output Enforcement
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0
)

# Enforce Pydantic schema
structured_llm = llm.with_structured_output(EnrichedProduct)

# 3. Prompt the Model
prompt = f"""
You are an expert B2B Industrial Product Intelligence AI for e-commerce PIM platforms.
Analyze the following raw technical datasheet text and extract accurate, structured product intelligence.

Raw Datasheet Text:
{raw_text}
"""

try:
    # 4. Invoke LLM
    result: EnrichedProduct = structured_llm.invoke(prompt)
    
    print("✅ Structured Data Generated Successfully!\n")
    print(json.dumps(result.model_dump(), indent=2))
    
    # Save output to a JSON file
    os.makedirs("data/processed_json", exist_ok=True)
    with open("data/processed_json/BVAL_enriched.json", "w") as f:
        json.dump(result.model_dump(), f, indent=2)
        
    print("\n💾 Saved output to: data/processed_json/BVAL_enriched.json")

except Exception as e:
    print("❌ Error during extraction:", e)