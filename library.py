
class Book:
    def __init__(self, title, author, isbn, year, pages):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.pages = pages
        self.is_available = True
        self.last_read_pages = 0

    def __repr__(self):
        return (
            f"Book({self.title!r}, {self.author!r}, "
            f"{self.isbn!r}, {self.year}, {self.pages})"
        )


class Reader:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.pages_read = 0


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_by_author(self, author):
        return [
            book for book in self.books
            if book.author == author
        ]

    def lend(self, isbn, reader):
        book = self.find_by_isbn(isbn)

        if book is None:
            raise KeyError(isbn)

        if not book.is_available:
            raise ValueError("Книга уже выдана")

        book.is_available = False
        reader.books.append(book)

    def take_back(self, isbn, reader, pages_read):
        book = self.find_by_isbn(isbn)

        if book is None or book not in reader.books:
            raise ValueError("У читателя нет этой книги")

        if not isinstance(pages_read, int) or isinstance(pages_read, bool):
            raise ValueError("Количество страниц должно быть целым числом")

        if pages_read < 0 or pages_read > book.pages:
            raise ValueError("Недопустимое количество страниц")

        book.last_read_pages = pages_read
        book.is_available = True
        reader.books.remove(book)
        reader.pages_read += pages_read

    def available(self):
        return [
            book for book in self.books
            if book.is_available
        ]

    def unfinished(self):
        return [
            book for book in self.books
            if 0 < book.last_read_pages < book.pages
        ]

    def __len__(self):
        return len(self.books)


if __name__ == "__main__":
    lib = Library()
    lib.add_book(Book("1984", "Оруэлл", "123", 1949, 328))
    lib.add_book(Book("Скотный двор", "Оруэлл", "124", 1945, 112))
    alice = Reader("Алиса")

    lib.lend("123", alice)
    alice.books
    lib.find_by_isbn("123").is_available
    len(lib.available())

    try:
        lib.lend("123", Reader("Боб"))
    except ValueError:
        pass

    try:
        lib.take_back("123", alice, 500)
    except ValueError:
        pass

    alice.books
    lib.take_back("123", alice, 100)
    alice.books
    alice.pages_read
    lib.unfinished()

    lib.lend("124", alice)
    lib.take_back("124", alice, 112)
    alice.pages_read
    len(lib.unfinished())
