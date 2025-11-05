
class Library:
    def __init__(self,books=[]):
        self.books = books

    def add_book(self,title, author):
        self.books.append((title,author))

    def remove_book(self,title):
        for i in range (len(self.books)):
            if title == self.books[(i)][0]:
                del self.books[i]

    def search_book(self,title):
        for i in range (len(self.books)):
            if title == self.books[(i)][0]:
                return f"The Book {self.books[i][0]} Found."
            else :
                return f"Book Not Found !"

    def show_books(self):
        return self.books



if __name__ == "__main__" :
    print ("you should use me as a package  !")