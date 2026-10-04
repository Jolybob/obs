# PF2e FR importer

The upstream French Foundry translation currently has a large structured corpus. Its `packs.json` defines collections such as ascendances, héritages, historiques, classes, capacités de classe, dons, sorts, actions and multiple equipment/bestiary collections. citeturn0search2

## Import

Clone the upstream repository next to this repository, then run:

```bash
python tools/import_pf2e_fr.py --source ../foundryvtt-pathfinder2-fr --output .
```

The importer creates one Markdown note per `.htm` source entry and adds:

- French title
- English title when present
- stable upstream file id
- PF2e type
- searchable tags
- French description
- common Foundry UUID references converted to Obsidian `[[wikilinks]]`

## Current upstream target

The translation repository's latest tagged release is **8.5.1 (September 26, 2026)**. citeturn0search0

The upstream translation status is not uniformly complete; for example, its current feat-effects status lists 828 entries as free to translate and 18 with no translation. Therefore the vault should preserve translation status rather than silently treating every upstream entry as official French content. citeturn0search1
