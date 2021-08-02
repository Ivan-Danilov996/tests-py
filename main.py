import unittest

from app import get_doc_owner_name, get_doc_shelf, show_all_docs_info, add_new_doc

documents = ['passport "2207 876234" "Василий Гупкин"',
             'invoice "11-2" "Геннадий Покемонов"',
             'insurance "10006" "Аристарх Павлов"',
             'passport "1111" "Ivan"']


class TestApp(unittest.TestCase):

    def test_get_doc_owner_name(self):
        self.assertEqual('Василий Гупкин', get_doc_owner_name("2207 876234"))

    def test_get_doc_shelf(self):
        self.assertEqual('1', get_doc_shelf('11-2'))

    def test_add_new_doc(self):
        self.assertEqual('2', add_new_doc('1111', 'passport', 'Ivan', '2'))

    def test_show_all_docs_info(self):
        self.assertEqual(documents, show_all_docs_info())


