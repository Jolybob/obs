---
title: "Barrage aigre"
title_en: "Acrid Barrage"
type: action
source_id: "NRjBkjYx10MAXp3T"
collection: "actions"
source: "PF2e FR"
tags:
  - pf2e
  - action
  - source/actions
---

# Barrage aigre
**Fréquence** Une fois par round





**Effet** Chaque ennemi dans votre aura subit @Damage[ternary(gte(@actor.level, 18), 7, ternary(gte(@actor.level, 15), 6, 5))d6[acid]]{5d6 dégâts d'acide} et @Damage[2d6[persistent,acid]]{2d6 dégâts d'acide persistants}avec un jet de @Check[reflex|against:class-spell|basic] contre leplus élevé entre votre DD de classe ou votre DD de sort. Les dégâts initiaux passent à 6d6 au niveau 15 et à 7d6 au niveau 18.
