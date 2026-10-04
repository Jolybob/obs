---
title: "Souffle de kobold"
title_en: "Kobold Breath"
type: feat
source_id: "ancestry-01-PPUNMjRLQYnmwQvF"
collection: "feats"
source: "PF2e FR"
tags:
  - pf2e
  - feat
  - source/feats
---

# Souffle de kobold
Vous canalisez la puissance de votre bienfaiteur draconique pour projeter un torrent d'énergie de votre bouche qui se manifeste sur une @Template[line|distance:30]{ligne de 9 mètres} ou un @Template[cone|distance:15]{cône de 4,50 mètres}, infligeant @Damage[(ceil(@actor.level / 2))d4|options:area-damage]{1d4 dégâts}. Chaque créature dans la zone doit faire un jet de sauvegarde basique contre le plus élevé entre votre DD de classe et votre DD de sort. Vous ne pouvez plus utiliser cette capacité de nouveau pendant [[/r 1d4 #Recharge Souffle de kobold]]{1d4 rounds}.


Au niveau 3 puis tous les 2 niveaux par la suite, les dégâts augmentent de 1d4. La forme du souffle, le type de dégâts et le jet de sauvegarde correspondent à ceux de votre [[Bienfaiteur draconique]]. Cette activité possède les traits associés à la tradition magique de votre bienfaiteur et le type de dégâts qu'inflige le souffle.





@Check[fortitude|against:class-spell|options:area-damage] @Check[reflex|against:class-spell|options:area-damage] @Check[reflex|against:class-spell|options:area-damage] @Check[will|against:class-spell|options:area-damage]
