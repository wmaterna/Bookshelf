# Bookshelf

Dokumentacja Projektu 
Weronika Materna
Kurs: Język Python



##Projekt Bazy Książek

###Cel projektu:
Zaimplementowanie Bazy Książek, aby potencjalny użytkownik miał 
możliwość zapisania i odczytywania książek.
###Opis
Rolę Bazy Danych pełni plik o rozszerzeniu json, z którego czytane i  do którego zapisywane są pozycje. 
Użytkownik ma możliwość wylistowania wszystkich książek znajdujących się w Bazie, wyszukania konkretnej pozycji, 
dodania nowej pozycji, usunięcia a także wyszukania określonej książki dzięki połączeniem z GoogleAPI.
###Użycie API
API z którego korzysta projekt to [GoogleBooksAPI](https://developers.google.com/books)
###Projket składa się z 4 plików
* itemsData.json - przechowujące pozycje
* interface.py - zarządzający komunikacją pomiędzy użytkownikiem a programem
* managerFunction.py - zawierającą klasę BookManager zapewniającą całą funkcjonalność na
bazie
* main.py - wywołującą metody
###Zewnętrzne biblioteki:
> JSON \
#Użycie funkcji load() i dump()
> REQUEST\
#Do połąćzenia sieciowego\
> PrettyTable i TextWrap \
#Do formatowania tekstu do postaci tabel\
