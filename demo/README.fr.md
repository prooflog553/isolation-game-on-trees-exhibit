# Jouer au jeu d'isolement

[English](README.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md)

[English](README.md) · [Accueil en français](../README.fr.md) · [Plateau en ligne](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/index.html) · [Construction D10](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/d10.html)

Téléchargez le [plateau HTML autonome](index.html) et ouvrez-le dans un navigateur, sans installation. Choisissez un arbre et le premier joueur. Cliquez sur un sommet, atteignez-le avec Tab puis appuyez sur Entrée ou Espace, ou utilisez les boutons des coups légaux. Le passage de l'anglais au chinois conserve la partie.

Chaque coup couvre le sommet choisi et ses voisins ; il doit couvrir pour la première fois une extrémité d'une arête orange. Un sommet déjà couvert reste jouable s'il satisfait cette condition. Les contours bleus indiquent tous les coups optimaux du joueur au trait. Le nombre affiché sur chaque bouton inclut ce coup et donne le nombre de coups restants si les deux joueurs jouent au mieux.

Le panneau de stratégie indique les valeurs initiales pour les deux premiers joueurs possibles et une suite optimale depuis la position actuelle. En cas d'égalité, l'aperçu et la commande de coup optimal choisissent le sommet de plus petit numéro.

| Arbre | D commence | S commence | À essayer |
|---|---:|---:|---|
| P5 | 1 | 2 | Jouer 2 puis le sommet 3, déjà couvert. |
| P9 | 3 | 4 | Comparer l'ouverture libre de D avec un premier coup imposé au centre 5. |
| D8 · 22 sommets | 9 | 10 | Vérifier la valeur de D avant l'ajout de la feuille. |
| D8 · 23 sommets | 10 | 10 | L'ajout d'une feuille porte la valeur de D à 10. |

Le contrôle dans le navigateur du 25 novembre 2026 a parcouru les huit parties optimales et vérifié 141 420 états accessibles ainsi que 1 335 806 transitions légales. Il a aussi testé le clavier, le pointeur, l'annulation, le redémarrage, le changement de langue et les largeurs de 320 et 375 pixels.

[Guide de reproduction (anglais)](../REPRODUCE.md)
