class Book:
    def __init__(self, title: str, author: str, isbn: str, year: int, pages: int):
        if pages <= 0:
            raise ValueError("Число страниц должно быть положительным")

        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.pages = pages

        self._is_available = True
        self._last_read_pages = 0

    @property
    def is_available(self) -> bool:
        """Свойство только для чтения: доступность книги"""
        return self._is_available

    @property
    def last_read_pages(self) -> int:
        """Свойство только для чтения: сколько прочел страниц"""
        return self._last_read_pages

    def borrow(self):
        """Выдать книгу читателю"""
        if not self._is_available:
            raise ValueError("Книга уже выдана")
        self._is_available = False

    def give_back(self, pages_read: int):
        """Вернуть книгу и зафиксировать прочитанные страницы"""
        if self._is_available:
            raise ValueError("Книга и так на полке")
        if not (0 <= pages_read <= self.pages):
            raise ValueError(f"Число прочитанных страниц должно быть от 0 до {self.pages}")

        self._last_read_pages = pages_read
        self._is_available = True

    def __eq__(self, other) -> bool:
        """Книги равны, если у них одинаковый ISBN"""
        if not isinstance(other, Book):
            return NotImplemented
        return self.isbn == other.isbn

    def __lt__(self, other) -> bool:
        """Сравнение по году издания для сортировки от старых к новым"""
        if not isinstance(other, Book):
            return NotImplemented
        return self.year < other.year

    def __repr__(self) -> str:
        """Текстовое представление объекта"""
        return f"Book({self.title!r}, {self.author!r}, {self.isbn!r}, {self.year}, {self.pages})"

b = Book("1984", "Оруэлл", "123", 1949, 328)
old = Book("Мы", "Замятин", "456", 1924, 224)

if __name__ == "__main__":
    (b.is_available)
    (b.last_read_pages)
    b.borrow()
    try:
        b.give_back(400)
    except  ValueError as e:
        (f"Ошибка перехвачена: {e}")
    (b.is_available)
    (b.give_back(120))
    (b.last_read_pages)
    (b == Book("1984", "Оруэлл", "123", 1949, 328))
    (old == Book("Мы", "Замятин", "456", 1924, 224))
    (sorted([b, old]))