6 Zufallszahlen
===============

Eine Folge von Zahlen, die als "zufällig" gebildet zu sein scheint, bezeichnet man als **(Pseudo-) Zufallszahlenfolge**. Je nach Anwendungsbereich stellt man an sie verschiedene Anforderungen.

- Wertebereich / Intervall:  
[0 ... m-1]
- Verteilung:  
Gleichverteilung, Normalverteilung, ...
- Unabhängigkeit:  
Das nächste Element einer Folge sollte nicht offensichtlich vorhersagbar sein.

6.1 Algorithmen mit Gedächnis
-----------------------------

            |           |
        ---------------------
        |   |           |   | 
    A1  |   ---> f ------   |
        |                   |
        ---------------------
        
    A1(↓i:... ↑o:...)
    
    
            |           |
        ---------------------
        |   |           |   | 
    A2  |   ---> f ------   |
        |   |    |          |
        ---------------------
        |   |    |          |
        |   |    |          |
        |   |    s <--      |
        |   |    ^   |      |
        |   |    |   |      |
        |   ---> g----      |
        |                   |
        ---------------------
        
    A2(↓i:... ↑o:...)
    o=f(i, s(n))
    s(n+1)=g(i, s(n))
        
Hängen die Ausgangsparameter nicht nur von den Eingangsparametern, sondern auch von den Ergebnissen früherer Aufrufe ab, so handelt es sich um einen **Algorithmus mit Gedächnis**. Das "Gedächnis" wird als **innerer Zustand** mittels **statischer Variablen** realisiert.