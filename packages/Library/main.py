
from Library import Library

library = Library.Library()

def Menu():
    while True :
        option = input("Enter Option (1.add book 2.remove book 3.search book 4.show books 5.Exit): ")

        match option :
            case '1' :
                title = input("Title : ")
                author = input ("Author : ")
                library.add_book(title=title,author=author)
                print ("Book added successfully !")
            case '2' :
                title = input("Title : ")
                library.remove_book(title=title)
                print ("Book removed successfully !")
            case '3':
                title = input("Title : ")
                print(library.search_book(title=title))
            case '4':
                print(library.show_books())
            case '5':
                break


if __name__ == "__main__" :
    Menu()