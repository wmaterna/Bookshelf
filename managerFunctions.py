import json
from textwrap import wrap
import requests
from prettytable import PrettyTable



class BookManager:
    def __init__(self, source):
        self.source = source

    def showBooks(self):
        titleTable = PrettyTable(["Title", "Author", "Description", "Year published"])
        titleTable.align["Description"] = "l"

        with open(self.source, "r") as f:
            temp = json.load(f)
            for entry in temp:
                wrapped_value_lines = wrap(str(entry["description"]) or '', 60) or ['']
                titleTable.add_row([entry["title"], entry["author"], wrapped_value_lines[0], entry["published"]])
                for subseq in wrapped_value_lines[1:]:
                    titleTable.add_row(['', '', subseq, ''])
                titleTable.add_row(['','','',''])
            print(titleTable)

    def searchBook(self):
        titleTable = PrettyTable(["Title", "Author", "Description", "Year published"])
        searchedTitle = input("What book are you looking for? ")
        with open(self.source, "r") as f:
            temp = json.load(f)
            for entry in temp:
                if entry["title"] == searchedTitle:
                    print("Yes, you have it on your Shelf! ")
                    print(self.tableWraping(titleTable, entry["title"], entry["author"],entry["description"],entry["published"]))
                    return
            print("You do not have this book on your Shelf")


    def addBook(self):
        print("Enter book info: ")
        title =  input("Book title : ")
        author= input("Book author: ")
        desc = input("Book description: (optional) ")
        year = input("Published data: ")
        self.addItem(title,author,desc,year)


    def deleteBook(self):
        self.showBooks()
        titleTable = PrettyTable(["Title", "Author"])
        title = input("Enter the title you want to delete: ")
        with open(self.source, "r") as f:
            temp = json.load(f)
            for entry in temp:
                if entry["title"] == title:
                    print("Are you sure you want to delete following position? [y/n]: ")
                    titleTable.add_row([entry["title"], entry["author"]])
                    print(titleTable)
                    confirm = input()
                    if confirm == 'y':
                        data = json.load(open(self.source))
                        for i in range(len(data)):
                            if data[i]["title"] == title:
                                data.pop(i)
                                break
                        with open(self.source, "w") as f:
                            json.dump(data,f, indent=4, separators=(',', ': '))
                        print("Book has been deleted from your storage ")
                        return
                    elif confirm == 'n':
                        return
                    else:
                        print("Unknown symbol")
                        return
            else:
                print("You do not have this position in your storage")


    def searchBookinAPI(self):
        titleTable = PrettyTable(["Title", "Author", "Description", "Year published"])
        bookTitle = input("Please enter book title: ")
        bookAuthor = input("Please enter book author: ")
        responseGoogle = requests.get(f"https://www.googleapis.com/books/v1/volumes?q=intitle:{bookTitle}+inauthor:{bookAuthor}&key=AIzaSyADNDAyuS4aq8m_oc6ha1r0sXI25ziZCl4")
        if responseGoogle.status_code != 200:
            raise ConnectionError("Problem with connecting to given URL")
        else:
            data = responseGoogle.json()
            if 'items' in data:
                for item in data['items']:
                    title = item['volumeInfo']['title']
                    author = item['volumeInfo']['authors'][0]
                    if "publishedDate" in item['volumeInfo']:
                        date = item['volumeInfo']['publishedDate']
                    else:
                        date = "Unknown date"
                    if "description" in item['volumeInfo']:
                        desc = item['volumeInfo']['description']
                    elif "categories" in item['volumeInfo']:
                        desc = item['volumeInfo']['categories'][0]
                    else:
                        desc = ""
                    break
                print(self.tableWraping(titleTable, title, author, desc, date))
                while True:
                    decistion = input("Do you want to add this position to your shelf? [y/n]: ")
                    if decistion == 'y':
                        self.addItem(title, author, desc, date)
                        break
                    elif decistion == 'n':
                        break
                    else:
                        print("Unnknown symbol, type y or n")
            else:
                print("Sorry, we do not have this title in our API")
                return


    def addItem(self,title, author, desc, date):
        data ={}
        with open (self.source, "r") as f:
            temp = json.load(f)
        data["title"] = title
        data["author"] = author
        data["description"] = desc
        data["published"] = date
        temp.append(data)
        with open(self.source, "w") as f:
            json.dump(temp, f)
        print("Your book has been added to your Bookshelf ")

    def tableWraping(self, table, title, author, desc, year):
        table.align["Description"] = "l"
        wrapped_value_lines = wrap(str(desc) or '', 60) or ['']
        table.add_row([title, author, wrapped_value_lines[0], year])
        for subseq in wrapped_value_lines[1:]:
            table.add_row(['', '', subseq, ''])
        return table