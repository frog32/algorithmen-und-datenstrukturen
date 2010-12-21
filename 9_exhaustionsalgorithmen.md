9 Exhaustionsalgorithmen
========================
Unter einem **Exhaustionsalgorithmen** versteht man einen Lösungsansatz durch systematisches Ausprobieren aller Möglichkeiten bzw. durch vollständiges/erschöpfendes Absuchen des gesamten Lösungsraums.

9.1 Problemformulierungen und Lösungsansätze
--------------------------------------------

Gegeben:

*   Ein **n-Tupel** x bestehend aus n **Variablen** x₁ bis xn, wobei jedes xi nur **diskrete** Werte aus einem endlichen **Wertebereich** D annehmen kann.

        x = (x₁,...,xn) mit xi ∈ D ∀ i ∈ {1,...,n}
    
*   Eine oder mehrere **Bedingungen**, die zur Einschränkungen der möglichen Variablenwerte des Tupels führen

Gesucht:

*   Eine bzw. alle möglichen **Belegungen**der Variablen x₁ bis xn, so dass die gegebenen Bedingungen erfüllt sind.

        x → Lösungstupel / Lösungsvektor / Lösungsfeld
        
Beispiel: n-Damen-Problem

*   x = (x₁,...,xn) mit n ≥ 4, xi ∈ {1,...,n} ∀ i ∈ {1,...,n}
    
    Für alle i,j ∈ {1,...,n}, i≠j gilt:
    
    1.  xi ≠ xj (keine gleiche Spalte)
    2.  i-xi ≠ j-xj (keine gleiche Hauptdiagonale)
    3.  i+xi ≠ j+xj (keine gleiche Nebendiagonale)

Gesucht:

* Eine bzw. alle möglichen Wertekombinationen des Lösungsvektors x, so dass die Bedingungen 1 bis 3 erfüllt sind.

Lösungsansatz: **Brute Force**

    Sei k = |D|
                  n
    → k*k*...*k = ∏ k=k^n
                 i=1

Lösungsansatz: **Backtracking** / **Rücksetzverfahren**

    Sei D={a,b,c}, k=3
    → Tiefensuche im Lösungsraum
    

9.2 Standardprobleme
--------------------

**Erfüllbarkeitsproblem / Satisfiability Problem (SAT)**

Gegeben:

*   n Variablen xi vom Typ boolean
*   Logische Ausdrücke mit and, or und not über xi

Gesucht:

*   Belegung der Variablen xi, so dass alle logischen Ausdrücke wahr sind.

**Rundreiseproblem / Traveling Salesman Problem (TSP)**

Gegeben:

*   n Städte mit Abständen d(i,j)>0 ∀ i,j ∈ {1,...,n}, i≠j

Gesucht:

*   kürzeste Rundreise durch alle Städte die in Stadt 1 beginnt und in Stadt 1 endet.

        x1=1, xi≠xj ∀ i,j ∈ {1,...,n}, i≠j
        d(x1,x2)+d(x2,x3)+...+d(xn,x1) ist minimal

**Rucksackproblem / Knapsack Problem**

Gegeben:

*   n Gegenstände mit Gewichten wi > 0 und Werten vi > 0 ∀ i∈ {1,...,n}
*   Maximalgewicht wmax eines Rucksacks

Gesucht:

*   Auswahl von Gegenständen für den Rucksack mit maximalem Wert, ohne das Maximalgewicht zu überschreiten

        x1*w1 + x2*w2 + ... + xn*wn ≤ wmax
        x1*v1 + x2*v2 + ... + xn*vn ist minimal

9.3 Algorithmenschemata für Backtracking
----------------------------------------