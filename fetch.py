#!/usr/bin/env python3
"""
arXiv Digest Fetcher - Phase 1
Fetches latest AI/ML papers from arXiv and generates a markdown report.
"""

import yaml
import urllib.request
import urllib.parse
from datetime import datetime
from pathlib import Path
import sys

CONFIG_FILE = "config.yaml"


def load_config():
    """Load configuration from YAML file."""
    with open(CONFIG_FILE, "r") as f:
        return yaml.safe_load(f)


def build_query(categories, max_papers):
    """Build arXiv API query string."""
    # Search for papers in specified categories
    cat_query = " OR ".join(f"cat:{cat}" for cat in categories)
    
    # Simple query - just category + sort by date
    query = f"search_query=cat:{categories[0]}"
    query += f"&start=0&max_results={max_papers}"
    query += "&sortBy=submittedDate&sortOrder=descending"
    
    # URL encode only the search_query parameter value
    encoded_search = urllib.parse.quote(query, safe='')
    return f"search_query={encoded_search}"


def fetch_papers(config):
    """Fetch papers from arXiv API."""
    categories = [c.strip() for c in config["categories"].split(",")]
    max_papers = config.get("max_papers", 10)
    
    # Build query - simple format
    cat_query = "+OR+".join(f"cat:{cat}" for cat in categories)
    url = f"http://export.arxiv.org/api/query?search_query=({cat_query})&start=0&max_results={max_papers}&sortBy=submittedDate&sortOrder=descending"
    
    print(f"Fetching papers...")
    
    with urllib.request.urlopen(url, timeout=30) as response:
        xml_content = response.read().decode("utf-8")
    
    return xml_content, categories


def parse_papers(xml_content):
    """Parse arXiv XML response and extract paper info."""
    import xml.etree.ElementTree as ET
    
    # arXiv namespace
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    
    root = ET.fromstring(xml_content)
    entries = root.findall(".//atom:entry", ns)
    
    papers = []
    for entry in entries:
        # Extract fields
        title = entry.find("atom:title", ns).text.strip()
        summary = entry.find("atom:summary", ns).text.strip()
        published = entry.find("atom:published", ns).text.strip()
        
        # Get PDF link
        links = entry.findall("atom:link", ns)
        pdf_link = None
        for link in links:
            if link.get("title") == "pdf":
                pdf_link = link.get("href")
                break
        
        # Get arXiv ID
        arxiv_id = entry.find("atom:id", ns).text.strip().split("/")[-1]
        
        # Get authors
        authors = entry.findall("atom:author/atom:name", ns)
        author_list = [a.text for a in authors]
        
        # Get categories
        categories = entry.findall("atom:category", ns)
        cat_list = [c.get("term") for c in categories]
        
        papers.append({
            "title": title,
            "summary": summary,
            "published": published[:10],  # Just date
            "pdf_link": pdf_link,
            "arxiv_id": arxiv_id,
            "authors": author_list[:3],  # Top 3 authors
            "categories": cat_list,
        })
    
    return papers


def generate_markdown(papers, categories):
    """Generate markdown report."""
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S %Z")
    
    md = f"""# arXiv AI Digest

**Fetched:** {date_str} at {time_str}

**Categories:** {", ".join(categories)}

**Total Papers:** {len(papers)}

---

"""
    
    for i, paper in enumerate(papers, 1):
        md += f"""### {i}. {paper['title']}

- **arXiv ID:** [{paper['arxiv_id']}](https://arxiv.org/abs/{paper['arxiv_id']})
- **PDF:** [Download]({paper['pdf_link']})
- **Published:** {paper['published']}
- **Categories:** {", ".join(paper['categories'])}
- **Authors:** {", ".join(paper['authors'])}

**Abstract:**
{paper['summary'][:500]}{"..." if len(paper['summary']) > 500 else ""}

---

"""
    
    return md, date_str


def main():
    # Load config
    config = load_config()
    
    # Fetch papers
    print("Fetching papers from arXiv...")
    xml_content, categories = fetch_papers(config)
    
    # Parse
    print("Parsing response...")
    papers = parse_papers(xml_content)
    print(f"Found {len(papers)} papers")
    
    # Generate markdown
    print("Generating markdown...")
    md_content, date_str = generate_markdown(papers, categories)
    
    # Save
    output_dir = Path(config.get("output_dir", "papers"))
    output_dir.mkdir(exist_ok=True)
    
    filename = config.get("output_filename", "arxiv-digest-{date}").format(date=date_str)
    output_file = output_dir / filename
    output_file.write_text(md_content)
    
    print(f"\n✅ Saved to: {output_file}")
    
    # Copy to SilverBullet if configured
    sb_space = config.get("silverbullet_space")
    if sb_space:
        filename = config.get("output_filename", "arxiv-digest-{date}").format(date=date_str)
        sb_path = Path(sb_space) / filename
        sb_path.write_text(md_content)
        print(f"✅ Copied to SilverBullet: {sb_path}")
    
    # Copy to MkDocs docs folder if configured
    mkdocs_dir = config.get("mkdocs_docs_dir")
    if mkdocs_dir:
        mkdocs_path = Path(mkdocs_dir) / "papers" / filename
        mkdocs_path.parent.mkdir(parents=True, exist_ok=True)
        mkdocs_path.write_text(md_content)
        print(f"✅ Copied to MkDocs: {mkdocs_path}")
    
    print(f"📄 {len(papers)} papers written")


if __name__ == "__main__":
    main()
