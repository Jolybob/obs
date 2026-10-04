---
title: "Frappe d'éclats"
title_en: "Shard Strike"
type: feat
source_id: "class-01-ECH7BEQQEq3pCQaS"
collection: "feats"
source: "PF2e FR"
tags:
  - pf2e
  - feat
  - source/feats
---

# Frappe d'éclats
Des éclats de métal se forment dans l'air et s'élancent à partir de vous. Vous pouvez choisir entre des éclats ou des pointes, ce qui modifie la zone, le type de dégâts et l'effet d'échec critique. Chaque créature dans la zone tente un jet de @Check[reflex|against:kineticist|basic|options:area-effect] contre votre DD de classe.




- **Éclats** Les éclats infligent @Damage[(floor((@actor.level -1)/2)+1)d6[slashing]|options:area-damage]{1d6 dégâts perforants} dans un @Template[cone|distance:15]{cône de 4,50 mètres} et une créature qui obtient un échec critique subit @Damage[(floor((@actor.level -1)/2)+1)d6[bleed]]{1d6 dégâts de saignement}.

- **Piquants** Les piquants infligent @Damage[(floor((@actor.level -1)/2)+1)d6[piercing]|options:area-damage]{1d6 dégâts perforants} sur une @Template[line|distance:30]{ligne de 9 mètres} et une créature qui obtient un échec critique est [[Maladroite 1]] jusqu'au début de votre prochain tour.




**Niveau (+2)** Les dégâts augmentent de 1d6.
