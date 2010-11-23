7 Suchalgorithmen
=================
In der Regel sucht man komplexe Datenobjekte anhand charakteristischer Merkmale / Attribute. Ein komplexes Datenobjekt besteht daher meist aus einem **Schlüssel** / **key** und **(Sateliten-)Daten**.

    type ListNotePtr = →compound
        next: ListNodePtr
        key: keyType
        data1: DataType1
        data2: DataType2
        ...
        dataN: DataTypeN
    end
    
Implementierung in Java:  

1. Implementiere equals/hashCode/compareTo über die Klassenattribute des Schlüssels.
2. "Baue" ein Objekt mit den entsprechenden Schlüsselattributen nach.
3. Suche und vergleiche Objekte mittels equals/compareTo

7.1 Sequenzielle Suche
----------------------
Bei der **sequenziellen** oder **linearen Suche** werden die Elemente einer Datenstruktur als eine lineare Anordnung (Sequenz) betrachtet und elementweise durchsucht, bis das gesuchte Element gefunden wurde oder kein weiteres Element mehr vorhanden ist.

7.2 Binäre Suche
----------------
Bei der binären Suche müssen die Elemente der Datenstruktur sortiert und ein direkter Zugriff auf das "mittlere" Element möglich sein.  
Nach dem Prinzip **Teile und Herrsche** (**divide and conquer**) wird bei nicht übereinstimmendem Schlüsselwert mit dem mittlerem Element rekursiv in einer der linken oder rechten Hälfte der Datenstruktur weitergesucht.

7.3 Hashing- basierte Suche
---------------------------
Beim **Hashing** ("Zerhacken") oder bei der **Streuspeicherung** handelt es sich um ein Verfahren, bei dem einzelne Datenobjekte in einem Array so abgelegt werden, dass sie mit dem Suchschlüssel als eine Art Feldindex auf Anhieb gefunden werden können.

    Asymptotische Laufzeitkomplexität: O(1)
    
7.3.1 Grundprinzip
------------------

*   Idee: Suchschlüssel direkt als Feldindex  
*   Beispiel:  Schweizer Sozialversicherungsnummer

        756.XXXX.XXXX.XY
        →10^9 Elemente / Indizes
        7'785'800 Einwohner
        → ~0.8% Belegung in einem Feld

*   Lösung: Transformation
    1.  Hash-Funktion
        
            h:K→N
            mit K: Schlüsselmenge mit n Schlüsseln
    
    2.  Transformation
    
            N→I
            mit I: Indexbereich 0...m-1
    
    3.  Hash-Tabelle
    
            mit m Feldelementen
            (assoziativer Speicher)

7.3.2 Hash-Funktionen und Kollisionen
-------------------------------------
Eine Hash-Funktion h(k) mit beiden Transformationen h:K→N→I = K→I muss folgende Anforderungen erfüllen:

*   **gleichmässige** Verteilung der Schlüsselmenge über den **gesammten** Indexbereich
*   etwa n/m Schlüssel pro Index
*   "zufällige" Verteilung der Schlüssel auf die Indizes, ohne Muster
*   effizient berechenbar, unabhängig von n

Da es in der Regel mehr Schlüssel als Indizes gibt (|k|>>|I|), werden unterschiedliche Suchschlüssel k1 und k2 mit k1≠k2 auch auf den gleichen Hash-Code abgebildet:

    h(k1) = h(k2)

Mann nennt dies **Kollision**.

7.3.3 Kollisionsbehandlung durch Verkettung
-------------------------------------------

Alle Datenobjekte deren Schlüsselwerte auf den selben Index in der Hash-Tabelle abgebildet werden, werden in einer einfach verketteten Liste "gesammelt" und im entsprechenden Element der Hash-Tabelle verankert. Den Faktor α=n/m bezeichnet man als **Auslastung**, **Belegungs-** oder **Füllfaktor**. (Java: α=0.75)  
Die durchschnittliche Anzahl Suchschritte bei nichtdegenerierten Hash-Tabellen beträgt

    Savg = 1+ α/2
    Asymptotische LZK: O(1)
    