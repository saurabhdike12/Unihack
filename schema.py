from pydantic import BaseModel, Field
from typing import List, Optional

class Attribute(BaseModel):
    key: str = Field(description="Spec name e.g., Maximum Pressure, Body Material, Thread Size")
    value: str = Field(description="Spec value e.g., 400 PSI, Stainless Steel, 1/2 inch")
    unit: Optional[str] = Field(description="Unit of measurement e.g., PSI, Bar, AWG, mm")
    source_citation: Optional[str] = Field(description="Exact snippet or page where this was found")

class EnrichedProduct(BaseModel):
    brand: str = Field(description="Manufacturer e.g., Parker, Schneider Electric, Swagelok")
    product_series: str = Field(description="Series name e.g., BVAL Series, PowerPact H-Frame")
    category: str = Field(description="E-commerce taxonomy category e.g., Industrial Valves, Circuit Breakers")
    unspsc_code: Optional[str] = Field(description="UNSPSC classification code if determinable")
    standardized_title: str = Field(description="SEO E-commerce Title")
    attributes: List[Attribute] = Field(description="List of extracted technical spec key-value pairs")
    marketing_description: str = Field(description="High-converting catalog description for procurement buyers")
    bullet_points: List[str] = Field(description="Key bullet features for the catalog listing")
    confidence_score: float = Field(description="Model confidence score between 0.0 and 1.0")
    flagged_for_human_review: bool = Field(description="True if confidence < 0.8 or data is missing")