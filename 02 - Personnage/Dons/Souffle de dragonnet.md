---
title: "Souffle de dragonnet"
title_en: "Dragonet Breath"
type: feat
source_id: "ancestry-01-RaqjaXp2miOq4Bis"
collection: "feats"
source: "PF2e FR"
tags:
  - pf2e
  - feat
  - source/feats
---

# Souffle de dragonnet
Vous avez développé votre souffle magique. Vous soufflez le souffle de dragonnet associé à votre héritage. Souffle de dragonnet obtient les traits indiqués entre parenthèses et le DD est le plus élevé entre votre DD de classe ou votre DD de sort. Après avoir utilisé Souffle de dragonnet, vous ne pouvez plus l'utiliser avant [[/r 1d4 #Recharger Souffle de dragonnet]]{1d4 rounds}.




- **Dragonnet fée** (arcanique, poison) Vous soufflez un @Template[type:cone|distance:15]{cône de 4,50 mètres} de gaz euphorisant. Chaque créature dans la zone doit réussir un jet de @Check[fortitude|against:class-spell|options:area-effect,inflicts:stupefied|traits:arcane,poison] ou être [[Stupéfiée 1]] pendant 1 round.

- **Dragonnet de perle** (arcanique, malédiction) Vous soufflez un @Template[type:cone|distance:15]{cône de 4,50 mètres} de brume dorée qui altère la chance des créatures prises en son sein. Chaque fois que vous utilisez Souffle de dragonnet, décidez s'il donne de la chance ou de la malchance. Toute créature affectée par votre Souffle de dragonnet devient temporairement immunisée pendant 1 heure. Si votre souffle accorde de la chance, chaque créature dans la zone obtient un bonus de statut de +1 à son prochain jet d'attaque ou test de compétence avant le début de votre prochain tour. Si votre souffle apporte de la malchance, chaque créature dans la zone doit tenter un jet de @Check[will|against:class-spell|options:area-effect|traits:arcane,curse]. Une créature qui obtient un échec sur son jet de sauvegarde subit une pénalité de statut de -1 sur son prochain jet d'attaque ou test de compétence avant le début de votre prochain tour. Sur un échec critique, la créature doit, à la place, lancer deux fois les dés et prendre le pire résultat sur le test. C'est un effet d'infortune.

- **Dragonnet de la marée** (feu) Vous soufflez sur une @Template[type:line|distance:15]{ligne de 4,50 mètres} de gaz surchauffé qui inflige @Damage[(ceil(@actor.level/2))d4[fire]|options:area-damage]{2d4 dégâts de feu} avec un jet de @Check[reflex|against:class-spell|basic|options:area-effect|traits:fire]. Au niveau 3 et tous les 2 niveaux par la suite, les dégâts augmentent de 1d4. Vous pouvez utiliser votre souffle sous l'eau bien qu'il possède le trait feu. Si vous le faites, il obtient le trait eau et émerge sous forme de @Template[type:cone|distance:20]{cône de 6 mètres} d'eau bouillante.

- **Drake domestique** (arcanique, mental) Vous soufflez un nuage de brume argentée dans un @Template[type:cone|distance:15]{cône de 4,50 mètres} qui inflige @Damage[(ceil(@actor.level/2))d4[mental]|options:area-damage]{2d4 dégâts mentaux} avec un jet de @Check[will|against:class-spell|options:area-effect,damage:material:silver|traits:arcane,mental]. Il est considéré comme de l'argent par rapport aux faiblesses. Au niveau 3 et tous les 2 niveaux par la suite, les dégâts augmentent de 1d4.

- **Drake guide** (acide) Vous émettez une @Template[type:line|distance:30]{ligne de 9 mètres} de crachat d'acide qui inflige @Damage[(ceil(@actor.level/2))d4[acid]|options:area-damage]{2d4 dégâts d'acide} avec un jet de @Check[reflex|against:class-spell|basic|options:area-effect|traits:acid]. Au niveau 3 et tous les 2 niveaux par la suite, les dégâts augmentent de 1d4.
