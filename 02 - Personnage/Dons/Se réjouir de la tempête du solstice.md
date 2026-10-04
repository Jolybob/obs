---
title: "Se réjouir de la tempête du solstice"
title_en: "Rejoice in Solstice Storm"
type: feat
source_id: "class-08-LFS9M737RCt0Jq8r"
collection: "feats"
source: "PF2e FR"
tags:
  - pf2e
  - feat
  - source/feats
---

# Se réjouir de la tempête du solstice
**Fréquence** Une fois par heure





Vous tendez les bras et la fureur des saisons vient vous étreindre dans la liesse. Une tempête s'élève en spirale autour de vous, infligeant 5d8 dégâts (voir ci-dessous) à chaque créature dans une @Template[type:emanation|distance:30]{émanation de 9 mètres}, avec un jet de @Check[reflex|against:exemplar|basic|options:area-effect] contre votre DD de classe. Au niveau 10 et tous les 2 niveaux par la suite, les dégâts augmentent de 1d8.


L'émanation est coupé en quatre cônes ne se chevauchant pas, chacune des saisons différentes, qui doit être arrangé dans le sens des aiguilles d'une montre du printemps, à l'été, à l'automne, à l'hiver. Chaque cône possède différents traits, un type de dégâts et un effet différent à une créature qui a obtenu un échec critique sur son jet de sauvegarde : une créature suffisamment grande pour être dans de multiples saisons peut choisir celle par laquelle elle est affectée.




- **Printemps** (électricité) La foudre du printemps inflige @Damage[(ceil((1+@actor.level)/2))d8[electricity]|options:area-damage|traits:electricity]{5d8 dégâts d'électricité}. Les créatures qui ont obtenu un échec critique sont laissées engourdies, devenant [[Maladroit 2]] jusqu'à la fin de leur prochain tour.

- **Été** (eau) Une mousson d'été inflige @Damage[(ceil((1+@actor.level)/2))d8[bludgeoning]|options:area-damage|traits:water]{5d8 dégâts contondants}. Les créatures qui obtiennent un échec critique sont mises [[À terre]] par des vents d'ouragan.

- **Automne** (bois, émotion, mental) Des feuilles qui tombent infligent @Damage[(ceil((1+@actor.level)/2))d8[slashing]|options:area-damage|traits:emotion,mental,wood]{5d8 dégâts tranchants}. Les créatures qui obtiennent un échec critique sont saisies par la mélancolie, devenant [[Prises au dépourvu]] jusqu'à la fin de leur prochain tour.

- **Hiver** (froid) Un blizzard inflige @Damage[(ceil((1+@actor.level)/2))d8[cold]|options:area-damage|traits:cold]{5d8 dégâts de froid}. Les créatures qui obtiennent un échec critique sont [[Stupéfiées 2]] jusqu'à la fin de leur prochain tour lorsque le froid engourdit leurs sens.
