"""Command-line interface for the Library Inventory Manager.
Name: Aditya Raj
Date: 4/12/25 """

import logging
from library_manager.inventory import LibraryInventory
from library_manager.book import Book
from pathlib import Path

LOG = logging.getLogger(__name__)

MENU = """
Library Inventory Manager
1) Add Book
2) Issue Book
3) Return Book
4) View All Books
5) Search by Title
6) Search by ISBN
7) Exit
"""

def prompt(prompt_text: str) -> str:
    return input(prompt_text).strip()

def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    storage = Path("books.json")
    inv = LibraryInventory(storage)

    while True:
        print(MENU)
        choice = prompt("Choose an option (1-7): ")
        try:
            if choice == "1":
                title = prompt("Title: ")
                author = prompt("Author: ")
                isbn = prompt("ISBN: ")
                if not (title and author and isbn):
                    print("All fields are required.")
                    continue
                inv.add_book(Book(title=title, author=author, isbn=isbn))
                print("Book added.")

            elif choice == "2":
                isbn = prompt("ISBN to issue: ")
                if inv.issue_book(isbn):
                    print("Book issued.")
                else:
                    print("Could not issue book — check ISBN or status.")

            elif choice == "3":
                isbn = prompt("ISBN to return: ")
                if inv.return_book(isbn):
                    print("Book returned.")
                else:
                    print("Could not return book — check ISBN or status.")

            elif choice == "4":
                for line in inv.display_all():
                    print(line)

            elif choice == "5":
                q = prompt("Title search: ")
                results = inv.search_by_title(q)
                if results:
                    for b in results:
                        print(b)
                else:
                    print("No matches.")

            elif choice == "6":
                isbn = prompt("ISBN search: ")
                b = inv.search_by_isbn(isbn)
                if b:
                    print(b)
                else:
                    print("Not found.")

            elif choice == "7":
                print("Goodbye.")
                break

            else:
                print("Invalid choice — pick 1-7.")
        except KeyboardInterrupt:
            print("\nInterrupted — exiting.")
            break
        except Exception as e:
            LOG.exception("Error in CLI loop: %s", e)
            print("An error occurred. Check logs.")

if __name__ == "__main__":
    main()
