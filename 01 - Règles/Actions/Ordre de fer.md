---
title: "Ordre de fer"
title_en: "Iron Command"
type: action
source_id: "M8RCbthRhB4bxO9t"
collection: "actions"
source: "PF2e FR"
tags:
  - pf2e
  - action
  - source/actions
---

# Ordre de fer
**Déclencheur** Un ennemi dans votre aura de champion vous inflige des dégâts.





**Effet** Vous remettez l'impertinent ennemi qui a osé vous blesser à sa place. Vous ordonnez à l'ennemi de se prosterner devant vous en signe d'obéissance. S'il ose refuser, il doit en payer le prix dans la douleur et l'angoisse. L'ennemi doit choisir une des deux options suivantes.




- **S'agenouiller** L'ennemi tombe [[À terre]] par une action gratuite.

- **Refuser** Vous lui infligez @Damage[(ternary(gte(@actor.level,19),6,ternary(gte(@actor.level,16),5,ternary(gte(@actor.level,12),4,ternary(gte(@actor.level,9),3,ternary(gte(@actor.level,5),2,1))))))d6[mental]]{1d6 dégâts mentaux}. Ces dégâts passent à 2d6 au niveau 5, 3d6 au niveau 9, 4d6 au niveau 12, 5d6 au niveau 16 et 6d6 au niveau 19.

Quelle que soit l'option choisie, vos Frappes contre cet ennemi infligeront 1 dégât spirituel supplémentaire jusqu'à la fin de votre prochain tour. Ces dégâts supplémentaires passent à 2 au niveau 9 et à 3 au niveau 16.


[[Effet - Dégâts supplémentaires du champion]]
