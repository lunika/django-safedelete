# imports
from django.test import TestCase

from .models import Author, Book

class TestOneToOneDeletion(TestCase):

    def test_one_to_one_deletion(self):
        author = Author()
        author.save()

        book = Book(name="foo", author=author)
        book.save()

        self.assertEqual(book.author, author)

        author.delete()

        book.refresh_from_db()

        with self.assertRaises(Book.author.RelatedObjectDoesNotExist):
            book.author