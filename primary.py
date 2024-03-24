#Library management system allowing users to manage books, library members and transactions effectively

#Book Class
class Book:
    #an empty list keep that helps store the values of the initialized variables, attributes of the object
    keep = []

    #init function which runs automatically as soon as the class is called or instantiated
    def __init__(self, bookname:str, author:str, ISBN:str, genre:str, publication_year:int):
        #assert to handle exceptions
        assert publication_year >= 1500, f"No books published before the year 1500 are available"

        #instance attributes initialized
        self.bookname = bookname
        self.author = author
        self.ISBN = ISBN
        self.genre = genre
        self.publication_year = publication_year

        #this adds the content of each instance from the instance variable or attribute to the list in keep.
        #the empty list is stored in a class variable called keep
        Book.keep.append(self)

    #adding new books
    @classmethod #this a class method which operates without instances but on the class itself

    #this method helps add new books to the class it takes the arguments as the way it is taken when the books are being instantiated
    #this is called from the class level

    #to use the method syntax will be for example: book_771 =Book.add_booK(in here necessary arguments will be passed) 
    def add_books(cls, bookname, author, ISBN, genre, publication_year):
        new_book = cls(bookname, author, ISBN, genre, publication_year)

        #this then uses the list method append to add the new book to the list
        cls.keep.append(new_book)
        return new_book
        
    @classmethod

    #this class method helps to update the already available instantiated class attributes in the book class 
    def update_books(cls):
        #directs user on what specific thing to update in the books
        print("""
            To Update Book Name Type in B
            To Update Author Type in A
            To Update ISBN Type in I
            To Update Genre Type in G
            To Update Publication Year Type in P
            """)
        update_term = input("What Do You Wish To Update In The Book? ")


        #looks from the set criteria the user wishes to use and picks by logic and peforms the operations necessary
        #updating all the attributes that tally in name, author, ISBN, genre and publication year
        if update_term.lower() == 'b':
            existing_bookName = input("What Book Would You like to update? ")
            new_bookname = input("What name would you like to change it to? ")
           
            for book in cls.keep:
                if book.bookname.lower() == existing_bookName.lower():
                    book.bookname = new_bookname
                    print(f"Done! {existing_bookName} has been changed to {new_bookname}")
                else:
                    print(f"Book {existing_bookName} not found please try again")
       
        elif update_term.lower() == 'a':
            existing_author = input("What Author's Books would you like to update: ")
            new_author = input("What is the new Author new you wish to replace it with: ")
            
            for book in cls.keep:
                if book.author.lower() == existing_author:
                    book.author = new_author
                    print(f"The Authors {existing_author} has been replaced with new_author")
                else:
                    print(f"{existing_author} not found abeg authors, Try again.")
        
        elif update_term.lower() == 'i':
            existing_ISBN = input("What ISBN would you like to update: ")
            new_ISBN = input("What's the ISBN you would like to update it to: ")
            for book in cls.keep:
                if book.ISBN == existing_ISBN:
                    book.ISBN = new_ISBN
                    print(f"Book ISBN {existing_ISBN} has been updated to {new_ISBN}")
                else:    
                    print(f"ISBN {existing_ISBN} does not exist, try again.")
                
        elif update_term.lower() == 'g':
            existing_Genre = input("What genre's would you like to update: ")
            new_Genre = input("What Genre would you like to put in place: ")
            for book in cls.keep:
                if book.genre.lower() == existing_Genre:
                    book.genre = new_Genre
                    print(f"The Genre {existing_Genre} has been updated to {new_Genre}")
                else:
                    print(f"The Genre {existing_Genre} does not exist")

        elif update_term.lower() == 'p':
            existing_pubYear = int(input("What book years would you like to update: "))
            new_pubYear = int(input("What year would you like to update it to? "))
            for book in cls.keep:
                if book.publication_year == existing_pubYear:
                    book.publication_year = new_pubYear
                    print(f"Book from the year {existing_pubYear} have been updated to {new_pubYear}") 
                else:
                    print(f"{existing_pubYear} does not exist among available years")

        else:
            print("Wrong input, please try again.") 
            
    
    #removes an entire books details by a single criteria, for example if the books belong to the year 2016 everything about it gets deleted               
    @classmethod
    def delete_book_by_bookname(cls, book_name):
        for book in cls.keep:
            if book.bookname.lower() == book_name.lower():
                cls.keep.remove(book)
                print(f"{book_name} is deleted from the books library")

    @classmethod
    def delete_by_authorname(cls, author_name):
        for authors in cls.keep:
            if authors.author.lower() == author_name.lower():
                cls.keep.remove(authors)
                print(f"The book by {author_name}, has been deleted from the library")

    @classmethod
    def delete_by_ISBN(cls):
        ISBN_del = input("What ISBN would you like to delete? ")
        for book in cls.keep:
            if book.ISBN.lower() == ISBN_del.lower():
                cls.keep.remove(book)

    @classmethod
    def delete_by_year_published(cls):
        date_prompt = int(input("What books from a certain year would you like to delete: "))
        for year in cls.keep:
            if year.publication_year == date_prompt:
                cls.keep.remove(year)
                print(f"The books from the year {date_prompt} have been delted")

    @classmethod
    def delete_by_genre(cls):
        genre_D = input("What genre of books would you look to delete: ")
        for genres in cls.keep:
            if genres.genre.lower() == genre_D.lower():
                cls.keep.remove(genres)
                print(f"The books in genre {genre_D} have been deleted!")
            

    #this is a magic method that allows the contents of a class to be shown in a more user friendly way.   
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.bookname}'{self.author}', '{self.ISBN}', '{self.genre}', {self.publication_year})" 

