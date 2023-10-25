import main
from unittest import TestCase
import flask

class main_test(TestCase):
    def test_main(self):
        with self.app_context():
            item = ItemModel('EUR', 15, 2, 2023, 09, 25)
            self(item)