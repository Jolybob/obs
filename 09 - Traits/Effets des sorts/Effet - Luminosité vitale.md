---
title: "Effet - Luminosité vitale"
title_en: "Spell Effect: Vital Luminance"
type: effect
source_id: "6ArAZeZyYSNLI0X5"
collection: "spell-effects"
source: "PF2e FR"
tags:
  - pf2e
  - effect
  - source/spell-effects
---

# Effet - Luminosité vitale
Accordé par [[Luminosité vitale]]


Vous émettez une lumière vive dans une émanation de 9 mètres (et de lumière faible dans les 9 mètres suivants).


Si une créature morte-vivante vous inflige des dégâts avec une attaque ou un sort alors qu'elle se trouve dans la zone de lumière vive de votre aura, la créature subit des dégâts de vitalité égaux à la moitié de la valeur de votre réservoir de luminosité. Elle subit ces dégâts uniquement la première fois qu'elle vous inflige des dégâts lors d'un round. (@Damage[(0.5 * @item.badge.value * @item.level)[vitality]])


Vous pouvez Révoquer ce sort. Quand vous le faites, vous pouvez cibler une créature située dans votre lumière et diriger l'énergie vitale vers elle. La cible doit être une créature vivante consentante ou une créature morte-vivante. Cela guérit une cible vivante ou inflige des dégâts à une cible morte-vivante d'un montant égal à la valeur de votre réservoir de luminosité. (@Damage[(@item.badge.value * @item.level)[healing]]{Soins})





*Note : La valeur du réservoir est le niveau de l'effet x la valeur du badge de cet effet. Le niveau de l'effet sera fixé automatiquement lorsque vous incantez le sort.*
