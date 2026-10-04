---
title: "Morts gémissants"
title_en: "Wailing Dead"
type: feat
source_id: "class-12-wp9Pnu2qe7GkZgHS"
collection: "feats"
source: "PF2e FR"
tags:
  - pf2e
  - feat
  - source/feats
---

# Morts gémissants
**Fréquence** Une fois toutes les 10 minutes


**Conditions** Votre horde est relevée et est composée d'esprits.





Les voix des esprits que vous dirigez répandent la peur dans le cœur de vos ennemis. Vous Maintenez votre horde et ordonnez à ces esprits de crier à l'unisson. Chaque ennemi vivant dans une @Template[type:emanation|distance:20]{émanation de 6 mètres} de votre horde subit @Damage[ternary(lte(@actor.level, 12),5,(floor(@actor.level/2)-1))d10[mental]|options:area-damage]{5d10 dégâts mentaux}, en fonction du résultat à leur jet de @Check[will|against:spell|options:area-effect] contre votre DD de sort. Ces dégâts augmentent de 1d10 au niveau 14 puis tous les 2 niveaux par la suite.





**Succès critique** La créature n'est pas affectée.


**Succès** La créature subit la moitié des dégâts et est [[Effrayée 1]].


**Échec** La créature subit la totalité des dégâts et est [[Effrayée 2]].


**Échec critique** La créature subit le double des dégâts et est [[Effrayée 3]].
