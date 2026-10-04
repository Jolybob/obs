---
title: "Piquants barbelés"
title_en: "Barbed Quills"
type: action
source_id: "oAWNluJaMlaGysXA"
collection: "actions"
source: "PF2e FR"
tags:
  - pf2e
  - action
  - source/actions
---

# Piquants barbelés
**Fréquence** Une fois par jour


**Déclencheur** Vous êtes touché par une Frappe à mains nues ou une frappe avec une arme au corps-à-corps sans allonge.





Vos piquants se brisent dans la peau de votre agresseur. Vous infligez @Damage[ceil(@actor.level/2)d8[piercing]]{1d8 dégâts perforants} à la créature déclencheuse (@Check[reflex|against:class-spell|basic] contre le plus élevé entre votre DD de classe et votre DD de sort). En cas d'échec critique, la créature subit aussi @Damage[(1d4+ceil(@actor.level/2)-1)[bleed]]{1d4 dégâts de saignement} lorsque vos piquants se fichent dans sa peau. Au niveau 3, puis à chaque niveau impair par la suite, ces dégâts augmentent d'1d8 et les dégâts perforants persistants augmentent de 1.
