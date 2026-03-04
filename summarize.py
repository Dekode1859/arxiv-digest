#!/usr/bin/env python3
"""
arXiv Digest Summarizer - Phase 2
Uses LLM to enrich paper summaries with categorization and structured output.
"""

import json
import yaml
import urllib.request
import urllib.parse
import ollama
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any

from schemas import PaperSummary
from prompts import build_categorization_prompt, build_summarization_prompt

CONFIG_FILE = "config.yaml"


def load_config():
    """Load configuration from YAML file."""
    with open(CONFIG_FILE, "r") as f:
        return yaml.safe_load(f)


def parse_raw_papers(date_str: str) -> List[Dict[str, Any]]:
    """Parse the raw markdown file to extract paper info."""
    config = load_config()
    output_dir = config.get("output_dir", "papers")
    filename = config.get("output_filename", "arxiv-digest-{date}").format(date=date_str)
    
    filepath = Path(output_dir) / filename
    if not filepath.exists():
        print(f"File not found: {filepath}")
        return []
    
    content = filepath.read_text()
    
    # Parse papers from markdown
    # Format: ### 1. Title ... --- 
    papers = []
    current_paper = None
    
    lines = content.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Look for paper title (### N. Title)
        if line.startswith("### "):
            # Save previous paper
            if current_paper:
                papers.append(current_paper)
            
            # Extract title (remove ### N. )
            title = line[4:].strip()
            
            # Find arXiv ID, PDF link from following lines
            arxiv_id = ""
            pdf_link = ""
            published = ""
            categories = ""
            authors = ""
            abstract = ""
            
            j = i + 1
            while j < len(lines) and not lines[j].startswith("### "):
                if "arXiv ID:" in lines[j]:
                    arxiv_id = lines[j].split("[")[1].split("]")[0] if "[" in lines[j] else ""
                if "PDF:" in lines[j]:
                    pdf_link = lines[j].split("(")[1].split(")")[0] if "(" in lines[j] else ""
                if "Published:" in lines[j]:
                    published = lines[j].split(":")[1].strip()
                if "Categories:" in lines[j]:
                    categories = lines[j].split(":")[1].strip()
                if "Authors:" in lines[j]:
                    authors = lines[j].split(":")[1].strip()
                if "Abstract:" in lines[j]:
                    # Collect abstract lines
                    abstract_lines = []
                    k = j + 1
                    while k < len(lines) and lines[k].strip() and not lines[k].startswith("-"):
                        abstract_lines.append(lines[k].strip())
                        k += 1
                    abstract = " ".join(abstract_lines)
                j += 1
            
            current_paper = {
                "title": title,
                "arxiv_id": arxiv_id,
                "pdf_link": pdf_link,
                "published": published,
                "categories": categories,
                "authors": [a.strip() for a in authors.split(",")],
                "abstract": abstract[:2000],  # Limit abstract length
            }
            i = j
        else:
            i += 1
    
    # Add last paper
    if current_paper:
        papers.append(current_paper)
    
    return papers


def call_llm(prompt: str, config: dict) -> Dict[str, Any]:
    """Call Ollama LLM and parse JSON response."""
    model = config.get("llm", {}).get("model", "minimax-m2.5:cloud")
    temperature = config.get("llm", {}).get("temperature", 0.3)
    
    try:
        response = ollama.chat(
            model=model,
            messages=[
                {"role": "system", "content": "You are an AI research assistant. Respond ONLY with valid JSON."},
                {"role": "user", "content": prompt}
            ],
            options={"temperature": temperature}
        )
        
        content = response["message"]["content"].strip()
        
        # Extract JSON from response
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0]
        elif "```" in content:
            content = content.split("```")[1].split("```")[0]
        
        return json.loads(content.strip())
    
    except Exception as e:
        print(f"LLM call failed: {e}")
        return {}


