import psycopg2
from author import Author
from genre import Genre
from book import Books

conn = psycopg2.connect(
    dbname='b81s1xhecmfxnpmteb27',
    user='urici3i0icy8cuufham5',
    password='FrtbL6FqnCsROZMWocDBkgoOeoZC7R',
    host='b81s1xhecmfxnpmteb27-postgresql.services.clever-cloud.com',
    port=50013
)

cursor = conn.cursor()

def vypis_menu():
    print("1. Pridat autora")
    print("2. Pridat zaner")
    print("3. Pridat knihu")

def aplikacia():
    while True:
        vypis_menu()
        choice = input("Vasa moznost: ")
        if choice == "1":
            Author.vloz_do_db(cursor)
            conn.commit()
            print("Pridat autora")
        elif choice == "2":
            Genre.vloz_do_db(cursor)
            conn.commit()
            print("Pridat zaner")
        elif choice == "3":
            Author.zobraz_autorov(cursor)
            author_ID = input("ID Authora:  ")
            Genre.zobraz_zanre(cursor)
            genre_ID = input("ID Genre:  ")
            Books.vloz_do_db(cursor, author_ID, genre_ID)
            conn.commit()
            print("Pridat knihu")
        else:
            print("Neplatny vstup")

aplikacia()










