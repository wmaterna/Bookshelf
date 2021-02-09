from managerFunctions import *


def choices():

    infoTable = PrettyTable(["No", "Action"])
    infoTable.add_row(["1", "Show your local Bookshelf"])
    infoTable.add_row(["2", "Search a book in your local Bookshelf"])
    infoTable.add_row(["3", "Search a book in GoogleBooks API"])
    infoTable.add_row(["4", "Add book position to your local Bookshelf manualy"])
    infoTable.add_row(["5", "Delete book from your Bookshelf manualy"])
    infoTable.add_row(['q', "Quit the program"])
    print(infoTable)
    interface()

def interface():
    bookMng = BookManager("./data/itemsData.json")
    option = input()

    while option!='q':
        if option == '1':
            bookMng.showBooks()
        elif option == '2':
            bookMng.searchBook()
        elif option == '3':
            bookMng.searchBookinAPI()
        elif option == '4':
            bookMng.addBook()
        elif option == '5':
            bookMng.deleteBook()
        infoTable = PrettyTable(["No", "Action"])
        infoTable.add_row(["1", "Show your local Bookshelf"])
        infoTable.add_row(["2", "Search a book in your local Bookshelf"])
        infoTable.add_row(["3", "Search a book in GoogleBooks API"])
        infoTable.add_row(["4", "Add book position to your local Bookshelf manualy"])
        infoTable.add_row(["5", "Delete book from your Bookshelf manualy"])
        infoTable.add_row(['q', "Quit the program"])
        print(infoTable)
        option = input("What should I do next? ")