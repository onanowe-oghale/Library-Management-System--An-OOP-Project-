#Library class

class Library_Books:
    """
    This Class will contain the Books in a library from a txt file,
    The books ID will also be there, the books Author name and the genre of the book

    The administrator will be able to add and delete books to the Library.
    """

    def __init__(self, library_books):
        self.library_books = "library_books.txt"
        self.library_dict = {}
        Id = 1021

        #to handle the books

        with open(self.library_books) as lb:
            content = lb.readlines()

        for line in content:
            self.library_dict.update({str(Id): {"Book_title": line.replace("\n", ""), "Author_name": "", 
            "Book_genre": ""}})
            Id = Id + 2

    def display_books(self):
        print("--------_____Books In The Library_____---------")
        print("Books ID \t  Books Title" ) 
        print("________________________________________________")
        for keys , values in self.library_dict.items():
            print(f"{keys} \t \t{values.get('Book_title')} \t")     

    def add_books(self):
        print("_------------------Welcome--------------------_\n")
        add_options ={"D": "Donate Book To The Library", "A": "Add New Library Book"}
        
        for keys, values in add_options.items():
            print(f"Press {keys} to {values}")
        add_choice = input("How is the book being added: ").lower()

        if add_choice == 'd':
            adder_name = input("What Is Your Name: ")
            print(f"Adding book from {adder_name} this shouldn't take long \n")
            New_book = input("What Is Name of the New book you would like to add: ")

            if New_book == "":
                print("Book name can't be blank")
                self.add_books()
            elif len(New_book) > 35:
                print("New Book Name can't be greater than 35 characters!")
            else:
                with open(self.library_books, 'a') as bk:
                    bk.writelines(f"{New_book} \n")
                    self.library_dict.update({str(int(max(self.library_dict))+2): {"Book_title": New_book, "Author_name":"", "Book_genre":""}})
                    print("Thank You, Book Added successfully! ")

        elif add_choice == 'a':
            New_book = input("Name Of Book Brought In: ")
            if New_book == "":
                print("Book name can't be blank")
                self.add_books()
            elif len(New_book) > 35:
                print("New Book Name can't be greater than 35 characters!")
            else:
                with open(self.library_books, 'a') as bk:
                    bk.writelines(f"{New_book}\n")
                    self.library_dict.update({str(int(max(self.library_dict))+2): {"Book_title": New_book, "Author_name":"", "Book_genre":""}})
                    print(f"Book {New_book} has been added to the library")
        
        else: 
            print("Seems there is a problem with your input, please try again! ")
            return self.add_books()
        
    def search_book(self):
        pass

    def delete_book(self):
        print("Book can only be deleted by administrator\n!")
        delete_option = int(input("Access code to delete book: "))

        if delete_option != 12234:
            print("Acces Code Not Correct")
        else:
            book_id = input("Input Book Id: ")
            
            if book_id in self.library_dict:
                print(f"The book {book_id} belongs to the the book {self.library_dict [book_id] ['Book_title']}")
                with open(self.library_books, 'r') as bk:
                    bk.readlines()
                    del(self.library_dict[book_id])
                    print("Book has been removed from the dictionary")
                    return self.display_books()
            else:
                print("Book ID not found!!!")
