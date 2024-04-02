class Books:
    def __init__(self, id, title, author_id, genre_id, isbn, publication_year, copies):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.genre_id = genre_id
        self.isbn = isbn
        self.publication_year = publication_year
        self.copies = copies


    @classmethod
    def from_db(cls, value):
        return cls(value[0], value[1], value[2], value[3], value[4], value[5], value[6])

    @staticmethod
    def vloz_do_db(cursor, author_ID, genre_ID):
        print("Vlozte nazov Knihy: ")
        title = input()
        print("Vlozte ISBN: ")
        ISBN = input()
        cursor.execute("INSERT INTO books (title, author_id, genre_id, isbn) VALUES (%s, %s, %s, %s)", (title, author_ID, genre_ID, ISBN))

    def __str__(self):
        return f"---BOOKS---\nID Book: {self.id}\nMeno: {self.title}\nBio: {self.ISBN}"

