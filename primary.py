#Library management system allowing users to manage books, library members and transactions effectively

#Book Class
class Book:
    keep = []
    def __init__(self, author:str, ISBN:str, genre:str, publication_year:int):
        #assert to handle exceptions
        assert publication_year >= 1500, f"No books published before the year 1500 are available"

        #instance attributes initialized
        self.author = author
        self.ISBN = ISBN
        self.genre = genre
        self.publication_year = publication_year

    #adding new books
    @classmethod
    def add_books(cls, author, ISBN, genre, publication_year):
        new_book = cls(author, ISBN, genre, publication_year)
        return new_book
        

    def update_books(self):
        pass

    def delete_books(self):
        pass


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.author}', '{self.ISBN}', {self.genre}, {self.publication_year})" 

    
    
#Member Class(Handling the members in the library)
class Member:
    def __init__(self, name:str, membership_ID:str, contact_info: str):
        #assert to handle exceptions
        assert name >= 3, f"Name should be longer"
        assert membership_ID >= 7, f"Membership ID is short, check well"

        #instance attributes initialized
        self.name = name
        self.membership_ID = membership_ID
        self.contact_info = contact_info


    #adding new members
    def add_members(self):
        pass

    #updating books
    def update_members(self):
        pass

    def delete_books(self):
        pass


    
book1 = Book("Carren Meinyard", "978-0-000-00000-0", "Adventure", 1900)

book_add = []
book_author = input("Add Book author: ")
book_ISBN = input("Add Book ISBN: ")
book_genre = input("What genre does the Book belong to: ")
book_publication_year = input("What year was the book published: ")

book_add.insert(book_author, book_ISBN, book_genre, book_publication_year)

book1.add_books(book_add)
