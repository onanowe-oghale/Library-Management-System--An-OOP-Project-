from library import Library_Books
import datetime
#The transaction class

class Transaction(Library_Books):
    """
    This class is responsible for showing the status of a given book 
    This class will be responsible for issuing and returning books to people that need them
    """

    def __init__(self, library_books):
        super().__init__(library_books,)

        self.transaction_dict = {}
        Id = 1021

        with open(self.library_books) as bk:
            line = bk.readlines()

        for lines in line:
            self.transaction_dict.update({str(int(Id)): {"Book_title": lines.replace("\n", ""), "Status": "Available", 
            "Lender_name": "", "Issue_date": ""}})
            Id = Id + 2



    def library_state(self):
        print("________---------Library State---------_________")
        print("Book ID \t Book Title ")

        for keys, values in self.transaction_dict.items():
            print(f"{keys} \t \t{values.get('Book_title')} \t - [{values.get('Status')}]")

    def issue_books(self):
        print("___________----Welcome----___________\n")
        print("\t\t ISSUING OF BOOKS")
        print('________________________________________')

        book_ID = str(input("Type In Book ID You Will Like to Get: "))

        if str(book_ID) in self.transaction_dict.keys():
            if self.transaction_dict [book_ID] ['Status'] != "Available":
                print(f"This Book has already been issued to {self.transaction_dict[book_ID] ['Lender_name']} on {self.transaction_dict[book_ID] ['Issue_date']}")
            else:
                your_name = input("What is your name: ")
                current_date = datetime.datetime.now().strftime("%Y-%M-%D  at around:%H:%M:%S")
                self.transaction_dict[book_ID]["Lender_name"] = your_name
                self.transaction_dict[book_ID]["Issue_date"] = current_date
                self.transaction_dict[book_ID]["Status"] = "Unavailable"
                print(f"Book has been Issued to {your_name} Sucessfully!!!")
        else:
            print("ID is not correct, check again")

    def return_books(self):
        """
        To return the books to the library we would make use of the books ID
        We would check if the book ID matches any of the already made ID's in the database
        If it matches we check if it's status is available
        If Available:
            We say book already available in library
        if not:
            We access the dictionary to update it changing the status of the book to available,
            The lender name to an empty string,
            The Issue date to an empty string
        """

        #implent!
        print("!\n -----------------WELCOME TO THE RETUERN DESK---------------- \n")
        book_ID = input("What Book would you like to return:_ ")

        if book_ID in self.transaction_dict.keys():
            if book_ID in self.transaction_dict [book_ID] ["Status"] == "Available":
                print(f"This Book is already in the Library, Book {book_ID} not issued!")
            else:
                self.transaction_dict [book_ID] ["Status"]= "Available"
                self.transaction_dict[book_ID] ["Lender_name"] = ""
                self.transaction_dict[book_ID] ["Issue_date"] = ""
                print(f"Book {book_ID}- {self.transaction_dict[book_ID] ['Book_title']} has been returned!\n")
                print("Thank You👍 \n")
        else:
            print("Check Well, Book ID doesn't exist!!! ")


try :
    l = Transaction('library_books.txt')
    

    choice_key = False

    while not choice_key == 'q':
        print("""
            Press S to Check Books Available in the Library
            Press I to Issue Books In The Library
            Press R to Return Book to The Library
            Press Q to Quit
          """)
        
        choice_key = input("What would you like to do in the library today:_ ").lower()

        if choice_key == "s":
            print("Checking Books Available in the Library!\n")
            l.library_state()
        elif choice_key == "i":
            print("Issuing Books from the Library!\n")
            l.issue_books()
        elif choice_key == "r":
            print("Return Books!\n")
            l.return_books()
        elif choice_key == "q":
            print("""
                  Closing Programme!

                  THANK YOU 🚀
                  """)
            break
        else:
            continue
    
except Exception as e:
    print("Something Went Wrong")

        








