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
    option = input()
    while True:
        if option == '1':
            showBooks()
            input("Press enter to see options again ")
            choices()
            break
        elif option == '2':
            searchBook()
            input("Press enter to see options again ")
            choices()
            break
        elif option == '3':
            searchBookinAPI()
            input("Press enter to see options again ")
            choices()
            break
        elif option == '4':
            addBook()
            input("Press enter to see options again ")
            choices()
            break
        elif option == '5':
            deleteBook()
            input("Press enter to see options again ")
            choices()
            break
        elif option == 'q':
            return