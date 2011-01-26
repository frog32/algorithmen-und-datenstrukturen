10 Mustersuchalgorithmen
========================
10.1 Repräsentation von Zeichenketten
-------------------------------------
**Zeichenketten/Strings** bestehen grundsätzlich aus einem eindimensionalen Array von Zeichen/Characters.

        |                       sLen                        |
        ---------------------------------------------------------
    si  | H | e | l | l | o | , |   | W | o | r | l | d | ! |   |
        ---------------------------------------------------------
        fist                          i                 sLast

first gibt den Indexwert des ersten Zeichens an. (Pascal:1 C/C++/C#/Java:0)

Es gilt: 

    sLen = sLast - first + 1
    sLast = first + sLen -1
    
10.2 Elementare Mustersuchalgorithmen
-------------------------------------
10.2.1 Mustersuche in Zeichenketten
-----------------------------------
Gegeben:

*   Zwei nicht-leere Zeichenketten s (**Zeichenkette**/**string**) und p(**Musterkette**/**pattern**) mit `0 < pLen ≤ sLen ≤ max`

Gesucht:

*   Startposition pos des ersten vollständigen Auftretens von p in s, so dass gilt: `s[pos : pos1 + pLen - 1] = p[first: pLast]`
*   `pos = first - 1`, wenn p nicht in s vorkommt.

10.2.2 Brute Force-Mustersuche
------------------------------

Laufzeitkomplexität:

    Smin(sLen,pLen) = pLen
    Smax(sLen,pLen) = pLen * (sLen - pLen + 1)
    Savg(sLen,pLen) ~ pLen + sLen
    
    A.L.K: O(plen+sLen)
    
10.3 Mustersuchalgorithmen nach Knuth, Morris und Pratt
-------------------------------------------------------
Beim **KMP-Algorithmus** wird die mussterkette wie gewohnt mit der Zeichenkette verglichen. Im Falle einer **Nichtübereinstimmung** kann aufgrund der Bekanntheit der bereits verglichenen Inhalte das Muster jedoch weiter relativ zur mismatch-Position verschoben werden.

                                    | i
        -----------------------------------------
    s:  |   |   |   | a | b | c | d | 0 |   |   |
        -----------------------------------------
                                    | fehler
                    ---------------------
    p               | a | b | c | d | e |
                    ---------------------
                                    |
    p neu                           ---------------------
                                    | a | b | c | d | e |
                                    ---------------------
                                    

                                    | i
        -----------------------------------------
    s:  |   |   | a | b | c | a | b | 0 |   |
        -----------------------------------------
                                    | fehler
                -------------------------
    p           | a | b | c | a | b | d |
                -------------------------
                                    |
    p neu                   -------------------------        
                            | a | b | c | a | b | d |
                            -------------------------

Das Feld next gibt für jede missmatch-Position j in der Musterkette p denjenigen Indexwert next[j] an, der sich ergibt, wenn man p so weit wie möglich nach rechts verschiebt. next[first] wird auf first -1 gesetzt.

Ermittlung der Elemente des next-Felds:

            -------------------------
    p:      | a | b | c | a | b | d |
            -------------------------
            -------------------------
    next:   | 0 | 1 | 1 | 0 | 1 | 3 |
            -------------------------


10.4 Mustersuchalgorithmus nach Robin und Karp
----------------------------------------------
Beim **Mustersuchalgorithmus nach Robin und Karp** werden die Hash-Codes hp für die Musterkette p und von vorne weg alle Hash-Codes hs für alle Teilketten von s mit der Länge pLen berechnet und verglichen.

            |       pLen        |
            ---------------------
    p:      |                   |
            ---------------------

                    |   plen    |
            ----------------------------------
    p:      |       |           |            |
            ----------------------------------


Als Hash-Funktion wird jedes Zeichen eines Strings als Zahl zur Basis d interpretiert und durch Anwendung des **Horner-Schemas** zu einem numerischen Gesamtwert berechnet.

Beispiel:
    
    Zeichenkette "AuD" (ISO-8859-1/Latin 1)
    
    => d=256
    
    Num("AuD")
    =((Int(↓'A')*256+Int(↓'u'))*256+Int('D'))
    =(65*256+117)*256+68
    
Implementierung in Pseudocode:

    var hp:int
        i:int
    begin
        hp:=0
        for i=first to pLast do
            hp:=(hp*d + Int(↓p[i])) mod q
        end
    end
    
Berechnung des Hash-Codes für die Position i+1:

    Num(s[i:i+pLen-1]) =    s[i] * d^(pLen-1) +
                            s[i] * d^(pLen-2) +
                            ... +
                            s[i+pLen-1]
                            
    Num(s[i+1:i+pLen]) =
                            (Num(s[i:i+pLen -1])-s[i]*d^(pLen-1))*d
                            + s[i+pLen]

Implementierung in Pseudocode:

    dp = d^(pLen-1)
    hs := (hs - Int(↓s[i])*dp) mod q
    => Problem: evtl. negative Zahlen
    hs := (hs + d*q - Int(↓s[i])*dp) mod q
    hs := (hs * d + Int(↓[i+pLen])) mod q
    
Laufzeitkomplexität:

    A.L.K:  O(pLen+sLen)    (durchnittlich)
            o(pLen*sLen)    (theoretisch bei Degeneration)
    