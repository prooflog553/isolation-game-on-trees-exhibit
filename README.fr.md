# Le jeu d’isolement sur les arbres

[English](README.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [Español](README.es.md) · **Français** · [Deutsch](README.de.md) · [Português](README.pt.md)

**Comment le diamètre d’un arbre influence-t-il la durée du jeu d’isolement ?** Pour la borne arrondie à l’entier supérieur étudiée ici, le changement décisif se situe entre les diamètres 9 et 10.

[Article (PDF, anglais)](manuscript/Isolation_Game_Research_Report.pdf) · [Sources et compilation Lean (anglais)](formal/README.md) · [Plateau interactif (anglais/chinois)](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/index.html)

## Résumé

Sur un arbre à $n$ sommets, Dominator, lorsqu’il commence, peut-il toujours terminer en au plus $\lceil3n/7\rceil$ coups ? Ce travail établit cette borne pour tout arbre fini de diamètre **au plus 9**. Au diamètre **10**, pour tout entier positif $k$, nous construisons un arbre à $210k$ sommets qui exige au moins $91k$ coups en jeu optimal, quel que soit le premier joueur ; la borne de référence vaut $90k$.

La preuve de la borne supérieure associe des réductions structurelles, des certificats finis et des stratégies pour 14 familles comportant un nombre arbitraire de branches ordinaires. La borne inférieure repose sur une construction modulaire extensible et une stratégie correspondante. Le dépôt rassemble l’article, les sources formelles, les calculs de vérification et les présentations interactives.

![La borne jusqu’au diamètre 9 et les contre-exemples de diamètre 10](assets/diameter-threshold.svg)

## À l’origine de la question

La recherche portait d’abord sur une borne plus forte, arrondie à l’entier inférieur. Un exemple la contredit : ajouter une feuille au centre d’un arbre à 22 sommets conserve son diamètre 8, mais porte de 9 à 10 sa valeur lorsque Dominator commence. Pour 23 sommets, l’arrondi inférieur vaut 9 et l’arrondi supérieur 10. La question est alors devenue : jusqu’à quel diamètre cette dernière borne est-elle garantie ? [Références et portée des théorèmes (anglais)](manuscript/SOURCES.md)

## Règles du jeu

Deux joueurs choisissent à tour de rôle un sommet. Choisir un sommet marque ce sommet et tous ses voisins. Un coup est légal s’il marque pour la première fois au moins une extrémité d’une arête dont les deux extrémités étaient non marquées avant le coup. On peut donc choisir un sommet déjà marqué. Le jeu prend fin lorsqu’il ne reste aucune arête dont les deux extrémités sont non marquées. Dominator cherche à minimiser le nombre de coups, Staller à le maximiser.

Sur le chemin 1–2–3–4–5, jouer 2 marque les sommets 1, 2 et 3. Jouer ensuite 3 est légal : le coup marque le sommet 4, une extrémité de la dernière arête dont les deux extrémités étaient encore non marquées, et termine la partie.

## Résultats

- **Diamètre au plus 9.** Dans le jeu ordinaire, si tous les sommets sont initialement non marqués et que Dominator commence, la valeur du jeu sur un arbre fini à $n$ sommets est au plus $\lceil 3n/7\rceil$. La même borne n’est pas établie lorsque Staller commence.
- **Diamètre exactement 10.** Pour tout entier $k\ge1$, il existe un arbre de $210k$ sommets dont la valeur du jeu est au moins $91k$, quel que soit le premier joueur. La borne précédente vaudrait $\lceil 3(210k)/7\rceil=90k$. Cela ne donne ni une valeur exacte de $91k$, ni la minimalité du contre-exemple à 210 sommets.

## Le tournant de la recherche : une seule feuille

Relions les sommets centraux de trois chemins disjoints de sept sommets à un nouveau sommet central. L’arbre obtenu a 22 sommets et le jeu dure 9 coups en jeu optimal si Dominator commence. Ajouter une feuille au centre ne change pas le diamètre, qui reste égal à 8, mais porte le jeu à 10 coups pour 23 sommets. À cette taille, la borne arrondie à l’entier inférieur donne 9 et échoue, alors que l’entier supérieur vaut 10. Ce contre-exemple a motivé le changement de conjecture ; le calcul sur deux arbres ne prouve pas la nouvelle borne en général.

## Des essais à la démonstration

Sur le chemin à neuf sommets, commencer au centre conduit à quatre coups si les deux joueurs jouent au mieux, alors qu'une ouverture libre de Dominator permet de finir en trois. Cet exemple écarte une stratégie générale, sans réfuter la borne recherchée.

La construction de diamètre 10 relie en étoile les centres de $14k$ modules de 15 sommets. La preuve finale contrôle d'abord la phase centrale, puis le jeu restant. Pour le diamètre 9, des certificats finis traitent les cas locaux et les stratégies de 14 familles couvrent un nombre arbitraire de branches ordinaires.

La personne responsable a orienté la recherche et demandé des examens critiques ; les systèmes d'IA ont proposé et révisé constructions et arguments. Les calculs Python vérifient des exemples et des certificats finis ; Lean vérifie les énoncés formalisés. Les archives de la recherche comportent des lacunes.

Pour D9, un contre-exemple sur des forêts prémarquées a écarté la règle générale selon laquelle ajouter un chemin de sept sommets augmente toujours la valeur d'au plus trois. Cet exemple local se distingue du théorème sur les arbres connexes initialement non marqués. Dans D7, la correspondance du sommet marqué d'un graphe auxiliaire a été corrigée et les petits cas, auparavant supposés, ont été démontrés séparément.

## Explorer et vérifier

- [Article complet (PDF, anglais)](manuscript/Isolation_Game_Research_Report.pdf) · [Carte des preuves (anglais)](EVIDENCE_MAP.md)
- [Histoire de la recherche (anglais)](RESEARCH.md) · [Guide de reproduction (anglais)](REPRODUCE.md) · [Sources et compilation Lean (anglais)](formal/README.md)
- [Plateau interactif (anglais/chinois)](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/index.html) · [Construction D10 (anglais/chinois)](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/d10.html)
- [Mode d’emploi du plateau (français)](demo/README.fr.md)
- [Licences et mentions (anglais)](LICENSE_SCOPE.md)


*Édition et maintenance de l’archive: Cen Yi (岑弈).*