def process_paper(paper: Dict[str, Any], config: dict) -> Dict[str, Any]:
    """Process a single paper with LLM."""
    title = paper["title"]
    abstract = paper["abstract"]
    focus_areas = config.get("focus_areas", [])
    
    # Step 1: Categorization
    cat_prompt = f"""Analyze this paper. Respond with ONLY valid JSON (no markdown):

{{
  "category": "architecture" | "benchmark" | "method" | "dataset" | "application" | "theory" | "survey",
  "subcategory": "agents" | "llms" | "fine_tuning" | "benchmarking" | "evaluation" | "reasoning" | "multimodal" | "computer_vision" | "nlp" | "robotics" | "reinforcement_learning" | "generative_models" | null,
  "tags": ["tag1", "tag2"]
}}

Title: {title}
Abstract: {abstract[:500]}"""
    
    print(f"  Categorizing: {title[:50]}...")
    cat_result = call_llm(cat_prompt, config)
    
    # Step 2: Summarization
    sum_prompt = f"""Summarize this paper. Respond with ONLY valid JSON:

{{
  "summary": "2-3 sentence plain English summary",
  "implementation_details": "Key technical details",
  "real_world_applications": ["app1", "app2"]
}}

Title: {title}
Abstract: {abstract}"""
    
    print(f"  Summarizing: {title[:50]}...")
    sum_result = call_llm(sum_prompt, config)
    
    # Combine results
    return {
        **paper,
        "category": cat_result.get("category", "method"),
        "subcategory": cat_result.get("subcategory"),
        "tags": cat_result.get("tags", []),
        "summary": sum_result.get("summary", ""),
        "implementation_details": sum_result.get("implementation_details", ""),
        "real_world_applications": sum_result.get("real_world_applications", []),
    }


def generate_enriched_markdown(papers: List[Dict], config: dict) -> str:
    """Generate enriched markdown output."""
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S %Z")
    
    categories = config.get("categories", "")
    
    md = f"""# arXiv AI Digest

**Generated:** {date_str} at {time_str}

**Categories:** {categories}

**Total Papers:** {len(papers)}

---

"""
    
    for i, paper in enumerate(papers, 1):
        tags = ", ".join(paper.get("tags", [])) if paper.get("tags") else "none"
        
        md += f"""### {i}. {paper['title']}

- **arXiv:** [{paper['arxiv_id']}](https://arxiv.org/abs/{paper['arxiv_id']}) | [PDF]({paper['pdf_link']})
- **Published:** {paper['published']}
- **Category:** {paper.get('category', 'N/A')} ({paper.get('subcategory', 'N/A')})
- **Tags:** {tags}

**Summary:**
{paper.get('summary', 'N/A')}

**Implementation:**
{paper.get('implementation_details', 'N/A')}

**Applications:**
{chr(10).join(f"- {app}" for app in paper.get('real_world_applications', []))}

---

"""
    
    return md


def main():
    config = load_config()
    
    # Get today's date
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    # Parse raw papers
    print(f"Loading papers from {date_str}...")
    papers = parse_raw_papers(date_str)
    print(f"Found {len(papers)} papers")
    
    if not papers:
        print("No papers found to process")
        return
    
    # Process each paper with LLM
    print("\nProcessing papers with LLM...")
    enriched_papers = []
    
    for paper in papers:
        try:
            enriched = process_paper(paper, config)
            enriched_papers.append(enriched)
        except Exception as e:
            print(f"Error processing paper: {e}")
            enriched_papers.append(paper)
    
    # Generate enriched markdown
    print("\nGenerating enriched markdown...")
    md_content = generate_enriched_markdown(enriched_papers, config)
    
    # Save to file
    output_dir = config.get("output_dir", "papers")
    filename = config.get("output_filename", "arxiv-digest-{date}").format(date=date_str)
    
    output_path = Path(output_dir) / filename
    output_path.write_text(md_content)
    print(f"\n✅ Saved to: {output_path}")
    
    # Copy to SilverBullet if configured
    sb_space = config.get("silverbullet_space")
    if sb_space:
        sb_path = Path(sb_space) / filename
        sb_path.write_text(md_content)
        print(f"✅ Copied to SilverBullet: {sb_path}")
    
    print(f"\n📄 {len(enriched_papers)} papers enriched")


if __name__ == "__main__":
    main()
