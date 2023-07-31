import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Jane Eyre", 4)
        self.assertIn("Jane Eyre", test_object.book_list['book_name'].values)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Harry Potter and the Sorcerer's Stone", 4)
        test_object.add_book("Harry Potter and the Sorcerer's Stone", 4)
        self.assertEqual(test_object.num_books_read(), 1)
        
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Harry Potter and the Chamber of Secrets", 5)
        self.assertTrue(test_object.has_read("Harry Potter and the Chamber of Secrets"))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        self.assertFalse(test_object.has_read("Harry Potter and the Prisoner of Azkaban"))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Harry Potter and the Goblet of Fire", 2)
        test_object.add_book("Harry Potter and the Order of the Phoenix", 3)
        test_object.add_book("Harry Potter and the Half-Blood Prince", 5)
        expected = 3
        self.assertEqual(test_object.num_books_read(), expected)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Harry Potter and the Goblet of Fire", 2)
        test_object.add_book("Harry Potter and the Order of the Phoenix", 3)
        test_object.add_book("Harry Potter and the Half-Blood Prince", 5)
        fav_book = test_object.fav_books()
        self.assertTrue(fav_book.shape[0] > 0)
        self.assertTrue((fav_book['book_rating'] > 3).all())
        
if __name__ == '__main__':
    
    unittest.main(verbosity=2)