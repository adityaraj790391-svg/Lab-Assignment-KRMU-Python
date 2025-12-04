"""Book model for the Library Inventory Manager."""
from dataclasses import dataclass, asdict

AVAILABLE = "available"
ISSUED = "issued"

@dataclass
class Book:
    title: str
    author: str
    isbn: str
    status: str = AVAILABLE

    def __post_init__(self):
        self.title = str(self.title).strip()
        self.author = str(self.author).strip()
        self.isbn = str(self.isbn).strip()
        if self.status not in (AVAILABLE, ISSUED):
            self.status = AVAILABLE

    def __str__(self) -> str:
        return f"{self.title} — {self.author} (ISBN: {self.isbn}) [{self.status}]"

    def to_dict(self) -> dict:
        return asdict(self)

    def is_available(self) -> bool:
        return self.status == AVAILABLE

    def issue(self) -> bool:
        if self.is_available():
            self.status = ISSUED
            return True
        return False

    def return_book(self) -> bool:
        if not self.is_available():
            self.status = AVAILABLE
            return True
        return False
