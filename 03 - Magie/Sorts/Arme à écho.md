---
title: "Arme à écho"
title_en: "Echoing Weapon"
type: spell
source_id: "common-01-vtCCVe869shMCJMj"
collection: "spells"
source: "PF2e FR"
tags:
  - pf2e
  - spell
  - source/spells
---

# Arme à écho
Vous canalisez l'énergie dans l'arme ciblée et l'air qui l'entoure bourdonne faiblement à chaque fois qu'elle frappe un coup car l'impact est absorbé par l'arme. Si une créature manie l'arme à la fin de son tour, l'arme émet une explosion de son qui cible une créature adjacente à celui qui la manie. Les dégâts de son infligés sont égaux au nombre de Frappes réussies avec l'arme ciblée que celui qui la manie a effectuées au cours de son tour (jusqu'à un maximum de 4 dégâts de son si le porteur touche avec quatre Frappes).



@Damage[(ceil(@item.rank/2))[sonic]]
@Damage[(ceil(@item.rank/2)*2)[sonic]]
@Damage[(ceil(@item.rank/2)*3)[sonic]]
@Damage[(ceil(@item.rank/2)*4)[sonic]]




**Intensifié (+2)** Les dégâts de son augmentent de 1 par Frappe (et les dégâts maximum augmentent de 4).
