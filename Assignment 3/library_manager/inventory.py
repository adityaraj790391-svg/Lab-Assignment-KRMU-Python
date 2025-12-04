"""LibraryInventory: manage collection of Book objects with JSON persistence."""

from pathlib import Path
import json
import logging
from typing import List, Optional
from .book import Book

LOG = logging.getLogger(__name__)

class LibraryInventory:
    def __init__(self, storage_path: Path | str = "books.json"):
        self.storage_path = Path(storage_path)
        self.books: List[Book] = []
        self.load()

    def add_book(self, book: Book) -> None:
        if self.search_by_isbn(book.isbn):
            LOG.info("Book with ISBN %s already exists. Skipping add.", book.isbn)
            return
        self.books.append(book)
        LOG.info("Added book: %s", book)
        self.save()

    def search_by_title(self, title_substring: str) -> List[Book]:
        s = title_substring.strip().lower()
        return [b for b in self.books if s in b.title.lower()]

    def search_by_isbn(self, isbn: str) -> Optional[Book]:
        isbn = isbn.strip()
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def display_all(self) -> List[str]:
        return [str(b) for b in self.books]

    def issue_book(self, isbn: str) -> bool:
        book = self.search_by_isbn(isbn)
        if not book:
            LOG.error("Attempted to issue non-existent ISBN: %s", isbn)
            return False
        result = book.issue()
        if result:
            LOG.info("Issued book: %s", book)
            self.save()
        else:
            LOG.info("Book already issued: %s", book)
        return result

    def return_book(self, isbn: str) -> bool:
        book = self.search_by_isbn(isbn)
        if not book:
            LOG.error("Attempted to return non-existent ISBN: %s", isbn)
            return False
        result = book.return_book()
        if result:
            LOG.info("Returned book: %s", book)
            self.save()
        else:
            LOG.info("Book was not issued: %s", book)
        return result

   
    def save(self) -> None:
        try:
            data = [b.to_dict() for b in self.books]
            self.storage_path.write_text(json.dumps(data, indent=2, ensure_ascii=False))
            LOG.info("Saved %d books to %s", len(self.books), self.storage_path)
        except Exception as e:
            LOG.exception("Failed to save books: %s", e)

    def load(self) -> None:
        if not self.storage_path.exists():
            LOG.info("Storage file %s not found. Starting with empty inventory.", self.storage_path)
            self.books = []
            return
        try:
            text = self.storage_path.read_text()
            data = json.loads(text) if text.strip() else []
            books: List[Book] = []
            for entry in data:
                try:
                    b = Book(
                        title=entry.get("title", ""),
                        author=entry.get("author", ""),
                        isbn=entry.get("isbn", ""),
                        status=entry.get("status", "available"),
                    )
                    books.append(b)
                except Exception:
                    LOG.exception("Skipping malformed book entry: %s", entry)
            self.books = books
            LOG.info("Loaded %d books from %s", len(self.books), self.storage_path)
        except json.JSONDecodeError:
            LOG.exception("JSON decode error for %s — starting with empty inventory.", self.storage_path)
            self.books = []
        except Exception:
            LOG.exception("Unexpected error loading %s. Starting empty.", self.storage_path)
            self.books = []
