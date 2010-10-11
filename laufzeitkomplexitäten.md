2 Laufzeitkomplexitäten
=======================
2.1 Laufzeitkomplexitäten und Problemgrösse
===========================================

Unter __komplexität__ versteht man den für die Ausführung eines Algorithmus erforderlichen Aufwand, z.B:

- __Speicherkomplexität__: Speicherbedarf
- __Laufzeitkomplexität__: Laufzeit / Rechenzeit
- __Problemkomplexität__: Minimale Laufzeitkomplexität eines Problems

Komplexitäten eines Algorithmus sind abhängig von einer oder mehreren Grössen, z.B:

- Anzahl Elemente einer Matrix
- Grad eines zu berechnenden Polynoms
- Länge eines zu bearbeitenden Texts

__Eine__ das Problem charakterisierende (Gesamt-)Grösse bezeichnet man als __Problemgrösse n__.

Die __Laufzeit t__ ist eine Funktion der Problemgrösse n.

    t=f(n)

2.2 Laufzeitmessung
===================
2.2.1 Laufzeitmessung über Systemzeitgeber
------------------------------------------

    startTime := CurrentTime()
    Algorithm()
    stopTime := CurrentTime()
    duration := stopTime - startTime

    Zeitgeber in Java:
    System.currentTimeMillis()
    System.nanoTime()

2.2.2 Einflussfaktoren
----------------------

- **Hardware**:
    - Systemzeitgeber
    - Prozessor(en)
    - Arbeitsspeicher und Zwischenspeicher (Cache)
    - ...
- **Betriebssystem**: 
    - Andere Anwendungen und Systemprozesse
    - Sicherheitseinstellungen, virtueller Speicher
- **Programmiersprachen und Bibliotheken**:
    - Interpretation
    - Bytecode
    - Maschinencode
- **Compiler**:
    - Optimierungen
    - Laufzeitprüfungen
    - Garbage Collector
    - ...

2.2.3 Verteilung der Laufzeiten im Programmcode
-----------------------------------------------

10% des Codes sind für 90% der Laufzeit verantwortlich.  
1% des Codes sind für 50% der Laufzeit verantwortlich.

2.3 Laufzeitberechnung - Feinanalyse
====================================

Bei der **Feinanalyse** betrachtet man einen Algorithmus auf der Ebene einzelner Aktionen.  
Jede elementare Operation verfügt dabei über einen **relativen Zeitaufwand**.

Definiere Problemgrösse `n = sqrt(n1*n2)`

2.4 Laufzeitberechnung - Grobanalyse
====================================

Bei der **Grobanalyse** betrachtet man nur die Teile eines Algorithmus, welche das Laufzeitverhalten signifikant beeinflussen. Man unterscheidet je nach Eingabe/Inhalt zwischen drei Fällen:

- **günstigster Fall** (best case)
- **ungünstigster Fall** (worst case)
- **durchschnittlicher Fall** (average case)

Beispiel: Bearbeitung einer Dreiecksmatrix
------------------------------------------

    for i := 1 to n
        for j := 1 to i
            A(matrix[i,j])
        end
    end
    
Algorithmus A wird 1+2+3+4...+n ausgeführt `(n+1)n/2 = (n^2 + n) / 2` --> Laufzeit steigt mit dem Quadrat der Matrizengrösse n.