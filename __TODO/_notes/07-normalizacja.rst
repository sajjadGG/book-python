Normalizacja
============


* CSV, arkusze Excel a także Pandas DataFrame to przykłady tabel 2 wymiarowych
* Wszystkie problemy o których mówimy wynikają z tego, że odwzorowujemy świat n-wymiarowy w przestrzeni dwuwymiarowej



Praktyka
--------
* Relacje wyglądają pięknie... ale na papierze
* ... w praktyce relacji mało się używa
* znormalizowane dane wyglądają pięknie, mamy mnóstwo tabelek, relacje, nie powtarzających się danych...
* stosując relacje likwidujemy powtarzanie danych
* Powoduje to zachowanie spójności przy update
* jak często robisz update w stosunku do select
* Robienie kolejnych postaci normalnych zmniejsza zapotrzebowanie na storage
* Robienie kolejnych postaci normalnych zwiększa zapotrzebowanie na computing power
* w trzeciej dekadzie XXI wieku, koszt storage jest bardzo mały, natomiast computing power jest drogi
* Dlatego tryumfy zaczęły święcić bazy NoSQL
