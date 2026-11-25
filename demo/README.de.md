# Das Isolationsspiel spielen

[English](README.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md)

[English](README.md) · [Deutsche Startseite](../README.de.md) · [Online-Spielbrett](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/index.html) · [D10-Konstruktion](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/d10.html)

Laden Sie das [eigenständige HTML-Spielbrett](index.html) herunter und öffnen Sie es ohne Installation im Browser. Wählen Sie einen Baum und den beginnenden Spieler. Knoten lassen sich anklicken, mit Tab fokussieren und mit Eingabe- oder Leertaste auswählen; alternativ gibt es Schaltflächen für zulässige Züge. Beim Wechsel zwischen Englisch und Chinesisch bleibt die Partie erhalten.

Ein Zug überdeckt den gewählten Knoten und seine Nachbarn. Dabei muss mindestens ein Endknoten einer orangefarbenen Kante neu überdeckt werden. Ein bereits überdeckter Knoten darf gewählt werden, wenn diese Bedingung erfüllt ist. Blaue Umrandungen zeigen alle optimalen Züge der Partei am Zug. Die Zahl auf einer Zugschaltfläche zählt diesen Zug mit und gibt die verbleibende Zugzahl bei beiderseits optimalem Spiel an.

Der Strategiebereich zeigt die Ausgangswerte für beide Startvarianten und eine optimale Fortsetzung ab der aktuellen Stellung. Bei Gleichstand wählen Vorschau und Funktion für einen optimalen Zug den Knoten mit der kleinsten Nummer.

| Baum | D beginnt | S beginnt | Zum Ausprobieren |
|---|---:|---:|---|
| P5 | 1 | 2 | Zuerst 2, dann den bereits überdeckten Knoten 3 wählen. |
| P9 | 3 | 4 | Die freie D-Eröffnung mit dem erzwungenen Start im Zentrum 5 vergleichen. |
| D8 · 22 Knoten | 9 | 10 | Den D-Startwert vor dem zusätzlichen Blatt prüfen. |
| D8 · 23 Knoten | 10 | 10 | Ein zusätzliches Blatt erhöht den D-Startwert auf 10. |

Die Browserprüfung vom 25. November 2026 spielte alle acht optimalen Partien durch und prüfte 141.420 erreichbare Zustände sowie 1.335.806 zulässige Übergänge. Getestet wurden auch Tastatur und Zeiger, Rücknahme, Neustart, Sprachwechsel und Layouts mit 320 und 375 Pixeln Breite.

[Reproduktionsanleitung (Englisch)](../REPRODUCE.md)
