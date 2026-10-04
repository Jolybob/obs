---
title: "Vengeance destructrice"
title_en: "Destructive Vengeance"
type: action
source_id: "r5Uth6yvCoE4tr9z"
collection: "actions"
source: "PF2e FR"
tags:
  - pf2e
  - action
  - source/actions
---

# Vengeance destructrice
**Déclencheur** Un ennemi dans votre aura de champion vous inflige des dégâts.





**Effet** Le sang appelle le sang lorsque vous menez votre ennemi vers son anéantissement. Vous augmentez le montant des dégâts que vous subissez de @Damage[(ternary(gte(@actor.level,19),6,ternary(gte(@actor.level,16),5,ternary(gte(@actor.level,12),4,ternary(gte(@actor.level,9),3,ternary(gte(@actor.level,5),2,1))))))d6] et vous infligez [[/r {1d6}]]{1d6 dégâts} à l'ennemi déclencheur et vous infligez @Damage[(ternary(gte(@actor.level,19),6,ternary(gte(@actor.level,16),5,ternary(gte(@actor.level,12),4,ternary(gte(@actor.level,9),3,ternary(gte(@actor.level,5),2,1))))))d6[spirit]|options:destructive-vengeance:enemy] à l'ennemi déclencheur. Les dégâts que vous subissez et que vous infligez en utilisant cette réaction passent à 2d6 au niveau 5, 3d6 au niveau 9, 4d6 au niveau 12, 5d6 au niveau 16 et 6d6 au niveau 19.


[[Effet - Dégâts supplémentaires du champion]]
