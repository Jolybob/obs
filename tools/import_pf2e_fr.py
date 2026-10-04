#!/usr/bin/env python3
"""
Build an Obsidian vault from the French PF2e Foundry translation repository.

Usage:
  python tools/import_pf2e_fr.py --source ./foundryvtt-pathfinder2-fr --output ./PF2e-FR

The importer is intentionally conservative: it preserves the French text,
keeps the English name when present, stores the upstream file id, and converts
common Foundry UUID links into Obsidian wikilinks where a French name is known.
"""
from __future__ import annotations
import argparse, html, re
from pathlib import Path

CATEGORIES = {
    "data/feats": ("02 - Personnage/Dons", "feat"),
    "data/spells": ("03 - Magie/Sorts", "spell"),
    "data/actions": ("01 - Règles/Actions", "action"),
    "data/ancestries": ("02 - Personnage/Ascendances", "ancestry"),
    "data/heritages": ("02 - Personnage/Héritages", "heritage"),
    "data/backgrounds": ("02 - Personnage/Historiques", "background"),
    "data/classes": ("02 - Personnage/Classes", "class"),
    "data/classfeatures": ("02 - Personnage/Capacités de classe", "class_feature"),
    "data/equipment": ("04 - Équipement", "item"),
}

def clean_name(value: str) -> str:
    value = html.unescape(re.sub(r"<[^>]+>", "", value)).strip()
    return re.sub(r'[\\/:*?"<>|]', "-", value)

def field(text: str, label: str) -> str:
    m = re.search(rf"(?mi)^\s*{re.escape(label)}\s*:\s*(.*?)\s*$", text)
    return m.group(1).strip() if m else ""

def html_block(text: str, start: str, end: str | None = None) -> str:
    m = re.search(rf"(?is)--\s*{re.escape(start)}\s*--\s*(.*?)(?:--\s*{re.escape(end)}\s*--|\Z)", text)
    if not m:
        return ""
    body = m.group(1)
    body = re.sub(r"<hr\s*/?>", "\n\n", body, flags=re.I)
    body = re.sub(r"<li>", "\n- ", body, flags=re.I)
    body = re.sub(r"</li>", "", body, flags=re.I)
    body = re.sub(r"<br\s*/?>", "\n", body, flags=re.I)
    body = re.sub(r"</p>", "\n\n", body, flags=re.I)
    body = re.sub(r"<p[^>]*>", "", body, flags=re.I)
    body = re.sub(r"<strong>(.*?)</strong>", r"**\1**", body, flags=re.I|re.S)
    body = re.sub(r"<em>(.*?)</em>", r"*\1*", body, flags=re.I|re.S)
    body = re.sub(r"<[^>]+>", "", body)
    return html.unescape(body).strip()

def convert_refs(body: str) -> str:
    # @UUID[...,]{French name} -> [[French name]]
    return re.sub(r"@UUID\[[^\]]+\]\{([^}]+)\}", lambda m: f"[[{clean_name(m.group(1))}]]", body)

def convert_file(src: Path, root: Path, out: Path, typ: str, folder: str):
    raw = src.read_text(encoding="utf-8", errors="replace")
    fr = field(raw, "Nom") or field(raw, "Name")
    en = field(raw, "Name") if field(raw, "Nom") else ""
    if not fr:
        return False
    desc = html_block(raw, "Desc (fr)", "End desc") or html_block(raw, "Desc (en)", "End desc")
    desc = convert_refs(desc)
    source_id = src.stem
    target = out / folder / f"{clean_name(fr)}.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    fm = [
        "---",
        f'title: "{fr.replace(chr(34), chr(92)+chr(34))}"',
        f'type: {typ}',
        f'source_id: "{source_id}"',
        'source: "PF2e FR"',
        "tags:",
        "  - pf2e",
        f"  - {typ}",
        "---",
        "",
        f"# {fr}",
        "",
    ]
    if en and en != fr:
        fm.insert(2, f'title_en: "{en.replace(chr(34), chr(92)+chr(34))}"')
    target.write_text("\n".join(fm) + desc + "\n", encoding="utf-8")
    return True

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True, type=Path)
    ap.add_argument("--output", required=True, type=Path)
    args = ap.parse_args()
    counts = {}
    for rel, (folder, typ) in CATEGORIES.items():
        base = args.source / rel
        n = 0
        if base.exists():
            for src in base.rglob("*.htm"):
                n += convert_file(src, args.source, args.output, typ, folder)
        counts[typ] = n
    print(counts)

if __name__ == "__main__":
    main()
