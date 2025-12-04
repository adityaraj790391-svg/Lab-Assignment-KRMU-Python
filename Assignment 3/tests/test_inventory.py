import unittest
from pathlib import Path
import tempfile
from library_manager.inventory import LibraryInventory
from library_manager.book import Book

class TestInventory(unittest.TestCase):
    def setUp(self):
        self.tmpfile = Path(tempfile.mktemp(suffix='.json'))
        if self.tmpfile.exists():
            self.tmpfile.unlink()
        self.inv = LibraryInventory(self.tmpfile)

    def tearDown(self):
        if self.tmpfile.exists():
            self.tmpfile.unlink()

    def test_add_and_search(self):
        b = Book('T1', 'Auth', 'isbn-123')
        self.inv.add_book(b)
        found = self.inv.search_by_isbn('isbn-123')
        self.assertIsNotNone(found)
        self.assertEqual(found.title, 'T1')

    def test_issue_and_return(self):
        b = Book('T2', 'Auth2', 'isbn-222')
        self.inv.add_book(b)
        self.assertTrue(self.inv.issue_book('isbn-222'))
        self.assertFalse(self.inv.issue_book('isbn-222'))
        self.assertTrue(self.inv.return_book('isbn-222'))

if __name__ == '__main__':
    unittest.main()
