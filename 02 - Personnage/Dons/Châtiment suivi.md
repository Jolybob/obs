---
title: "Châtiment suivi"
title_en: "Following Smite"
type: feat
source_id: "class-16-uyZ3gY7gtKCLiywR"
collection: "feats"
source: "PF2e FR"
tags:
  - pf2e
  - feat
  - source/feats
---

# Châtiment suivi
**Conditions** Votre dernière action a consisté à porter une Frappe avec une arme ou à mains nues bénéficiant de l'[[Arme du héraut]].





Vous faites appel à la puissance de votre divinité et la canalisez à travers votre arme. La créature que vous avez touché au cours de votre action précédente doit faire un jet de @Check[reflex|against:class-spell] contre le plus élevé entre votre DD de classe ou votre DD de sort.





**Succès critique** La cible n'est pas affectée.


**Succès** La cible subit des @Damage[(floor(@actor.level/2))[spirit]]{dégâts spirituels égaux à la moitié de votre niveau}.


**Échec** La cible subit des @Damage[(@actor.level)[spirit]]{dégâts spirituels égaux à votre niveau} et se retrouve [[À terre]].


**Échec critique** La cible subit des @Damage[(2*@actor.level)[spirit]]{dégâts spirituels égaux au double de votre niveau}, se retrouve À terre, et est [[Maladroite 1]] jusqu'au début de votre prochain tour.