book1 = Book("A Deep End","Camila Stens", "901-222-22222","Biography", 1982)
book2 = Book("Up Hill", "Stephen Jaws", "212-11-111-11", "Thriller", 2007)
book3 = Book("When it collides", "Sam Grips", "231-341-222", "Fiction", 2002)
book4 = Book("Up In The air", "Wendy Baumaannn", "213-2331-342", "Essay", 2019)
book5 = Book("Attack", "John Climber", "123-3000-331-1", "Narrative", 2017) 
book6 = Book("Ande and Up", "Amanda Falls", "239-000-02101", "Humor", 2016)
book7 = Book("Can't we fly", "Camila Stens", "124-444-121-554","Novel", 2013)
book8 = Book("Marie in wheels", "Kristie Phalms", "233-3213-342", "Humor", 2016)

#Book.delete_by_ISBN()
#print(Book.keep)




#Member Class(Handling the members in the library)
class Member:
    mem = []
    def __init__(self, name:str, membership_ID:str, phone: str):
        #assert to handle exceptions
        assert len(name) >= 3, f"Name should be longer"
        assert len(membership_ID) >= 7, f"Membership ID is short, check well"
        assert len(phone) >= 10, f"Phone number can't be more thean 10 digits"

        #instance attributes initialized
        self.name = name
        self.membership_ID = membership_ID
        self.phone = phone

        Member.mem.append(self)


    #adding new members
    @classmethod
    def add_members(cls, name, membership_ID, phone):
        new_member = (name, membership_ID, phone)
        cls.mem.append(new_member)
        return new_member

    #updating books
    @classmethod
    def update_members(cls):
        print("""
                What criteria would you like to update the members of the library on?
                
                Type in N to update Name
                Type in M to update Membership ID
                Type in P to update Phone details
              """)
        update_member = input("What members details would you like to update: ")
        if update_member.lower() == 'n':
            existing_membername = input("What Member's name would you like to update: ")
            new_member_name = input("What name would you like to change it to: ")
            for name in cls.mem:
                if name.name.lower() == existing_membername.lower():
                    name.name = new_member_name
                    print(f"{existing_membername} has been changed to {new_member_name}")
                else:
                    print(f"The given name {existing_ID} cannot be found.")


        elif update_member.lower() == 'm':
            existing_ID = input("What Member's ID would you like to update: ")
            new_member_ID = input("What name would you like to update to: ")
            for ID in cls.mem:
                if ID.membership_ID.lower() == existing_ID.lower():
                    ID.membership_ID = new_member_ID
                    print(f"{existing_ID} has been updated in {new_member_ID}")
                else:
                    print(f"{existing_ID} can't be found")
        
        elif update_member.lower() =='P':
            existing_Phone = input("what existing phone number would you like to change: ")
            new_phone = input("What is the new phone number you'll like to put it with: ")

            for phone in cls.mem:
                if phone.phone.lower() == existing_Phone.lower():
                    phone.phone = new_phone
                    print(f"The number{existing_Phone} has been updated to {new_phone}")
                else:
                    print(f"{existing_Phone} can't be found.")

        else:
            print(f"Your chosen choice is mostly likely wrong.")

        
    @classmethod
    def delete_members(cls):
        #to delete a member's entire details we delete it by an identifier which is what one of the attributes in the __init__ can act as
        #so lines of code will be implemented to delete an entire user from the list based on a certain attribute.


        print("""
                What would you like to use to delete the members details
              
                To delete with Member's name type in NE
                To delete with Member's ID type in ID
                To delete with Member's Phone type in PE
              """) 

        delete_option = input("What would you like to delete the users with? ")
        if delete_option.lower() == 'ne':
            mem_del = input("Type in Member's name: ")
            confirm_del = input("Type in name again for confirmation it will delete all member's details- ")
        
            for member in cls.mem:
                
                if mem_del.lower() == confirm_del.lower():    
                    if member.name.lower() == mem_del.lower():
                        cls.mem.remove(member)
                    else:
                        return f"{mem_del} not found"
                        
                else:
                    print("It does not match previous name, try again!")
       
        elif delete_option.lower() == 'id':
            mem_del_ID = input("Type in Member's ID: ")
            confirm_del_ID = input("Type in ID again for confirmation it will delete all member's details- ")
            for members in cls.mem:
                
                if mem_del_ID.lower() == confirm_del_ID.lower():

                    if members.membership_ID.lower() == mem_del_ID.lower():
                        cls.mem.remove(members)
                    else:
                        return f"{mem_del_ID} not found"
                else:
                    print("Confirmation Failed!")

        elif delete_option.lower() ==  'pe':
            mem_del_phone = input("Type in Phone details: ")
            confirm_del_phone = input("Type in Phone again for confirmation it will delete all member's details- ")
            for members in cls.mem:
                
                if mem_del_phone.lower() == confirm_del_phone.lower():

                    if members.phone.lower() == mem_del_phone.lower():
                        cls.mem.remove(members)
                    else:
                        return f"{mem_del_phone} not found"
                else:
                    print("confirmation failed!")
        else:
            print("Option you put in is not valid try again")
        
        
    def __repr__(self):
        return f"{self.__class__.__name__} ('{self.name}', '{self.membership_ID}', '{self.phone}')"
    

member1 = Member("Clint Amore", "Y2-1302", "0129284682")
member2 = Member("Dyche Xera", "Y2-2139","1203839182")
member3 = Member("Bakes Sam", "Y3-1239", "2103484761")


Member.delete_members()
print(Member.mem)