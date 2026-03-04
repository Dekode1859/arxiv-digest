"""
Pydantic schemas for arxiv-digest
"""

from pydantic import BaseModel, Field
from typing import List, Literal, Optional


class PaperSummary(BaseModel):
    """LLM-generated summary for a paper."""
    
    # Categorization
    category: str = Field(description="Main category: architecture, benchmark, method, dataset, application, theory, or survey")
    subcategory: Optional[str] = Field(default=None, description="Specific subcategory like transformer, RL, agent, etc.")
    
    # Summary (2-3 sentences, plain English)
    summary: str = Field(description="2-3 sentence plain English summary of what the paper proposes")
    
    # Implementation details
    implementation_details: str = Field(description="Key technical details, architecture, model sizes, or methodological contributions")
    
    # Real-world applications
    real_world_applications: List[str] = Field(description="List of potential real-world applications or use cases")
    
    # Tags for quick filtering
    tags: List[str] = Field(description="Relevant tags like LLM, robotics, code_generation, etc.")
    
    # Validation
    def validate_fields(self):
        """Ensure no empty critical fields."""
        if not self.summary or len(self.summary) < 20:
            raise ValueError("Summary too short")
        if not self.category:
            raise ValueError("Category is required")
