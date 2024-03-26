import datetime
import os

class Lms:
    """This class is used to keep record of the books library
    It will have total of modules which are Display books, issue books, return books, add books"""

    def __init__(self, list_of_books, library_name):
        self.list_of_books = "list_of_books.txt"
        self.library_name = library_name
        self.books_dict = {} #this dictionary will help to hold the information of the books: like book title, lender name, issue date
        Id = 1011 

        #file handling
        with open(self.list_of_books) as bk:
            content = bk.readlines()
        for line in content:
            self.books_dict.update({str(Id): {"book_title": line.replace("\n", ""),
            "Lender_name": "", "Issue_date":"", "Status":"Available" }})
            Id = Id + 1

    def display_books(self):
        print("______________________________---List Of Books---____________________________")
        print("Books ID", "\t", "Title")
        print('-----------------------------------------------------------------------------')

        for key,values in self.books_dict.items():
            print(f"{key}: \t\t {values.get('book_title')} - [{values.get('Status')}]")

    def Issue_books(self):
        books_Id = input("Enter books ID: ")
        current_date = datetime.datetime.now().strftime("%Y-%M-%D %H:%M:%S")
        if books_Id in self.books_dict.keys():
            if not self.books_dict[books_Id] ["Status"] == 'Available':
                print(f"This book is already issued to {self.books_dict [books_Id] ["lender_name"]} on {self.books_dict [books_Id] ["Issue_date"]}")
                return self.Issue_books
            elif self.books_dict [books_Id]["Status"] == 'Available':
                your_name = input("Please enter you name")
                self.books_dict [books_Id] ["lender_name"] = your_name
                self.books_dict [books_Id] ["Issue_date"] = current_date
                self.books_dict [books_Id] ["Status"] = "Not Available"
                print("Books Issued Succesfully!!! \n")
        else:
            print("Book ID not found") 
            return self.Issue_books()  

    def add_books(self):
        new_books = input("Enter Books Title: ")

        if new_books == "":
            return self.add_books()
        elif len(new_books) > 30:
            print("Books title length is too length | Title shouls not be more than 30 characters")
            return self.add_books()
        else:
            with open(self.list_of_books, "a") as bk:
                bk.writelines(f"{new_books}\n")
                self.books_dict.update(str)


L =Lms('list_of_books.txt', 'Dams Library')
L.display_books()