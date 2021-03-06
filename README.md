# Prosty system księgowy/magazyn

### Napisz program (accountant.py), który będzie rejestrował operacje na koncie firmy i stan magazynu.

Program jest wywoływany w następujący sposób:
1. python accountant.py saldo <int wartosc> <str komentarz>
2. python accountant.py sprzedaż <str identyfikator produktu> <int cena> <int liczba sprzedanych>
3. python accountant.py zakup <str identyfikator produktu> <int cena> <int liczba zakupionych>
4. python accountant.py konto
5. python accountant.py magazyn <str identyfikator produktu 1> <str identyfikator produktu 2> <str identyfikator produktu 3> ...
6. python accountant.py przegląd

### Działanie programu będzie zależne od podanych argumentów
Niezależnie od trybu program zawsze będzie działał w następujący sposób
**I.** Program pobierze rodzaj akcji (ciąg znaków). Dozwolone akcje to **"saldo", zakup", "sprzedaż"**. Jeśli użytkownik wprowadzi inną akcję, program powinien zwrócić błąd i zakończyć działanie.

**saldo:** program pobiera dwie linie: zmiana na koncie firmy wyrażona w groszach (int) (może być ujemna) oraz komentarz do zmiany (str)

**zakup:** program pobiera trzy linie: identyfikator produktu (str), cena jednostkowa (int) i liczba sztuk (int). Program odejmuje z salda cenę jednostkową pomnożoną przez liczbę sztuk. Jeśli saldo po zmianie jest ujemne, cena jest ujemna bądź liczba sztuk jest mniejsza od zero program zwraca błąd. Program podnosi stan magazynowy zakupionego towaru

**sprzedaż:** program pobiera trzy linie: identyfikator produktu (str), cena jednostkowa (int), liczba sztuk (int). Program dodaje do salda cenę jednostkową pomnożoną razy liczbę sztuk. Jeśli na magazynie nie ma wystarczającej liczby sztuk, cena jest ujemna bądź liczba sztuk sprzedanych jest mniejsza od zero program zwraca błąd. Program obniża stan magazynowy zakupionego towaru.

**stop:** program przechodzi do kroku **IV**

**II.** Program zapamiętuje każdą wprowadzoną linię

**III.** Program wraca do kroku **I**

**IV.** W zależności od wywołania:

1., 2., 3., program dodaje do historii podane argumenty tak, jakby miały być wprowadzone przez standardowe wejście, przechodzi do kroku **V**

4. program wypisuje na standardowe wyjście stan konta po wszystkich akcjach, kończy działanie 

5. program wypisuje stany magazynowe dla podanych produktów, w formacie: <id produktu>: <stan> w nowych liniach i kończy działanie:
6. Program wypisuje wszystkie akcje zapisane pod indeksami w zakresie [od, do] (zakresy włącznie)

**V.** Program wypisuje wszystkie podane parametry w formie identycznej, w jakiej je pobrał.
