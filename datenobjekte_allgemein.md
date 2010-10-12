3.2 Datenobjekte allgemein
==========================

Man unterteilt **nicht-elementare** Datenobjekte in **strukturierte** Datenobjekte und **dynamische** oder **vernetzte** Datenobjekte.

3.2.1 Strukturierte Datenobjekte
================================

**Felder** / **Arrays** bestehen aus einer fixen Anzahl von **Elementen** gleichen Datentyps. Auf sie kann mittels **Index i** und **Indexoperator a[i]** zugegriffen werden.

    var a:array[first:last] of ElementType
    
                    |                   a                       |
                ----------------------------------------------------
    Hauptspeicher   |   1   |   2   |   3   |     ...   |   10  |
                ----------------------------------------------------
                    ^           indizes
                    |
                start
                adresse
    
    Speicherabbildungsfunktion:
    
    AddrOf(↓a[i]) = AddrOf(↓a) + (i-first) * elementSize
    
    mit elementSize = sizeOf(↓ElementType)

**Verbunde** / **Structures** / **Records** / **Compounds** bestehen aus einer fixen Anzahl von **Komponenten**, welche unterschiedliche Datentypen haben dürfen.

    var c = compound
        a: TypeA
        b: TypeB
        ...
        z: TypeZ
    end
    
Auf sie kann mittels **Name n** und **Komponentenselektionsoperator c.n** zugegriffen werden.
    
    
                    |                       c                     |
                ----------------------------------------------------
    Hauptspeicher   |   c.a     | c.b |    ...   |      c.z       |
                ----------------------------------------------------
                    ^           c
                    |
                start
                adresse

3.2.2 Dynamische Datentypen
---------------------------

**Dynamische** / **verkettete** Datenobjekte können während ihrer Lebensdauer nicht nur ihre **Werte**, sondern auch ihre **Struktur** und damit ihre **Grösse** ändern.

Auf ihre Bestandteile kann mittels **Zeiger** / **Pointer** / **Referenz** und eines **Dereferenzierungsoperator →** zugegriffen werden.

**Allotiation** und **Freigabe** des benötigten Speicherplatzes erfolgt auf dem **dynamischen Speicherbereich** / **Heap**.

    var intPtr: →int
    intPtr := New(↓int)
    Write(↓intPtr)      ⇒Speicheradresse
    intPtr→ := 17
    Write(↓intPtr→)     ⇒17
    Dispose(↓intPtr)    ⇒Pointer zeigt immer noch auf die selbe Adresse
    intPtr := null      ⇒Pointer zeigt nirgends mehr hin (nullPointer exception)

