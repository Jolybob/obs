#!/usr/bin/env python3
"""
Build an Obsidian vault from the French PF2e Foundry translation repository.

The upstream project is organized as structured Foundry packs. The current
packs map includes character options, rules, equipment, effects, hazards,
vehicles and a large set of bestiary/adventure collections.

Usage:
  python tools/import_pf2e_fr.py --source ../foundryvtt-pathfinder2-fr --output .
"""
from __future__ import annotations
import argparse, html, re
from pathlib import Path

COLLECTIONS = {
    "feats": ("02 - Personnage/Dons", "feat"),
    "spells": ("03 - Magie/Sorts", "spell"),
    "actions": ("01 - Règles/Actions", "action"),
    "ancestries": ("02 - Personnage/Ascendances", "ancestry"),
    "heritages": ("02 - Personnage/Héritages", "heritage"),
    "backgrounds": ("02 - Personnage/Historiques", "background"),
    "classes": ("02 - Personnage/Classes", "class"),
    "class-features": ("02 - Personnage/Capacités de classe", "class_feature"),
    "ancestry-features": ("02 - Personnage/Capacités d'ascendance", "ancestry_feature"),
    "familiar-abilities": ("02 - Personnage/Pouvoirs des familiers", "familiar_ability"),
    "equipment": ("04 - Équipement", "item"),
    "deities": ("07 - Divinités", "deity"),
    "conditions": ("01 - Règles/États", "condition"),
    "boons-and-curses": ("09 - Traits/Bénédictions et malédictions", "boon_curse"),
    "bestiary-effects": ("09 - Traits/Effets des monstres", "effect"),
    "campaign-effects": ("09 - Traits/Effets des campagnes", "effect"),
    "equipment-effects": ("09 - Traits/Effets de l'équipement", "effect"),
    "feat-effects": ("09 - Traits/Effets des dons et capacités", "effect"),
    "other-effects": ("09 - Traits/Autres effets", "effect"),
    "spell-effects": ("09 - Traits/Effets des sorts", "effect"),
    "bestiary-ability-glossary-srd": ("09 - Traits/Capacités des monstres", "monster_ability"),
    "bestiary-family-ability-glossary": ("09 - Traits/Capacités des familles de monstres", "monster_family_ability"),
    "hazards": ("06 - Dangers", "hazard"),
    "vehicles": ("08 - Véhicules", "vehicle"),
    "kingmaker-features": ("10 - Remaster/Kingmaker", "kingmaker_feature"),
}

BESTIARY = {
    "pathfinder-bestiary": "Bestiaire",
    "pathfinder-bestiary-2": "Bestiaire 2",
    "pathfinder-bestiary-3": "Bestiaire 3",
    "pathfinder-monster-core": "Monstres de base",
    "pathfinder-monster-core-2": "Monstres de base 2",
    "pathfinder-npc-core": "Livre des PNJ",
    "npc-gallery": "Galerie de PNJ",
    "pfs-season-1-bestiary": "Bestiaire Saison 1 PFS",
    "pfs-season-2-bestiary": "Bestiaire Saison 2 PFS",
    "pfs-season-3-bestiary": "Bestiaire Saison 3 PFS",
    "pfs-season-4-bestiary": "Bestiaire Saison 4 PFS",
    "pfs-season-5-bestiary": "Bestiaire Saison 5 PFS",
    "pfs-season-6-bestiary": "Bestiaire Saison 6 PFS",
    "pfs-season-7-bestiary": "Bestiaire Saison 7 PFS",
    "howl-of-the-wild-bestiary": "Howl of the Wild",
    "battlecry-bestiary": "Battlecry",
    "book-of-the-dead-bestiary": "Livre des morts",
    "lost-omens-bestiary": "Prédictions perdues",
    "pathfinder-dark-archive": "Archives sombres",
    "rage-of-elements-bestiary": "Fureur des éléments",
    "age-of-ashes-bestiary": "Age des Cendres",
    "blood-lords-bestiary": "Seigneurs du sang",
    "extinction-curse-bestiary": "Sentence d'Extinction",
    "fall-of-plaguestone": "Chute de Plaguestone",
    "fists-of-the-ruby-phoenix-bestiary": "Poings du Phénix de rubis",
    "gatewalkers-bestiary": "Franchisseur de portail",
    "malevolence-bestiary": "Malveillance",
    "menace-under-otari-bestiary": "Boîte d'initiation",
    "outlaws-of-alkenstar-bestiary": "Hors-la-loi d'Alkenastre",
    "sky-kings-tomb-bestiary": "Tombe du Roi du ciel",
    "strength-of-thousands-bestiary": "Force de milliers",
    "troubles-in-otari-bestiary": "Otari en difficulté",
    "agents-of-edgewatch-bestiary": "Agents d'Absalom",
    "abomination-vaults-bestiary": "Caveau des abominations",
    "kingmaker-bestiary": "Kingmaker",
    "seven-dooms-for-sandpoint-bestiary": "Les sept fléaux de Pointesable",
}

