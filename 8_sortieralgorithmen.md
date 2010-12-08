8 Sortieralgorithmen
====================
Wie bei den Suchalgorithmen unterscheidet man bei komplexen Datenobjekten zwischen **(Sortier-)Schlüsseln** und **(Satelliten-)Daten**. Die Sortierschlüssel müssen eine Vergleichsoperation < oder > erlauben.  
Ein Sortieralgorithmus wird als **stabil** bezeichnet, wenn die relative Reihenfolge von Datenobjekten mit gleichem Schlüsselwert durch den Sortiervorgang unverändert bleibt, ansonsten heisst er **instabil**.

8.1 Auswahlsortieren / Selection Sort
-------------------------------------
Beim **Auswahlsortieren**/**selection sort**/**minimum sort** wird das jeweils kleinste Element aus dem noch zu sortierenden Feld ermittelt und mit dem jeweils ersten Element vertauscht.  
Es handelt sich um einen instabilen Sortieralgorithmus.

    Laufzeitkomplexität:
    
    Anzahl Schlüsselvergleiche:
        Scmp(n)=n(n-1)/2 ≈ n^2/2
        
    Anzahl Zuweisungen:
    
        S(n) = 3* (n-1)
        
    Total:
        
        S(n^2)
        
8.2 Einfügesortieren / Insertion Sort
-------------------------------------
Beim **Einfügesortieren**/**insertion sort** wird ähnlich wie beim Kartenspielen das jeweils nächste unsortierte Element an der richtigen Stelle im Sortierten Bereich eingefügt.  
Es handelt sich um einen stabilen Sortieralgorithmus.

    Laufzeitkomplexität:
    
    Günstigster Fall:
        
        Anzahl Schlüsselvergleiche:
            Scmp(n)=n-1

8.3 Shell-Sortieren / Shell Sort
--------------------------------
Beim **Shell-Sortieren**/**Shell sort** wird das Feld jeweils so "vorsortiert", dass eine abschliessende Endsortierung mittels Einfügesortieren ohne grosse Verschiebungsdistanzen vorgenommen werden kann. Die Vorsortierung wird schrittweise mit Hilfe des Einfügesortierens auf h disjunkten Teilfeldern vorgenommen, bei denen zwei benachbarte Elemente i und j den Abstand h voneinander haben.

    Laufzeitkomplexität:
    hs = 2^k
    32, 16, 8, 4, 2, 1
    O(n^2)


8.5 Quick Sort
--------------
Beim **Quick Sort** wird nach der Strategie Teile und Herrsche das zu sortierende Feld abhängig von einem **Pivotelement x** in zwei Teilfelder aufgeteilt, so dass im linken TeilFeld alle Elemente ≤ x und im rechten Teilfeld alle Elemente ≥ x sind. Diese Teilfelder werden anschliessend rekursiv nach dem gleichen Prinzip weiter aufgeteilt.  
Es handelt sich um einen instabilen Sortieralgorithmus.

       -------------------------
    a: |  |  |  |  |  |  |  |  |
       -------------------------
                   |
            ≤ x          ≥ x

    Laufzeitkomplexität:

    Günstigster Fall:
        Anzahl Schlüsselvergleiche:
            Scmp(n)=n*log(n)
        
        Ungünstigster Fall:
            Scmp(n)=n^2
            
        Durchschnittlicher Fall:
            Scmp(n)=c*n*log(n)

8.6 Heap Sort
-------------
8.6.1 Heap-Datenstruktur
------------------------
Ein **Heap** (≠ dynamischer Speicherbereich) ist eine Datenstruktur, die:

*   Zugriff auf das grösste Element in O(1)
*   einfügen eines Elements in O(log(n))
*   entfernen des grössten Elements in O(log(n))

erlaubt.  
Er kann als **kompletter Binärbaum** (d.h. perfekt ausser der "letzten Ebene rechts") oder als Feld realisiert werden.  

*   Implementierung als kompletter Binärbaum:
    *   Die Wurzel eines Heaps ist grösser oder gleich all ihrer Nachfolger.
*   Implementierung als Feld h[1...n]:
    *   Die **Wurzel** ist h[1]
    *   Der **linke Nachfolger** eines Elements h[i] ist h[2*i]
    *   Der **rechte Nachfolger** eines Elements h[i] ist h[2*i+1]
    *   Der Vorgänger des Elements h[i] ist h[i/2]
    *   Für alle h[i] mit i ≠ 1 gilt:
        *   h[i] ≤ h[i/2]
        
Abbildung im Speicher als Baum oder als Feld
    
             13
           /    \
         11      7
        /  \    /
       3    2  5
    
    -------------------------------    
    | 13 | 11 |  7 |  3 |  2 |  5 |
    -------------------------------

8.6.2 Heap-Sortieren
--------------------
Beim **(Top-Down-)Heap-Sortieren** werden in zwei Phasen zuerst alle Elemente des zu sortierenden Felds mittels Insert der Reihe nach in einen schrittweise anwachsenden Heap eingetragen und anschliessend alle Elemente dem Heap mittels RemoveMax entnommen und von hinten her in das dann sortierte Feld eingetragen.  Es handelt sich um einen instabilen Sortieralgorithmus.