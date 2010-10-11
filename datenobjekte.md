3 Datenobjekte
==============
3.1 Datenobjekte in Java
------------------------
Für Datenstrukturen in Java ist es unerlässlich, für alle Datentypen welche als Elemente in Frage kommen (Wertklassen) die folgenden gemeinsamen Methoden gemäss Spezifikationen richtig zu implementieren bzw. zu überschreiben.

3.1.1 Object.equals
-------------------

    public boolean equals(Object o)

Die equals-Methode definiert die Gleichheit zweier Objekte und muss

*   reflexif
*   symetrisch
*   transitiv
*   konsistent
*   nicht null

sein.

3.1.2 Object.hashCode
---------------------

    public int hashCode()
    
Die hashCode-Methode berechnet eine Art **Fingerabdruck** eines Objekts und

*   muss überschrieben werden, wenn equals überschrieben wurde
*   muss bei Gleichheit zweier Objekte (gem. equals) die gleichen Werte zurück geben
*   darf bei Ungleichheit zweier Objekte (gem. equals) die selben Werte zurück geben

3.1.3 Object.toString
---------------------

    public String toString()
    
Die toString-Methode soll eine anschauliche **String-Darstellung** eines Objekts zurückgeben.

3.1.4 Compareable<T>.compareTo
------------------------------
    
    public int compareTo(T o)

Die compareTo-Methode definiert die Reienfolge zweier Objekte und muss

*   asymetrisch
*   transitiv
*   konsistent mit equals

sein.