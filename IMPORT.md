# PF2e FR — import complet

Le dépôt suit le corpus français PF2e upstream. La version courante publiée est 8.5.1. citeturn0search0

Le projet upstream indique que son dépôt de données doit être cloné localement et représente environ 800 Mo. citeturn0search4

## Import local

```bash
git clone --depth 1 https://gitlab.com/pathfinder-fr/foundryvtt-pathfinder2-fr.git ../foundryvtt-pathfinder2-fr
python tools/import_pf2e_fr.py --source ../foundryvtt-pathfinder2-fr --output .
```

## Vérification

Après import :

```bash
find . -name "*.md" | wc -l
```

Puis ouvrir le dépôt comme coffre Obsidian.

## Provenance

Le script conserve `source_id` et `collection` dans chaque note. C'est important car le corpus contient des collections de types différents : Items, Actors, journaux et macros. Le fichier upstream `packs.json` fait explicitement cette distinction. citeturn0search1

## Important

Ne pas remplacer automatiquement une entrée absente de traduction par sa version anglaise. Le wiki doit rester clairement identifiable comme corpus français, avec la provenance et l'état de traduction conservés.
