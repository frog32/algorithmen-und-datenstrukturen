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
Bei **doppelt-verketteten** Listen bestimmt ein zweiter Zeiger auch den jeweils vorangehenden Knoten (**Vorgänger**).

    →O→O→O
    jedes Element hat einen Pointer auf den Nachfolger
    
    →O←→O←→O←→O
    
    jedes Element hat einen Pointer auf den Nachfolger und einen auf den
    Vorgänger
    
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
**Bäume** repräsentieren Mengen von Knoten, in denen es jeweils genau einen ausgezeichneten Knoten (**Wurzel**) und eine endliche Menge disjunkter Bäume (**Teilbäume**) gibt, die mit der Wurzel verbunden sind.  
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

4.2.4 Komplexitäten
-------------------

    SortedInsert(↓1)    1
    SortedInsert(↓2)     \
    SortedInsert(↓3)      2
    SortedInsert(↓4)       \
    SortedInsert(↓5)        3
    SortedInsert(↓6)         \
    SortedInsert(↓7)          4
                               \
                                5
                                 \
                                  6
                                   \
    h = 6                           7
    
    SortedInsert(↓4)                  4
    SortedInsert(↓2)               /     \
    SortedInsert(↓1)             2         6
    SortedInsert(↓3)           /   \     /   \
    SortedInsert(↓6)          1     3   5     7
    SortedInsert(↓5)
    SortedInsert(↓7)
    
    h=2

Ein **vollständiger Binärbaum** ist ein Binärbaum, in dem jeder Knoten entweder keinen oder genau zwei Nachfolger hat.  
Ein **perfekter Binärbaum** ist ein vollständiger Binärbaum, in dem alle Blätter auf ein und derselben Ebene liegen. Die Anzahl Knoten eines perfekten Binärbaums beträgt 

    2^k -1 für k=h+1
    h = ⎡log(n+1) - 1⎤

Binäre Suchbäume, die eher eine einfachverkettete Liste bilden, bezeichnet man als **degenerierte** binäre Suchbäume.

    LZK: O(h) ≅ O(n)

Binäre Suchbäume, denen die Elemente in zufälliger Reihenfolge zugeführt werden, oder die über Mechanismen verfügen, um Degenerationen zu vermeiden, bezeichnet man als balancierte oder als ausgeglichene binäre Suchbäume.
    
    LZK: O(h) ≅ O(log n)
    
4.3 Stapel
==========

**Stapel** / **Kellerspeicher** / **Stacks** repräsentieren eine Datenstruktur, in der das jeweils letzte eingefügte Datenobjekt wieder als erstes entnommen wird. Stapel implementieren somit eine **Last In - First Out Strategie (LIFO)**.  
Für das **Einkellern** sieht man in der Regel eine Methode **push**, für das **Auskellern** eine Methode **pop** vor. Um festzustellen, ob der Kellerspeicher leer bzw. voll ist, verwendet man eine Methode **isEmpty** bzw **isFull**.

    var e:int
    Push(↓1)
    Push(↓2)
    Push(↓3)
    while not IsEmpty() do
        Pop(↑e)
        Write(↓e)
    end
    
    3 2 1

4.4 Warteschlangen
==================

**Warteschlangen** / **Queues** repräsentieren eine Datenstruktur, in der das jeweils erste eingefügte Datenobjekt auch wieder als erstes entnommen wird. Warteschlangen implementieren somit eine **First in - First out Strategie (FIFO)**.  
Für das **Einreiehn** / **Einbringen** sieht man in der Regel eine Methode **enqueue**, für das **Entfernen** eine Methode **dequeue** vor. Um festzustellen, ob die Warteschlange leer bzw. voll ist, verwendet man eine Methode **isEmpty** bzw. **isFull**.

    var e:int
    Enqueue(↓1)
    Enqueue(↓2)
    Enqueue(↓3)
    while not IsEmpty() do
        Dequeue(↑e)
        Write(↑e)
    end
    
    1 2 3
    