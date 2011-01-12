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
    
    A.L.K: O(plen*sLen)
    
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
    next:   | 0 | 1 | 1 | 1 | 2 | 3 |
            -------------------------