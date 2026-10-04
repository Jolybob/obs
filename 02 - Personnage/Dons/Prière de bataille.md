---
title: "Prière de bataille"
title_en: "Battle Prayer"
type: feat
source_id: "skill-07-nBlzWZnmYuFHrMyV"
collection: "feats"
source: "PF2e FR"
tags:
  - pf2e
  - feat
  - source/feats
---

# Prière de bataille
En invoquant votre divinité, vous récitez des écritures dans le but de blesser un adversaire. Lorsque vous obtenez ce don, choisissez bien, chaos, loi ou mal. Votre choix doit correspondre à une des composantes d'alignement de votre divinité. Cette action possède le trait correspondant à l'alignement choisi.


Faites un test de @Check[religion|against:will] contre le DD de Volonté d'un adversaire situé dans les 9 mètres. L'adversaire est alors temporairement immunisé contre les Prières de bataille de votre divinité pendant 1 journée.





**Succès critique** Vous infligez @Damage[(ternary(gte(@actor.skills.religion.rank,4),6,2))d6[untyped]]{2d6 dégâts} du type de l'alignement choisi ou 6d6 dégâts si vous êtes légendaire en Religion.


**Succès** Vous infligez @Damage[(ternary(gte(@actor.skills.religion.rank,4),3,1))d6[untyped]]{1d6 dégâts} du type de l'alignement choisi ou 3d6 dégâts si vous êtes légendaire en Religion.


**Échec** Il n'y a pas d'effet.


**Échec critique ** Le contrecoup de la volonté de votre ennemi contre votre prière vous empêche d'utiliser Prière de bataille de nouveau pendant 10 minutes.
