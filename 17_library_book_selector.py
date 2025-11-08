# Library Book Selector:
# This script defines a Library class for books and stores several book objects.
# It allows the user to enter a number to select a book,
# then displays that book's title, author, and number of pages.

class Laibery :
    def __init__(self,title,athoner,pages) :
        self.title = title 
        self.athoner = athoner 
        self.pages = pages 

book_1 =Laibery('The word','Abdo motah',126)
book_2 =Laibery('The live ','Ali aloca',230)
book_3 =Laibery('The World','Ashar cokha',120)
books=[book_1,book_2,book_3]
user_input=int(input('Enter the book number'))
number_book = user_input - 1

print('\n *** inforntion the Book *** \n')
print(f"The Title book is {books[number_book].title}")
print(f"The Athoner book is {books[number_book].athoner}")
print(f"# Library Book Selector:
# This script defines a Library class for books and stores several book objects.
# It allows the user to enter a number to select a book,
# then displays that book's title, author, and number of pages.

class Laibery :
    def __init__(self,title,athoner,pages) :
        self.title = title 
        self.athoner = athoner 
        self.pages = pages 

book_1 =Laibery('The word','Abdo motah',126)
book_2 =Laibery('The live ','Ali aloca',230)
book_3 =Laibery('The World','Ashar cokha',120)
books=[book_1,book_2,book_3]
user_input=int(input('Enter the book number'))
number_book = user_input - 1

print('\n *** inforntion the Book *** \n')
print(f"The Title book is {books[number_book].title}")
print(f"The Athoner book is {books[number_book].athoner}")
print(f"The Pages book is {books[number_book].pages}")