def clean_name(value: str) -> str:
    value = html.unescape(re.sub(r"<[^>]+>", "", value)).strip()
    return re.sub(r'[\\/:*?"<>|]', "-", value)

def field(text: str, label: str) -> str:
    m = re.search(rf"(?mi)^\s*{re.escape(label)}\s*:\s*(.*?)\s*$", text)
    return m.group(1).strip() if m else ""

def desc_block(text: str) -> str:
    patterns = [
        r"(?is)--\s*Desc \(fr\)\s*--\s*(.*?)(?:--\s*End desc\s*--|\Z)",
        r"(?is)--\s*Desc\s*--\s*(.*?)(?:--\s*End desc\s*--|\Z)",
    ]
    body = ""
    for pattern in patterns:
        m = re.search(pattern, text)
        if m:
            body = m.group(1)
            break
    if not body:
        return ""
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
    body = re.sub(r"@UUID\[[^\]]+\]\{([^}]+)\}",
                  lambda m: f"[[{clean_name(m.group(1))}]]", body)
    return re.sub(r"@Compendium\[[^\]]+\]\{([^}]+)\}",
                  lambda m: f"[[{clean_name(m.group(1))}]]", body)

def convert_file(src: Path, out: Path, typ: str, folder: str, collection: str) -> bool:
    raw = src.read_text(encoding="utf-8", errors="replace")
    fr = field(raw, "Nom") or field(raw, "Name") or field(raw, "name")
    en = field(raw, "Name") if field(raw, "Nom") else ""
    if not fr:
        return False

    fr = clean_name(fr)
    desc = convert_refs(desc_block(raw))
    source_id = src.stem
    target = out / folder / f"{fr}.md"
    target.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        "---",
        f'title: "{fr.replace(chr(34), chr(92)+chr(34))}"',
    ]
    if en and en != fr:
        lines.append(f'title_en: "{en.replace(chr(34), chr(92)+chr(34))}"')
    lines += [
        f"type: {typ}",
        f'source_id: "{source_id}"',
        f'collection: "{collection}"',
        'source: "PF2e FR"',
        "tags:",
        "  - pf2e",
        f"  - {typ}",
        f"  - source/{collection}",
        "---",
        "",
        f"# {fr}",
        "",
    ]
    target.write_text("\n".join(lines) + desc + "\n", encoding="utf-8")
    return True

def iter_sources(root: Path, collection: str):
    # Prefer a matching collection directory; if the repository uses a
    # different nested layout, fall back to filenames under data/.
    candidates = [
        root / "data" / collection,
        root / "data" / collection.replace("-", "_"),
    ]
    for base in candidates:
        if base.exists():
            yield from base.rglob("*.htm")
            yield from base.rglob("*.html")
            return

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True, type=Path)
    ap.add_argument("--output", required=True, type=Path)
    args = ap.parse_args()

    counts = {}
    for collection, (folder, typ) in COLLECTIONS.items():
        n = 0
        for src in iter_sources(args.source, collection):
            n += convert_file(src, args.output, typ, folder, collection)
        counts[collection] = n

    # Bestiary packs are represented separately so the vault can retain
    # provenance instead of merging similarly named creatures.
    for collection, display in BESTIARY.items():
        folder = f"05 - Créatures/{display}"
        n = 0
        for src in iter_sources(args.source, collection):
            n += convert_file(src, args.output, "creature", folder, collection)
        counts[collection] = n

    print("\n".join(f"{key}: {value}" for key, value in counts.items()))

if __name__ == "__main__":
    main()
