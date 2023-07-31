from books_package.booklover import BookLover

print()

test_object = BookLover("Luna Lovegood", "luna@hogwarts.edu", "fiction")
print('test_object = BookLover("Luna Lovegood", "luna@hogwarts.edu", "fiction")')
print()
test_object.add_book("Harry Potter and the Sorcerer's Stone", 5)
print('test_object.add_book("Harry Potter and the Sorcerer\'s Stone", 5)')
print()

print("Number of books read: ",test_object.num_books_read())

