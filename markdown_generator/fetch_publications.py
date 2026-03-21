#!/usr/bin/env python3
"""
Fetch publications from Google Scholar and generate Jekyll markdown files.

Usage:
    python fetch_publications.py

This script:
1. Fetches all publications from the Google Scholar profile
2. Generates individual markdown files in _publications/
3. Each file has YAML front matter with title, authors, venue, year, date, url

To update publications, just re-run this script. It will overwrite existing files.

Requirements:
    pip install scholarly
"""

import json
import os
import re
import html

SCHOLAR_ID = "6MfHyuMAAAAJ"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "_publications")

def html_escape(text):
    table = {"&": "&amp;", '"': "&quot;", "'": "&apos;"}
    return "".join(table.get(c, c) for c in text)

def make_slug(title):
    slug = re.sub(r"[^a-zA-Z0-9\s-]", "", title)
    slug = re.sub(r"\s+", "-", slug.strip())
    slug = re.sub(r"-+", "-", slug)
    return slug[:80]

def fetch_publications():
    from scholarly import scholarly

    print(f"Fetching publications for Scholar ID: {SCHOLAR_ID}")
    author = scholarly.search_author_id(SCHOLAR_ID)
    author = scholarly.fill(author, sections=["publications"])

    pubs = []
    total = len(author["publications"])
    for i, pub in enumerate(author["publications"]):
        print(f"  Fetching details [{i+1}/{total}]: {pub['bib'].get('title', '?')[:60]}")
        filled = scholarly.fill(pub)
        bib = filled.get("bib", {})
        pubs.append({
            "title": bib.get("title", ""),
            "author": bib.get("author", ""),
            "venue": bib.get("venue", bib.get("journal", bib.get("conference", ""))),
            "year": str(bib.get("pub_year", "")),
            "url": filled.get("pub_url", ""),
            "num_citations": filled.get("num_citations", 0),
        })

    return pubs

def generate_markdown(pubs):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Clear old generated files
    for f in os.listdir(OUTPUT_DIR):
        if f.endswith(".md"):
            os.remove(os.path.join(OUTPUT_DIR, f))

    count = 0
    for pub in pubs:
        title = pub["title"]
        year = pub["year"]
        if not title or not year:
            continue

        slug = make_slug(title)
        date = f"{year}-01-01"
        md_filename = f"{date}-{slug}.md"

        venue = pub["venue"] or ""
        authors = pub["author"] or ""
        url = pub["url"] or ""

        md = "---\n"
        md += f'title: "{html_escape(title)}"\n'
        md += f"collection: publications\n"
        md += f"permalink: /publication/{date}-{slug}\n"
        md += f"date: {date}\n"
        md += f"year: {year}\n"
        md += f"venue: '{html_escape(venue)}'\n"
        md += f"authors: '{html_escape(authors)}'\n"
        if url:
            md += f"paperurl: '{url}'\n"
        md += f"citation: '{html_escape(authors)}, \"{html_escape(title)}.\" {html_escape(venue)}, {year}.'\n"
        md += "---\n"

        if url:
            md += f"\n[Access paper here]({url}){{:target=\"_blank\"}}\n"

        with open(os.path.join(OUTPUT_DIR, md_filename), "w") as f:
            f.write(md)
        count += 1

    print(f"\nGenerated {count} publication files in {OUTPUT_DIR}")

def main():
    pubs = fetch_publications()

    # Save raw data as cache for reference
    cache_path = os.path.join(os.path.dirname(__file__), "publications_cache.json")
    with open(cache_path, "w") as f:
        json.dump(pubs, f, indent=2)
    print(f"Cached raw data to {cache_path}")

    generate_markdown(pubs)

if __name__ == "__main__":
    main()
