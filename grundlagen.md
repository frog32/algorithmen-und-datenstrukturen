1.1. Grundlagen
===============
Definition und Eigenschaften von Algorithmen
--------------------------------------------
Ein Algorithmus ist ein schrittweises Problemlösungsverfahren mit den folgenden Eigenschaften:

1.1.1. Vollständigkeit
------------------
Ein Algorithmus ist eine Beschreibung eines Lösungsverfahrens darf keinen Schritt auslassen und muss alle relevanten Vor- und Rahmenbedingungen berücksichtigen.
1.1.2. Eindeutigkeit
----------------
Jede Aktion muss eindeutig interpretierbar sein. Es darf keinen Interpretationsspielraum geben.
1.1.3. Ausführbarkeit
-----------------
Jede Aktion muss ausführbar sein. Die Art und Weise der Ausführung muss klar sein.
1.1.4. Statische Endlichkeit
------------------------
Der Umfang der Beschreibung eines Algorithmus muss endlich sein, unabhängig von der Notation.
1.1.5. Dynamische Endlichkeit
-------------------------
Ein Algorithmus heisst __abbrechend__ oder __terminierend__ wenn seine Ausführung nach endlich vielen Schritten anhält.
Sonnst heisst der Algorithmus nicht __nicht abbrechend__ oder __nicht terminierend__
1.1.6. Korrektheit
--------------
Ein Algorithmus ist __korrekt__ wenn er für jede Eingabeinstanz mit der richtigen Ausgabe hält.
Ein __inkorrekter__ Algorithmus terminiert nicht oder terminiert mit einer falschen Ausgabe.
1.1.7. Effizienz
------------
Ein Algorithmus soll seinen Zweck unter bestmöglicher Ausnutzung aller beteiligten Ressourcen erfüllen.

1.2. Bestandteile von Algorithmen
=================================
In der __imperativen__ oder prozeduralen Programmierung bestehen Algorithmen aus einer Folge von __Anweisungen__ / __Aktionen__ / __Befehlen__ / __Kommandos__, welche auf __Datenobjekte__ angewandt werden.

1.2.1. Datenobjekte und Datentypen
----------------------------------
Datenobjekte können während der Ausführung eines Algorithmus veränderbar (__Variabeln__) oder unveränderbar (__Konstanten__) sein und besitzen je einen __Datentyp__, welcher ihre __Wertemenge__ und die auf sie anwendbaren __Operationen__ beschreibt.

Ein Datenobjekt heisst __elementar__ (__atomar__) wenn es im logischen Sinne nicht weiter in einzelne Bestandteile zerlegt werden kann. Ein Datenobjekt heisst __strukturiert__, wenn es eine Struktur aufweist und sich logisch aus kleineren Bestandteilen zusammensetzt.

1.2.2. Anweisungen
------------------
    if condition then
         statement sequence 1
    else
        statement sequence 2
    end
    
1.3. Schnittstellen von Algorithmen
===================================
    CalculateFactorial(pfeilabwärts x:int pfeilaufwärts xf:int)
    BinominalCoefficient(pfeilabwärts n:int pfeilabwärts k:int) :int

1.4. Darstellungsformen für Algorithmen
=======================================
- Grafische Darstellungsformen für Algorithmen
    - Ablaufdiagramme
    - Struktogramme / Nassi-Schneiderman-Diagramme
- (UML)
- Text-basierte Darstellungsformen für Algorithmen
    - Stilisierte Prosa
    - Pseudocode

1.5 Algorithmen und Programme
=============================
- Ein Algorithmus kann in verschiedenen Darstellungsformen beschrieben sein. Ein Programm hingegen muss immer in der Sprache des Rechners formuliert sein.
- Ein Programm kann eine Beschreibung eines Algorithmus sein. Es kann sich aber ebenso um eine sinnlose Aneinanderreihung von Operationen handeln.
- Ein Programm kann (unfreiwillig) fehlerhaft sein, auch wenn der zugrundeliegende Algorithmus korrekt ist.
- Von einem Algorithmus spricht man nur im Zusammenhang mit einem Problem.