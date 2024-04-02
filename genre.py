class Genre:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    @classmethod
    def from_db(cls, value):
        return cls(value[0], value[1], value[2])

    @staticmethod
    def vloz_do_db(cursor):
        print("Vlozte nazov zanru: ")
        nazov = input()
        print("Vlozte popis zanru: ")
        description = input()
        cursor.execute("INSERT INTO genres (name, description) VALUES (%s, %s)", (nazov, description))

    def zobraz_zanre(cursor):
        cursor.execute("SELECT * FROM genres")
        genre_ID = cursor.fetchall()
        for genre in genre_ID:
            print(f"{genre[0]}. {genre[1]}")

    def __str__(self):
        return f"---GENRE---\nID Genre: {self.id}\nMeno: {self.name}\nDescription: {self.description}"