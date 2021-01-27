# Bookshelf

Dokumentacja Projektu 

Weronika Materna

Kurs: Język Python




Projekt Bazy Książek


  Celem projektu było zaimplementowanie Bazy Książek, aby potencjalny użytkownik miał 
możliwość zapisania i odczytywania książek. Rolę Bazy Danych pełni plik o rozszerzeniu json, z którego czytane i  do którego zapisywane są pozycje. 
  Użytkownik ma możliwość wylistowania wszystkich książek znajdujących się w Bazie, wyszukania konkretnej pozycji, 
dodania nowej pozycji, usunięcia a także wyszukania określonej książki dzięki połączeniem z GoogleAPI.
  Projekt składa się z 4 plików, itemsData.json - przechowujących pozycje, interface.py zarządzającym 
komunikacją pomiędzy użytkownikiem a programem, managerFunction.py zawierającą klasę BookManager zapewniającą całą funkcjonalność na
bazie i main.py - wywołującą metody.
  Projekt korzysta z zewnętrznych bibliotek tj. json do obsługi operacji na formacie json (funkcje load i dump), 
request połączenia sieciowego, prettytable i textwrap do formatowania tekstu wyświetlanego użytkownikowi w postaci tabel
