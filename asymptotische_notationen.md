2.5 Asymptotische Notationen
============================
O-Notation/Landau-Notation
--------------------------
Seien f:N->R+ und g: N->R+ zwei Funktionen. Dann ist f von der Ordnung g, wenn gilt:

    O(g(n))={f(n)| es existieren positive Konstannten c und n0, so dass 0<=f(n)<=c*g(n)}
    
Man schreibt
    
    f(n)€ O(g(n)) oder f(n)=O(g(n))