4 Datenstrukturen
=================
Entfernen und Einfügen von Elementen in einem Feld:

          ↑                               ↓
    -------------------------       -------------------------
    |   |   | ← | ← | ← | ← |       |   | → | → | → | → | → |
    -------------------------       -------------------------
    
    jedes element umkopieren

    Günstigster Fall:   Smin(n)=1
    Ungünstigster Fall: Smax(n)=n
    
    → Asymptotische LZK: O(n)
    
4.1 Verkettete Listen
---------------------
**Verkettete Listen** repräsentieren eine sequentielle Anordnung von **Knoten** / Elementen, deren Reihenfolge explizit durch Verkettung festgelegt ist.  
Bei **einfach-verketteten** Listen bestimmt ein Zeiger den jeweils nächsten Knoten (**Nachfolger**).  
Bei **doppelt-vertetteten** Listen bestimmt ein zweiter Zeiger auch den jeweils vorangehenden Knoten (**Vorgänger**).

    →O→O→O
    jedes Element hat einen Pointer auf den Nachfolger
    
    →O←→O←→O←→O
    
    jedes Element hat einen Pointer auf den Nachfolger und einen auf den Vorgänger
    
Den Listenknoten ohne (logischen) Vorgänger bezeichnet man als **Kopf**, den **Rest** der Liste als **Schwanz**. Die Listenknoten ohne Nachfolger bezeichnet man als **Ende** der Liste. Sind Kopf und Ende mittels Zeiger verbunden, so ist die Liste **zirkulär** / **zyklisch**.

4.1.1 Einfach-verkettete Listen
-------------------------------
Siehe Arbeitsblätter

4.1.2 Doppelt-verkettete Listen
-------------------------------
Zur Vereinfachung der Listenverarbeitungsalgorithmen bei doppelt-verketteten Listen lässt sich ein **Anker** / **Wächter** einsetzen. Ausgehend von diesem Ankerknoten können alle Listenknoten sowohl von vorne weg als auch von hinten her besucht werden.

4.2 Bäume
---------
4.2.1 Allgemeine Bäume
----------------------
**Bäume** repräsentieren Mengen von Knoten, in denen es jeweils genau einen ausgezeichneten Knoten (**Wurkel**) und eine endliche Menge disjunkter Bäume (**Teilbäume**) gibt, die mit der Wurzel verbunden sind.  
Jeder Knoten eines Baumes hat höchstens einen **Vorgänger** aber beliebig viele **Nachfolger**. Knoten ohne Nachfolger bezeichnet man als **Blätter**. Die Höhe eines Baums ist die Länge des Wegs beziehungsweise die Anzahl Verbindungen von der Wurzel bis zum Blatt auf der höchsten Ebene.

                                X           Ebene 0
    X = Wurzel               /  |  \        
    + = innere Knoten       +   O   +       Ebene 1
    O = Blätter           / | \    / \
                         O  O  O  O   O     Ebene 2
    höhe = 2

4.2.2 Binärbäume
----------------
Binärbäume sind Bäume in denen jeder Knoten maximal zwei Nachfolger hat. Man bezeichnet die beiden Nachfolger als linken und rechten Nachfolger.  
Jeder Baum lässt sich in einen Binärbaum transformieren.

4.2.3 Binäre Suchbäume
----------------------
**Binäre Suchbäume** sind Binärbäume, in denen für alle Knoten die Werte der Datenkomponenten aller linken Nachfolger **kleiner** und die Werte aller rechten Nachfolger **grösser oder gleich** dem Wert des betrachteten Knotens sind.

    2 3 5 7
    
                5               3           2
              /   \           /   \           \
             3     7         2     7           3
           /                     /               \
          2                     5                 5
                                                    \
                                                     7