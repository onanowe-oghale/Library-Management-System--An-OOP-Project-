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
        Id = 1020#(so it tallies with the ID from the Library_Books class)

        with open(self.library_books) as bk:
            line = bk.readlines()

        for lines in line:
            self.transaction_dict.update({str(int(Id)+1): {"Book_title": lines.replace("\n", ""), "Status": "Available", 
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

        book_ID = input("Type In Book ID You Will Like to Get: ")

        if book_ID in self.library_dict.keys():
            if not self.library_dict [book_ID] ['Status'] == "Available":
                print(f"This Book has already been issued to {self.library_dict[book_ID] ['Lender_name']} on {self.library_books[book_ID] ['Issue_date']}")
            else:
                your_name = input("What is your name: ")
                current_date = datetime.datetime.now().strftime("%Y%M%D%H%M%S")
                self.library_dict[book_ID]["Lender_name"] = your_name
                self.library_dict[book_ID]["Issue_date"] = current_date
                self.library_dict[book_ID]["Status"] = "Unavailable"
                print(f"Book has been Issued to {your_name} Sucessfully!!!")
        else:
            print("ID is not correct, check again")

    def return_books(self):
        pass



l = Transaction('library_books.txt')
l.issue_books()

        








