---
title: "Peau toxique"
title_en: "Toxic Skin"
type: action
source_id: "kKKHwVUnroKuAnOt"
collection: "actions"
source: "PF2e FR"
tags:
  - pf2e
  - action
  - source/actions
---

# Peau toxique
**Fréquence** Une fois par heure


**Déclencheur** Une créature vous touche, par exemple en vous [[Saisissant]], en réussissant à vous toucher avec une attaque à mains nues ou en utilisant un sort de contact contre vous.





**Effet** Vous exsudez une toxine mortelle. La créature déclencheuse subit @Damage[(ceil(@actor.level/2))d4[poison]]{dégâts de poison selon le niveau} (@Check[fortitude|against:class-spell|basic] en utilisant le plus élevé entre votre DD de classe et votre DD de sort). Au niveau 3 et tous les niveaux impairs par la suite, les dégâts augmentent de 1d4.
