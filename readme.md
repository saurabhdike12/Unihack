# ⚡ CogniSpec AI Engine
### An enterprise-grade multi-modal AI pipeline for automated catalog enrichment, taxonomy mapping, and deterministic rule validation.
🔗 **Live Application Demo:** [https://cognispec-ai.streamlit.app]

🎥 **Walkthrough Video:** [Watch on YouTube]([[https://www.youtube.com/watch?v=YOUR_VIDEO_ID](https://youtu.be/PmReAvRpmNs?si=5qg-l58fpr-zHUtK)](https://youtu.be/PmReAvRpmNs?si=5qg-l58fpr-zHUtK))
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://cognispec-ai.streamlit.app)
[![Built with Gemini](https://img.shields.io/badge/Model-Gemini%20Flash%20%2F%20Pro-blue)](https://ai.google.dev/)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://python.org)
[![Pydantic](https://img.shields.io/badge/Validation-Pydantic%20v2-E92063?logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)

CogniSpec AI is an enterprise-grade product data intelligence engine that automates the ingestion, parsing, normalization, and validation of complex B2B technical datasheets and catalogs.

---

## 📌 Problem Statement

In industrial B2B commerce and supply chain management, onboarding new supplier inventory requires extracting specifications from thousands of multi-page PDF datasheets. 

* **Manual Extraction:** Takes 20–45 minutes per SKU and introduces human transcription errors.
* **Standard LLM Parsers:** Lack deterministic type safety, fail on complex engineering tables, and frequently hallucinate units and ratings.
* **Lack of Auditability:** Enterprise systems require verifiable citation grounding before committing data to production Product Information Management (PIM) databases.

**CogniSpec AI** bridges this gap by combining multimodal Gemini models with deterministic Pydantic schema guardrails, explainable confidence scoring, and a Human-in-the-Loop review workspace.

---

## 🚀 Key Features

* **End-to-End Multimodal Pipeline:** Ingests raw supplier spec sheets (PDF/Images) and enriches catalog entries into fully structured attributes.
* **Accuracy & Anti-Hallucination Guardrails:** Verbatim extraction with source grounding, confidence metrics, and deterministic rule verification to ensure zero false attributes.
* **Enterprise Taxonomy & Standards Compliance:** Automated UNSPSC classification, attribute triplets (`LABEL`, `VALUE`, `UOM`), and direct export to the 252-column Unilog CIMM2 delivery standard.
* **⚡ Multimodal PDF Ingestion:** Natively parses raw technical datasheets, CAD dimension blocks, and complex multi-column electrical/mechanical tables.
* **🛡️ Deterministic Schema Guardrails:** Validates extracted attributes against strict Pydantic models to ensure standard units, range limits, and correct data types.
* **🎯 Explainable Grounding & Confidence Scoring:** Calculates field-level confidence ratings with direct verbatim citations from the source document to guarantee zero hallucinations.
* **👤 Human-in-the-Loop (HITL) Workspace:** Automatically routes low-confidence fields to an inline review interface for rapid catalog manager verification and approval.
* **📜 Real-Time Enterprise Audit Logging:** Immutably records pipeline executions, validation metrics, model reasoning, and manual human overrides.

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **LLM Engine** | Google Gemini API | Multimodal document parsing & attribute extraction |
| **Core Runtime** | Python 3.11+ | Pipeline orchestration and backend processing |
| **Data Validation** | Pydantic v2 | Strict schema enforcement and type integrity |
| **User Interface** | Streamlit | Responsive dashboard & HITL review workspace |
| **Environment** | Streamlit Community Cloud | Cloud deployment and secret management |

---

## 🏗️ Architecture & Data Flow

```text
                           Raw Spec Sheet (PDF/Image) + Unenriched Part Data
                                                │
                                                ▼
                                  [ Multimodal Extraction (LLM) ]
                                                │
                                                ▼
                           [ Schema Parsing & Attribute Triplet Mapping ]
                                                │
                                                ▼
                        [ Deterministic Rule Validation & Confidence Audit ]
                                                │
                                                ▼
                       [ Export to 252-Column Unilog Delivery Schema (.CSV) ]
```
---

## 📦 Quick Start (Local Setup)

### Prerequisites
* Python 3.11 or higher installed
* A Google Gemini API Key

### Installation Steps

1. Clone the repository:
   git clone https://github.com/saurabhdike12/Unihack.git
   cd Unihack

2. Create and activate a virtual environment:
   python -m venv venv
   .\venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Configure Environment Variables:
   Create a .env file in the root directory:
   GOOGLE_API_KEY="your_actual_gemini_api_key_here"

5. Run the Streamlit application:
   streamlit run app.py

---

## 👥 Team — Pair Pulse

| Contributor | Role | GitHub Profile |
| :--- | :--- | :--- |
| **Saurabh Dike** | Lead Architecture & Pipeline Engineering | [@saurabhdike12](https://github.com/saurabhdike12) |
| **Gauri Shinde** | HITL Workspace UI & Data Normalization | [@gaurishinde6402-dev](https://github.com/gaurishinde6402-dev) |
