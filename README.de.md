# Das Isolationsspiel auf Bäumen

[English](README.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [Español](README.es.md) · [Français](README.fr.md) · **Deutsch** · [Português](README.pt.md)

**Wie beeinflusst der Durchmesser eines Baumes die Dauer des Isolationsspiels?** Für die hier untersuchte aufgerundete Schranke liegt die entscheidende Grenze zwischen Durchmesser 9 und 10.

[Aufsatz (PDF, Englisch)](manuscript/Isolation_Game_Research_Report.pdf) · [Lean-Quellen und Builds (Englisch)](formal/README.md) · [Interaktives Spielbrett (Englisch/Chinesisch)](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/index.html)

## Zusammenfassung

Kann Dominator auf einem Baum mit $n$ Knoten als erster Spieler immer innerhalb von $\lceil3n/7\rceil$ Zügen beenden? Diese Arbeit beweist die Schranke für jeden endlichen Baum mit Durchmesser **höchstens 9**. Bei Durchmesser **10** konstruieren wir für jede positive ganze Zahl $k$ einen Baum mit $210k$ Knoten, der bei optimalem Spiel und unabhängig vom Startspieler mindestens $91k$ Züge erfordert; der aufgerundete Vergleichswert beträgt $90k$.

Der Beweis der oberen Schranke verbindet strukturelle Reduktionen und endliche Zertifikate mit Strategien für 14 Familien, die beliebig viele gewöhnliche Zweige zulassen. Die untere Schranke beruht auf einer skalierbaren Modulkonstruktion und einer zugehörigen Strategie. Das Repository enthält den Aufsatz, formale Quellen, Nachrechnungen und interaktive Darstellungen.

![Obere Schranke bis Durchmesser 9 und Gegenbeispielfamilie bei Durchmesser 10](assets/diameter-threshold.svg)

## Ausgangspunkt

Zunächst stand eine stärkere, abgerundete Schranke im Mittelpunkt. Ein kleines Beispiel widerlegt sie: Fügt man am Zentrum eines Baumes mit 22 Knoten ein Blatt hinzu, bleibt der Durchmesser 8, während der optimale D-Startwert von 9 auf 10 steigt. Für 23 Knoten ergibt Abrunden 9 und Aufrunden 10. Daraus entstand die Frage, bis zu welchem Durchmesser die aufgerundete Schranke gilt. [Literatur und Geltungsbereich der Sätze (Englisch)](manuscript/SOURCES.md)

## Spielregeln

Zwei Spieler wählen abwechselnd einen Knoten. Dabei werden der gewählte Knoten und alle seine Nachbarn markiert. Ein Zug ist zulässig, wenn er mindestens einen Endknoten einer Kante neu markiert, deren beide Endknoten vor dem Zug unmarkiert waren. Der gewählte Knoten darf bereits markiert sein. Das Spiel endet, sobald keine Kante mehr zwei unmarkierte Endknoten hat. Dominator möchte die Zahl der Züge minimieren, Staller möchte sie maximieren.

Auf dem Pfad 1–2–3–4–5 markiert der Zug auf Knoten 2 zunächst die Knoten 1, 2 und 3. Der nächste Zug auf Knoten 3 ist zulässig: Er markiert Knoten 4, einen Endknoten der letzten Kante mit zwei unmarkierten Endknoten, und beendet das Spiel.

## Ergebnisse

- **Durchmesser höchstens 9.** In der gewöhnlichen Variante sind anfangs alle Knoten unmarkiert. Beginnt Dominator, ist der Spielwert auf einem endlichen Baum mit $n$ Knoten höchstens $\lceil 3n/7\rceil$. Für einen Start durch Staller ist dieselbe Schranke nicht nachgewiesen.
- **Durchmesser genau 10.** Zu jeder ganzen Zahl $k\ge1$ gibt es einen Baum mit $210k$ Knoten, dessen Spielwert für beide Startvarianten mindestens $91k$ beträgt. Die obige Schranke ergäbe $\lceil 3(210k)/7\rceil=90k$. Weder der exakte Spielwert $91k$ noch die Minimalität des Gegenbeispiels mit 210 Knoten werden behauptet.

## Der Wendepunkt: ein einziges Blatt

Man verbindet die Mittelknoten dreier paarweise disjunkter Pfade mit je sieben Knoten mit einem neuen Zentrum. Der Baum hat damit 22 Knoten; bei optimalem Spiel und einem Start durch Dominator dauert das Spiel 9 Züge. Hängt man am Zentrum ein Blatt an, bleibt der Durchmesser 8, doch bei nun 23 Knoten steigt der Spielwert auf 10. Für diese Knotenzahl ergibt Abrunden die falsche Schranke 9; Aufrunden ergibt 10. Das Gegenbeispiel gab Anlass, die Vermutung zu ändern. Die Berechnung für zwei Bäume beweist die neue Schranke aber noch nicht allgemein.

## Vom Versuch zum Beweis

Auf dem Pfad mit neun Knoten führt ein Start im Zentrum bei optimalem Weiterspiel zu vier Zügen. Bei freier Wahl des ersten Zuges kann Dominator dagegen in drei Zügen beenden. Das Beispiel widerlegt eine allgemeine Eröffnungsstrategie, nicht die angestrebte Schranke.

Die Konstruktion mit Durchmesser 10 verbindet die Zentren von $14k$ Modulen mit je 15 Knoten sternförmig. Der endgültige Beweis kontrolliert zuerst die Zentrumsphase und danach das verbleibende Spiel. Für Durchmesser 9 behandeln endliche Zertifikate lokale Fälle; Strategien für 14 Familien erfassen beliebig viele gewöhnliche Zweige.

Der Mensch gab die Forschungsrichtung vor und verlangte kritische Prüfungen; KI-Systeme schlugen Konstruktionen und Argumente vor und überarbeiteten sie. Python prüft Beispiele und endliche Zertifikate; Lean prüft die formalisierten Aussagen. Die überlieferten Forschungsaufzeichnungen sind lückenhaft.

Für D9 widerlegte ein Gegenbeispiel auf vormarkierten Wäldern die allgemeine Regel, dass ein zusätzlicher Pfad mit sieben Knoten den Wert um höchstens drei erhöht. Dieses lokale Beispiel ist vom Satz über zusammenhängende, anfangs unmarkierte Bäume zu unterscheiden. Bei D7 wurden außerdem die Zuordnung des markierten Knotens im Hilfsgraphen korrigiert und die zuvor vorausgesetzten kleinen Fälle gesondert bewiesen.

## Entdecken und überprüfen

- [Vollständiger Aufsatz (PDF, Englisch)](manuscript/Isolation_Game_Research_Report.pdf) · [Beweisübersicht (Englisch)](EVIDENCE_MAP.md)
- [Forschungsverlauf (Englisch)](RESEARCH.md) · [Anleitung zur Reproduktion (Englisch)](REPRODUCE.md) · [Lean-Quellen und Builds (Englisch)](formal/README.md)
- [Interaktives Spielbrett (Englisch/Chinesisch)](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/index.html) · [D10-Konstruktion (Englisch/Chinesisch)](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/d10.html)
- [Anleitung zum Spielbrett (Deutsch)](demo/README.de.md)
- [Lizenzen und Hinweise (Englisch)](LICENSE_SCOPE.md)


*Redaktion und Pflege des Archivs: Cen Yi (岑弈).*
