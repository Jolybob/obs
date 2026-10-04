---
title: "Projection en rotation"
title_en: "Whirling Throw"
type: feat
source_id: "class-06-w0nSRBNwexM5Dh0D"
collection: "feats"
source: "PF2e FR"
tags:
  - pf2e
  - feat
  - source/feats
---

# Projection en rotation
**Conditions** Vous [[Agrippez]] ou [[Entravez]] une créature.





Vous projetez votre adversaire au loin. Faites un test d'[[Athlétisme]] contre le DD de Vigueur de l'adversaire. Vous subissez une pénalité de circonstances de -2 si votre cible est d'une taille plus grande que vous, et une pénalité de circonstances de -4 si elle est plus grande que cela. Vous obtenez un bonus de circonstances de +2 si la cible est d'une taille plus petite que vous, et un bonus de circonstances de +4 si elle est plus petite que cela.





**Succès critique** Vous projetez la créature à une distance de votre choix jusqu'à 3 mètres plus 1,50 mètre multiplié par votre modificateur de Force ([[/r 3+(1*@actor.abilities.str.mod)]] mètres). Elle subit des dégâts contondants égaux à votre modificateur de Force plus 1d6 par tranche de 3 mètres à laquelle vous la lancez (@Damage[((floor((10+(5*@actor.abilities.str.mod))/10))d6 + @actor.abilities.str.mod)[bludgeoning]] dégâts). Si vous lancez la cible d'au moins 3 mètres sur un obstacle solide, utilisez la distance maximale à laquelle vous auriez pu la lancer pour calculer les dégâts. La créature tombe [[À terre]].


**Succès** Comme pour un succès critique, mais la créature ne tombe pas À terre.


**Échec** Vous ne projetez pas la créature.


**Échec critique** Vous ne projetez pas la créature et elle n'est plus ni [[Saisie]] ni [[Entravée]] par vous.
