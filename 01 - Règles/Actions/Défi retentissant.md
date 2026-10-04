---
title: "Défi retentissant"
title_en: "Ringing Challenge"
type: action
source_id: "mBqZ2IahMT9Jvo7k"
collection: "actions"
source: "PF2e FR"
tags:
  - pf2e
  - action
  - source/actions
---

# Défi retentissant
vous percutez votre ikône contre une arme, un bouclier ou le sol, en émettant une onde de choc qui inflige @Damage[(max(1,(floor((@actor.level - 2)/2))))d4[spirit],(max(1,(floor((@actor.level - 2)/2))))d4[sonic]|options:area-damage]{1d4 dégâts spirituels et 1d4 dégâts de son} à toutes les créatures dans un @Template[type:cone|distance:30]{cône de 9 mètres} ou une @Template[type:emanation|distance:15]{émanation de 4,50 mètres} (@Check[fortitude|against:exemplar|basic|options:area-effect]). Une créature qui obtient un échec critique sur ce jet de sauvegarde est [[Sourde]] pendant 1 minute.


Au niveau 6 et tous les 2 niveaux suivants, les dégâts spirituels et de son augmentent de 1d4 chacun.
