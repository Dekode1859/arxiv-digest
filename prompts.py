"""
LLM prompts for paper summarization
"""

from typing import List


SYSTEM_PROMPT = """You are an AI research assistant that academic analyzes papers and extracts structured information. 
Respond ONLY with valid JSON, no other text.
Focus on accuracy and brevity."""


CATEGORIZATION_PROMPT = """Analyze this paper title and abstract. Classify it.

Respond with JSON:
{{
  "category": "architecture" | "benchmark" | "method" | "dataset" | "application" | "theory" | "survey",
  "subcategory": "transformer" | "diffusion" | "reinforcement_learning" | "llm" | "agent" | "multimodal" | "vision" | "nlp" | "reasoning" | "robotics" | "generative" | "benchmark" | "fine_tuning" | null,
  "tags": ["tag1", "tag2"]
}}

Paper:
Title: {title}
Abstract: {abstract}"""


SUMMARIZATION_PROMPT = """Summarize this paper in 2-3 sentences, then extract implementation details and applications.

Respond with JSON:
{{
  "summary": "2-3 sentence plain English summary",
  "implementation_details": "Key technical details (architecture, model size, methodology)",
  "real_world_applications": ["app1", "app2", "app3"]
}}

Paper:
Title: {title}
Abstract: {abstract}"""


def build_categorization_prompt(title: str, abstract: str, focus_areas: List[str]) -> str:
    """Build categorization prompt with dynamic focus areas."""
    focus_text = ", ".join(focus_areas)
    prompt = CATEGORIZATION_PROMPT.format(title=title, abstract=abstract[:500])
    
    # Add focus area hint
    prompt += f"\n\nFocus on detecting: {focus_text}"
    
    return prompt


def build_summarization_prompt(title: str, abstract: str) -> str:
    """Build summarization prompt."""
    return SUMMARIZATION_PROMPT.format(title=title, abstract=abstract)
