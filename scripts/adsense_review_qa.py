#!/usr/bin/env python3
"""Deterministic public-corpus checks for the Green Living Trend review set."""
from __future__ import annotations
from collections import defaultdict
from pathlib import Path
import re, sys

ROOT = Path(__file__).resolve().parents[1]
POSTS = ROOT / "src/content/posts"
RETAINED = {
"drought-tolerant-plants-data","home-recycling-reality-data","sustainable-food-choices-data","energy-star-appliances-roi","ev-vs-hybrid-lifecycle-data","low-flow-showerhead-tested","smart-thermostat-savings-low-waste-setup-2026","heat-pump-water-heater-checklist-2026","home-energy-audit-checklist-renters-homeowners","cloth-vs-paper-towel-data","reusable-water-bottles-compared","heat-pump-vs-gas-heater","bamboo-toothbrush-reviewed","composting-bin-guide-small-space","rainwater-collection-setup","silicone-food-storage-tested","eco-friendly-pest-control","sustainable-clothing-brands-compared","solar-charger-portable-tested","led-vs-cfl-bulbs-data","home-energy-rebates-2026-tax-credits-ended","shade-tree-home-cooling-energy-plan","solar-panel-cleaning-soiling-rainfall-safety-guide","space-heater-vs-heat-pump-cost-safety-guide",
"window-heat-loss-curtains-film-air-sealing-calculator",
}
BANNED = re.compile(r"\b(?:adsense|seo)\b|publishing\s+(?:run|workflow)|generated[- ]image\s+qa", re.I)
WORD = re.compile(r"\b[A-Za-z]+(?:[-'][A-Za-z]+)*\b")

def split_doc(text: str):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, re.S)
    if not m: raise ValueError("missing YAML frontmatter")
    return m.group(1), text[m.end():]

def draft_value(fm: str):
    m=re.search(r"^draft:\s*(true|false)\s*$",fm,re.I|re.M)
    return None if not m else m.group(1).lower()=="true"

def visible_text(body: str):
    text=re.sub(r"```.*?```", " ", body, flags=re.S)
    text=re.sub(r"!\[[^]]*\]\([^)]+\)", " ", text)
    text=re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", text)
    text=re.sub(r"https?://\S+", " ", text)
    text=re.sub(r"<[^>]+>", " ", text)
    text=re.sub(r"^\s*import\s+.*$", " ", text, flags=re.M)
    text=re.sub(r"[`*_#>|{}]", " ", text)
    return text

def paragraphs(body: str):
    for block in re.split(r"\n\s*\n", visible_text(body)):
        norm=" ".join(block.split()).lower()
        if len(WORD.findall(norm)) >= 18 and not norm.startswith("choice for "):
            yield norm

def main():
    errors=[]; rows=[]; owners=defaultdict(list)
    files=sorted(POSTS.glob("*.mdx"))
    slugs={p.stem for p in files}
    if not RETAINED <= slugs: errors.append("missing retained files: "+", ".join(sorted(RETAINED-slugs)))
    public=[]
    for p in files:
        try: fm,body=split_doc(p.read_text(encoding="utf-8"))
        except Exception as exc: errors.append(f"{p.name}: {exc}"); continue
        draft=draft_value(fm)
        expected=p.stem not in RETAINED
        if draft is None: errors.append(f"{p.name}: draft boolean is missing")
        elif draft != expected: errors.append(f"{p.name}: draft={str(draft).lower()}, expected {str(expected).lower()}")
        if draft is False: public.append(p.stem)
        if p.stem not in RETAINED: continue
        words=len(WORD.findall(visible_text(body)))
        sources=len(re.findall(r"^  - title:\s*",fm,re.M))
        image_refs=re.findall(r"!\[[^]]*\]\(([^)]+)\)",body)
        vm=re.search(r"^visualsCount:\s*(\d+)\s*$",fm,re.M)
        images=int(vm.group(1)) if vm else len(image_refs)
        if words < 850: errors.append(f"{p.name}: visible words {words} < 850")
        if sources < 8: errors.append(f"{p.name}: sources {sources} < 8")
        if images < 3: errors.append(f"{p.name}: image references {images} < 3")
        for ref in image_refs:
            if ref.startswith("/") and not (ROOT/"public"/ref.lstrip("/")).is_file(): errors.append(f"{p.name}: missing image asset {ref}")
        hit=BANNED.search(visible_text(body))
        if hit: errors.append(f"{p.name}: production-process phrase {hit.group(0)!r}")
        for para in paragraphs(body): owners[para].append(p.name)
        rows.append((p.stem,words,sources,images))
    if len(public)!=len(RETAINED): errors.append(f"public corpus has {len(public)} posts, expected {len(RETAINED)}")
    if set(public)!=RETAINED: errors.append("public corpus does not equal retained allowlist")
    for para,names in owners.items():
        if len(names)>1: errors.append("duplicate 18+ word paragraph in "+", ".join(names)+": "+para[:100])
    print(f"QA corpus: posts={len(files)} retained={len(public)} drafted={len(files)-len(public)}")
    for slug,w,s,i in rows: print(f"PASS {slug}: visible_words={w} sources={s} images={i}")
    if errors:
        print(f"QA FAIL: {len(errors)} violation(s)")
        for e in errors: print(" - "+e)
        return 1
    print("QA PASS: allowlist, draft flags, depth, sources, visual metadata/assets, process-language, and paragraph uniqueness")
    return 0
if __name__=="__main__": sys.exit(main())
