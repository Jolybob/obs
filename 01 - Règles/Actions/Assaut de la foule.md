---
title: "Assaut de la foule"
title_en: "Mobbing Assault"
type: action
source_id: "yWTdfPklh8jL94GZ"
collection: "actions"
source: "PF2e FR"
tags:
  - pf2e
  - action
  - source/actions
---

# Assaut de la foule
**Conditions** Votre horde a été relevée





**Effet** Chaque ennemi dans une @Template[type:emanation|distance:5]{émanation de 1,50 mètre} autour de votre horde subit @Damage[(ternary(gte(@actor.level,18),8,ternary(gte(@actor.level,14),6,ternary(gte(@actor.level,10),4,2))))d6[bludgeoning]|options:area-damage]{2d6 dégâts contondants} (si votre horde est constituée de zombies) ou @Damage[(ternary(gte(@actor.level,18),8,ternary(gte(@actor.level,14),6,ternary(gte(@actor.level,10),4,2))))d6[slashing]|options:area-damage]{2d6 dégâts tranchants} (si votre horde est composée de squelettes) avec un jet de @Check[reflex|against:spell|basic|options:area-effect] contre votre DD de sort. Au niveau 10 puis tous les 4 niveaux par la suite, les dégâts augmentent de 2d6.
