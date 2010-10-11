Anzahl Suchschritte: s(n)=1+Anzahl Schleifendurchläufe

Günstigster Fall: S min(n)=1  
Ungünstigster Fall: S max(n)=1+(n-1)=n  

    Estes Auftreten     Warscheinlichkeit       Anzahl
    von "3"                                     Schleifendurchläufe
    -------------------------------------------------------------------
    Pos. 1              1/3                     0
    Pos. 2              2/9                     1
    ...
    Pos. i              (2/3)^(i-1)*1/3         i-1
    gar nicht           (2/3)^n                 n-1

Durchschnittlicher Fall: `S avg(n)=1+sum(i=1;n;(2/3)^(i-1)*1/3*(i-1))+(2/3)^n*(n-1)=3-3*(2/3)^n`  
limes n->unendlich = 3