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