# arxiv-digest

Automated arXiv paper digest that fetches latest AI/ML research papers and generates markdown summaries.

## Setup

```bash
# Install dependencies
pip install pyyaml

# Run fetcher
python fetch.py
```

## Configuration

Edit `config.yaml` to customize:
- Categories to search
- Max papers to fetch
- Output directories

## Features

- Fetches papers from arXiv API (cs.AI, cs.LG, cs.CL, stat.ML)
- Generates markdown with titles, links, abstracts
- Auto-copies to SilverBullet space
- Configurable via YAML
