5 Rekursive Algorithmen
=======================

Unter **Rekursion** / **Rekursivität** / **Rekurrenz** versteht man, dass sich etwas direkt oder indirekt auf sich selbst bezieht.

5.1 Standartbeispiele
---------------------
5.1.1 Fakultät
--------------

Definition: n! = 1*2*...*(n-1)

Iterativer Algorithmus:

    FactorialIterative(↓n:int):int
        var f:int
        var i:int
        begin
            f:=1
            for i:=2 to n do
                f:=f*i
            end
    end FactorialIterative
    
Rekursive Definition: 

    Factorial(↓n:int):int
    begin
        if n<=1 then
            return 1
        else
            return n*Factorial(↓n-1)
        end
    end Factorial

Bei der Fakultät handelt es sich um eine **Lineare** Rekursion

5.1.2 Fibonacci-Zahlen
----------------------

Rekursive Definition:
    
    f(0)=0
    f(1)=1
    f(n)=f(n-1)+f(n-2)
    
    1,1,2,3,4,8,13,21,34,55,89
    
    Fibonacci(↓n:int):int
    begin
        if n<=1 then
            return n
        else
            return Fibonacci(↓n-1)+Fibonacci(↓n-2)
        end
    end Fibonacci
    
    Fibonacci(↓)

Bei der rekursiven Berechnung der Fibonacci-Zahlen handelt es sich um eine **nicht-lineare** oder **Baumrekursion**.

5.2 Ausführung und Terminierung
-------------------------------

Beim Aufruf eines Algorithmus / Funktion wird jeweils ein eigener **Aktivierungssatz** im **Laufzeitkeller** angelegt.  
Der Aktivierungssatz enthält die Parameter und Variablen des aufgerufenen Algorithmus.  
Wenn die Ausführung eines Algorithmus endet, wird sein Aktivierungssatz aus dem Laufzeitkeller ausgekellert.  
Jeder rekursive Algorithmus muss mindestens einen nicht rekursiven Zweig haben sonnst terminiert der Algorithmus nicht.
(stack overflow)

5.3 Rekursion und Iteration
---------------------------

Prinzipiell lässt sich jeder rekursive Algorithmus in einen iterativen Algorithmus umwandeln. (**Entrekursivierung**) In der Regel sind bei den iterativen Algorithmen jedoch eigene Kellerspeicher erforderlich.  
Ausnahme: **primitive Rekursion** / **Endrekursion**  
Der einzige rekursive Aufruf bildet die letzte Aktion des Algorithmus.

    RecursiveAlgoritm(...)
    ..
    begin
        if condition then
            A
        else
            B
            RecursiveAlgoritm(...)
        end
    end RecursiveAlgoritm
    
    
    IterativeAlgorithm(...)
    ...
    begin
        while not condition do
            B
        end
        A
    end IterativeAlgorithm

Jeder iterative Algorithmus lässt sich in einen rekursiven Algorithmus transformieren.  
(**Rekursivierung**)

    IterativeAlgorithm(...)
    ..
    begin
        A
        while condition do
            B
        end
        C
    end IterativeAlgorithm
    
    
    Algorithm(...)
    begin
        A
        RecursiveAlgoritm(...)
        C
    end Algorithm
    
    RecursiveAlgoritm(...)
    begin
        if condition then
            B
            RecursiveAlgoritm(...)
        end
    end RecursiveAlgoritm
    
5.4 Rekursive Algorithmen auf binären (Such-) Bäumen
----------------------------------------------------

Knoten eines Binärbaums als rekursive Datenstruktur:

    type TreeNodePtr = →compound
        left: TreeNodePtr
        right: TreeNodePtr
        ...
    end
    
    PreOrder(↓tree:TreeNodePtr)
    begin
        if tree != null then
            Write(↓tree→data)
            PreOrder(↓tree→left)
            PreOrder(↓tree→right)
        end
    end PreOrder
    
    => 4 2 1 3 6 5 7

    InOrder(↓tree:TreeNodePtr)
    begin
        if tree != null then
            InOrder(↓tree→left)
            Write(↓tree→data)
            InOrder(↓tree→right)
        end
    end PreOrder
    
    => 1 2 3 4 5 6 7

    PostOrder(↓tree:TreeNodePtr)
    begin
        if tree != null then
            PostOrder(↓tree→left)
            PostOrder(↓tree→right)
            Write(↓tree→data)
        end
    end PostOrder
    
    => 1 3 2 5 7 6 4
            