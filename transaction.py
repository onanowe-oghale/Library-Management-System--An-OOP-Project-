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


