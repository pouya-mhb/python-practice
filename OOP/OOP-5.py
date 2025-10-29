# Special Methods
# using built-in functions


class Book1:
    def __init__(self, title, author, pages):

        self.title = title
        self.author = author
        self.pages = pages


class Book2:
    def __init__(self, title, author, pages):

        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages


my_book_1 = Book1(title="Book 1", author="John Doe", pages=215)

my_book_2 = Book2(title="Book 2", author="John Doe", pages=215)

print(my_book_1)

print(my_book_2)

print(str(my_book_2))

print(len(my_book_2))
