#Library management system allowing users to manage books, library members and transactions effectively

#Book Class
class Book:
    keep = []
    def __init__(self, bookname:str, author:str, ISBN:str, genre:str, publication_year:int):
        #assert to handle exceptions
        assert publication_year >= 1500, f"No books published before the year 1500 are available"

        #instance attributes initialized
        self.bookname = bookname
        self.author = author
        self.ISBN = ISBN
        self.genre = genre
        self.publication_year = publication_year

        Book.keep.append(self)

    #adding new books
    @classmethod
    def add_books(cls, bookname, author, ISBN, genre, publication_year):
        new_book = cls(bookname, author, ISBN, genre, publication_year)
        cls.keep.append(new_book)
        return new_book
        

    def update_books(self):
        pass

   
    @classmethod
    def delete_book_by_bookname(cls, book_name):
        for book in cls.keep:
            if book.bookname == book_name:
                cls.keep.remove(book)
                print(f"{book_name} is deleted from the books library")

    @classmethod
    def delete_by_authorname(cls, author_name):
        for authors in cls.keep:
            if authors.author == author_name:
                cls.keep.remove(authors)
                print(f"The book by {author_name}, has been deleted from the library")
            

        
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.bookname}'{self.author}', '{self.ISBN}', {self.genre}, {self.publication_year})" 

book1 = Book("A Deep End","Camila Stens", "901-222-22222","Biography", 1982)
book2 = Book("Up Hill", "Stephen Jaws", "212-11-111-11", "Thriller", 2007)
book3 = Book("When it collides", "Sam Grips", "231-341-222", "Fiction", 2002)
book4 = Book("Up In The air", "Wendy Baumaannn", "213-2331-342", "Essay", 2019)
book5 = Book("Attack", "John Climber", "123-3000-331-1", "Narrative", 2017) 
book6 = Book("Ande and Up", "Amanda Falls", "239-000-02101", "Humor", 2016)
book7 = Book("Can't we fly", "Camila Stens", "124-444-121-554","Novel", 2013)

Book.delete_by_authorname("Camila Stens")
print(Book.keep)





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


