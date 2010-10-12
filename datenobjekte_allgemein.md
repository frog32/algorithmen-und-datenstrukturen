3.2 Datenobjekte allgemein
==========================

Man unterteilt **nicht-elementare** Datenobjekte in **strukturierte** Datenobjekte und **dynamische** oder **vernetzte** Datenobjekte.

3.2.1 Strukturierte Datenobjekte
================================

**Felder** **Arrays** bestehen aus einer fixen Anzahl von **Elementen** gleichen Datentyps. Auf sie kann mittels **Index i** und **Indexoperator a[i]** zugegriffen werden.

    var a:array[first:last] of ElementType
    
                    |                   a                       |
                -----------------------------------------------------
    Hauptspeicher   |   1   |   2   |   3   |     ...   |   10  |
                ----------------------------------------------------
                    ^           indizes
                    |
                start
                adresse
    
    Speicherabbildungsfunktion:
    
    AddrOf(↓a[i]) = AddrOf(↓a) + (i-first) * elementSize