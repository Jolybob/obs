---
title: "Exploser"
title_en: "Explode"
type: action
source_id: "naKVqd8POxcnGclz"
collection: "actions"
source: "PF2e FR"
tags:
  - pf2e
  - action
  - source/actions
---

# Exploser
Vous amenez volontairement votre innovation au-delà de ses limites de sécurité habituelles, la faisant exploser en infligeant des dégâts aux créatures proches sans endommager l'innovation... avec un peu de chance. L'explosion inflige @Damage[max(2, @actor.level)d6[@actor.flags.system.inventor.explode]|options:area-damage]{2d6 dégâts de feu} avec un jet de @Check[reflex|against:inventor|basic|options:area-effect] à toutes les créatures dans une @Template[emanation|distance:5]{émanation de 1,50 mètre} autour de vous (si vous maniez ou portez l'innovation) ou autour de votre innovation (si votre innovation est un sbire).


Au niveau 3, puis à chaque niveau par la suite, augmentez les dégâts de l'explosion de 1d6. Si vous avez la capacité de classe Innovation de rupture, vous pouvez choisir également une @Template[emanation|distance:10]{émanation de 3 mètres} pour la zone lorsque vous utilisez Exploser. Si vous avez la capacité de classe Innovation révolutionnaire, vous pouvez choisir une émanation de 1,50 mètre, de 3 mètres ou @Template[emanation|distance:15]{de 4,50 mètres}.
