---
title: "Irradiation (Déviant)"
title_en: "Irradiate"
type: feat
source_id: "class-06-79GUhBznFfYqdwgO"
collection: "feats"
source: "PF2e FR"
tags:
  - pf2e
  - feat
  - source/feats
---

# Irradiation (Déviant)
Vous exsuder une aura radioactive, rendant tous ceux qui sont autour de vous malades. Toutes les créatures dans une @Template[emanation|distance:15]{émanation de 4,50 mètres} doivent réussir un jet de @Check[fortitude|against:class-spell] contre le plus élevé entre votre DD de sort ou votre DD de classe ou être [[Nauséeuses 1]]. En cas d'échec critique, elles sont aussi [[Fatiguées]] pendant 1 minute. Vous êtes immunisé à votre propre radioactivité. La valeur de l'état nauséeux augment de 1 par tranche de 5 niveaux que vous possédez au-delà du 6e.


**Éveillé** vous êtes plus efficace lorsqu'il s'agit d'émettre cette aura radioactive. Le rayon de l'émanation passe à @Template[emanation|distance:60]{18 m}.


**Éveillé** Les radiations sont plus puissantes. Les créatures dans la zone subissent @Damage[(floor(@actor.level/2))d4[poison]|options:area-damage]{1d4 dégâts de poison} supplémentaires par tranche de 2 niveaux que vous possédez, avec un jet de @Check[fortitude|against:class-spell|basic] contre le plus élevé entre votre DD de sort ou votre DD de classe (lancez le jet de Vigueur une fois et appliquez le à la fois aux dégâts et à l'état nauséeux).
