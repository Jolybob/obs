---
title: "Jeu de l'esprit vengeur"
title_en: "Vengeful Spirit Deck"
type: feat
source_id: "class-06-z8NUh2FayDa7Ctnp"
collection: "feats"
source: "PF2e FR"
tags:
  - pf2e
  - feat
  - source/feats
---

# Jeu de l'esprit vengeur
**Conditions** Vous avez un présage de Tourment actif.





Vous faites apparaître un jeu fantomatique de cartes du Tourment. Tirez une carte d'un jeu du Tourment, puis choisissez une cible dans les 18 mètres. La carte vole à travers les airs pour Frapper cette cible, lui infligeant 4d6 dégâts, avec un jet de @Check[reflex|against:class-spell|basic] contre votre DD de classe. Le type de dégâts infligé est déterminé par votre présage de Tourment. Si la carte tirée est de la même couleur que votre présage de Tourment actif, la cible subit une pénalité de statut de -2 à son jet de sauvegarde. Les dégâts passent à 6d6 si vous êtes au moins de niveau 10 et de 8d6 si vous êtes au moins de niveau 15. Vous pouvez continuer pour tirer des cartes sur les cibles lors de votre tour tant que vous Maintenez le jeu de l'esprit vengeur — lancer une carte prend deux actions. Cet effet dure tant que vous le Maintenez, jusqu'à 1 minute ou jusqu'à ce que vous n'ayez plus de présage du Tourment actif. Une fois que l'effet se termine, vous perdez votre présage de Tourment actif.


**Marteaux** @Damage[(ternary(gte(@actor.level,15),8,ternary(gte(@actor.level,10),6,4)))d6[cold]]{4d6 dégâts de froid}


**Clés** @Damage[(ternary(gte(@actor.level,15),8,ternary(gte(@actor.level,10),6,4)))d6[fire]]{4d6 dégâts de feu}


**Boucliers** @Damage[(ternary(gte(@actor.level,15),8,ternary(gte(@actor.level,10),6,4)))d6[poison]]{4d6 dégâts de poison}


**Livres** @Damage[(ternary(gte(@actor.level,15),8,ternary(gte(@actor.level,10),6,4)))d6[electricity]]{4d6 dégâts d'électricité}


**Étoiles** @Damage[(ternary(gte(@actor.level,15),8,ternary(gte(@actor.level,10),6,4)))d6[mental]]{4d6 dégâts mentaux}


**Couronnes** @Damage[(ternary(gte(@actor.level,15),8,ternary(gte(@actor.level,10),6,4)))d6[acid]]{4d6 dégâts d'acide}
