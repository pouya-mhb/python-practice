'''
this is a library management system
this system can add books, remove and update books, and manage authors

'''

class User ():
    def __init__(self,id,name, last_name, age, gender):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender

class Book():
    def __init__(self, id,title, desciption, author, publish_date,ISBN):
        self.id = id
        self.title = title
        self.desciption = desciption
        self.author = author
        self.published_date = publish_date
        self.ISBN = ISBN


class Library ():
    def __init__(self, books={}, users={} ,authors={}):
        self.books = books
        self.users = users
        self.authors = authors

    def add_user (self, id, name, last_name, age, gender, joined_date):
        self.users[id] = {'name': name, 'last_name': last_name, 'age': age, 'gender': gender, 'joined_date': joined_date}

    def remove_user (self,id):
        if id in self.users:
            del self.users[id]
        else:
            return "User not found"

    def update_user (self, user_id, **kwargs):
        if user_id in self.users:
            self.users[user_id].update(**kwargs)
        else:
            return "User not found"

    def add_book(self, id, title, description, author, published_date, ISBN):
        if self.books.get(id) is not None:
            return "Book already exists"
        self.books[id] = {'title': title, 'description': description, 'author': author, 'published_date': published_date, 'ISBN': ISBN}

    def remove_book(self,id):
        if id not in self.books:
            return "Book not found"
        removed_book = self.books[id]
        del self.books[id]
        print(f"The {removed_book['title']} has been removed")

    def update_book(self,book_id,**kwargs):
        if book_id in self.books :
            self.books[book_id].update(**kwargs)
        else:
            return "Book not found"

    def search_book (self,title):
        book_results = []
        for book in self.books:
            if title.lower() in book.title.lower():
                book_results.append(book)
        return book_results

    def add_author(self, id, name, last_name, age, gender):
        self.authors[id] = {'name': name, 'last_name': last_name, 'age': age, 'gender': gender}

    def remove_author(self,id):
        del self.authors[id]

    def update_author(self,id,**kwargs):
        if id in self.authors:
            self.authors[id].update(**kwargs)
        else:
            return "Author not found"

    def view_library(self):
        return f"Users : {self.users}, Authors : {self.authors}, Books : {self.books}"


def main ():
    library = Library()
    library.add_user(1, "John", "Doe", 30, "Male", "2023-01-01")
    library.add_book(1, "The Great Gatsby", "A novel by F. Scott Fitzgerald", "F. Scott Fitzgerald", "1925-04-10", "9780743273565")
    library.add_author(1, "F. Scott", "Fitzgerald", 44, "Male")

    library.add_user(2, "Jane", "Doe", 28, "Female", "2023-01-01")
    library.add_book(2, "To Kill a Mockingbird", "A novel by Harper Lee", "Harper Lee", "1960-07-11", "9780061120084")
    library.add_author(2, "Harper", "Lee", 34, "Female")

    library.update_author(1, age=45)
    library.update_book(1, title="The Great Gatsby (Updated)", description="An updated description")
    library.update_user(1, age=31)

    library.update_author(2, age=35)
    library.update_book(2, title="To Kill a Mockingbird (Updated)", description="An updated description")
    library.update_user(2, age=29)

    library.remove_author(1)
    library.remove_book(1)
    library.remove_user(1)

    print(library.view_library())

if __name__ == "__main__":
    main()