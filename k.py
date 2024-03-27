#importing the date and time module which helps to state the current date and time in a given program
import datetime
#importing the OS module
import os

#making the class called Lms
class Lms:
    #a docstring talking about what the class does and the methods available in the class
    """This class is used to keep record of the books library
    It will have total of four modules which are Display books, issue books, return books, add books"""

    #the __init__ used to initialize the instance variables
    def __init__(self, list_of_books, library_name):
        
        #the list of book variable is set to a txt file which contains the list of book in the library the self makes it an instance variable
        self.list_of_books = "list_of_books.txt"
        
        #the library name attribute is set to an instance form called in the class
        self.library_name = library_name

        #a variable that is not an argument passef in the function is being passed
        #it is an empty dictionary which would contain the information for the books

        self.books_dict = {} #this dictionary will help to hold the information of the books: like book title, lender name, issue date
       
        #this Id variable is another instance variable that is used to give the books specific identifiers 
        Id = 1011 

        #file handling

        #with file handling we are able to collect the instance variable (self.list_of_books) which contains the txt file where the list of books are located.

        #this opens the file and sets it to a variable bk
        with open(self.list_of_books) as bk:
            
            #this collects each line of the file, reads them and sets them to a variable called content
            content = bk.readlines()
        
        #this is a for loop that loops each line of the file already placed in the content variable
        
        #the loop means for each line in the already read lines of the content variable do these:
        for line in content:

            #the empty dictionary which was the self.books_dict which was not passed as an argument in the __init__ function

            #this line of code basically updates the dictionary with a new Id for each book

            #the library is update with a key which is Id converted to string and 4 key and value pairs in it as the 
            #values of the Id key,
            #the line.replace("\n", "") means for each next line replace it with nothing as the previous readlines function gives a space
            #so the empty string means replace with nothing
            self.books_dict.update({str(Id): {"book_title": line.replace("\n", ""),
                                              
            #the lender name key has a value of an empty string which would bw updated when someone borrows a book
            #the Issue date key also does the same thing which means it will be updated on the day someone comes to get the books
            #the status key has a value of available which helps the user know if the book is available or not 
                                     
            "Lender_name": "", "Issue_date":"", "Status":"Available" }})
            Id = Id + 1 #this id variable adds 1 to each of its value as it is assigned to each book - this is the main key remember,
            #the for loop makes this possible


    #this is a display book method that display the books available in the library and shows if they are available or not
    def display_books(self):

        #this is some string the gives a heading list of books and seperates the Book's ID and the book's title
        print("______________________________---List Of Books---____________________________")
        #the books Id remember is the major key in the self.book_dict dictionary 
        #the \t is used to move four spaces before the title stirng is placed
        print("Books ID", "\t", "Title")
        print('-----------------------------------------------------------------------------')


        #this is a for loop loops of the self.books dictionary with the .items(),

        for key,values in self.books_dict.items():

            #after looping over the dictionary this prints the major key (Id)
            #then gives to spaces of four with the two \t\t
            #then it gets the value of the book title which is the names of the book in the txt file
            #the gets the values of the of the status whether it is available or not.
            print(f"{key}: \t\t {values.get('book_title')} - [{values.get('Status')}]")

    #this makes a function called issue books which would take a self argument(it is an instance method all instance methods must take the self argument)
    
    def Issue_books(self):

        #remember the books Id is the book key so the Isuue a book the book Id should be entered first,
        books_Id = input("Enter books ID: ")

        #this uses the datetime module to get the current year month, date, hour, minute and second the book is being issued
        #I take the strftime as meaning string for time😂,
        #it get the time thanks to the date time module and assigns it to the current_date variable
        current_date = datetime.datetime.now().strftime("%Y-%M-%D %H:%M:%S")

        #this line of code checks if the given book Id exists in the dictionary
        if books_Id in self.books_dict.keys():

            #if the given book Id exists in the dictionary and is not available
            if not self.books_dict[books_Id] ["Status"] == 'Available':

                #this lines prints the that the given book given is not available and 
                #one thing to notice is the use of the books_Id that is the major, identifier the key of the dictionary
                #the lender_name in double quotes is a value which is a key to a certain value but it is accessed with the major key books_Id
                #the same applies for the issue books it gives out the details as have been updated in the library
            
                print(f"This book is already issued to {self.books_dict [books_Id] ['Lender_name']} on {self.books_dict [books_Id] ['Issue_date']}")
            
                #this is like recursion calling a function in a function, the function is called with self
                return self.Issue_books
            
            #if the book however is available in the txt file:
            elif self.books_dict [books_Id]["Status"] == 'Available':
                
                #intending borrower is asked for their name
                your_name = input("Please enter you name: ")

                #the name is added to the Lender name in the dictionary with the Lender name key
                self.books_dict [books_Id] ["Lender_name"] = your_name

                #the current date which is gotten from the date time module is assigned as a value to the dictionary
                self.books_dict [books_Id] ["Issue_date"] = current_date

                #the status of the books which is about to be taken is now changed to Not available
                self.books_dict [books_Id] ["Status"] = "Not Available"

                #the book is now given
                print(f"Books Issued Succesfully!!! on {current_date} to {your_name}")
        
        #if the given Id doesn't match what is in the book
        else:

            #prints a message that the book Id is not founc
            print("Book ID not found") 

            #recursion like and then calls the Issue books method to begin again.
            return self.Issue_books()  

    #this adds new books from someone donating to the library, it updates the books coming in 
    def add_books(self):
        #asks for the book title
        new_books = input("Enter Books Title: ")

        #if the new book is an empty string it can't be added
        if new_books == "":

            #the method is then called again
            return self.add_books()
        
        #if the length of the name of the book is more than 30 it is not allowed to be added
        elif len(new_books) > 30:

            #the message is printed
            print("Books title length is too length | Title shouls not be more than 30 characters")

            #the function is called again
            return self.add_books()
        
        #if the book name given is not an empty string and it is less than 30 characters then this happens
        else:

            #with file handling the dictionary which contains the book is opened, 
            #the "a" means that you about to append and the the lines is assigned to the k variable

            with open(self.list_of_books, "a") as bk:

                #this writes new lines to the files and which is the content of the name written in the new book variable 
                bk.writelines(f"{new_books}\n")

                #this updates the content of the files with the dictionary 
                #with updates the Id of the books by adding one to the already available max number of books assigning that value to the new book to be added
                #the book title is updated with the new book variable content, 
                #the lender name is updated with an empty string
                #the issue date updated because it has not been issued to anyone , the status is given as available,

                #remember everything is one dictionary with the Id as the main key and the values of that main key being 4 key value pairs,
                self.books_dict.update({str(int(max(self.books_dict))+1):{"book_title": new_books, "Lender_name":"", "issue_date": "", "Status": "Available"}})
               
                #this prints that the new book has been added
                print(f"This Books '{new_books} has been added successfully !!!'")
    
    #this is an instance method that helps to return books
    def return_books(self):
        #this asks for the books ID using it as an identifier for the books already in the dictionary
        books_Id = input("Enter BooK ID: ")

        #if the given id given exists in the dictionary remember they were the main keys
        if books_Id in self.books_dict.keys():
            
            #if from the existing book Id the status is available then it doesn't need to be returned it wasn't issued
            if self.books_dict[books_Id]["Status"] == "Available":

                #print the message that the book is available
                print("This book is already available in the library. Please check your book ID. ")
                
            #if the status of the book is not available then    
            elif not self.books_dict[books_Id] ["Status"] == "Available":

                #change the lenders name to an empty string 
                self.books_dict[books_Id] ["Lender_name"] = ""

                #change the issue date to an empty string
                self.books_dict[books_Id] ["Issue_date"] = ""

                #restore the availability status of the book to available
                self.books_dict[books_Id] ["Status"]  = "Available"

                #give a message that the book has been returned succesfully
                print("Book has been successfully Returned! \n")
        
        #if the given Id is not in the library give the error message!
        else:
            print("Book ID is not in library!")


#this trys the block of code inside it
try:
    #this is instantiating the class to an object called made,
    Made = Lms("list_of_books.txt", "Town Library")

    #this is a dictionary that gives options of what to perform on the books!
    press_key_list = {"D" : "Display Books", "A": "Add Books", "I" :"Issue Books", "R": "Return Books", "q": "Quit"}

    #the variable key_press is set to False
    key_press = False

    #while the key press is not q which means while it is not true
    while not(key_press == "q"):

        #prints the a welcome message along with the libraries name
        print(f"\n___________---------Welcome To {Made.library_name} Library Management System!-------__________\n")

        #loops over the keys in the dictionary
        for key, value in press_key_list.items():
            #prints the key and everyone of its values in the dictionay
            print(f"Press {key} To {value}")
        #this is the key press variable as and it asks for input on the users choices and changes the input into lowercase
        key_press = input("Press Key ").lower()

        #when the key press aligns with I the issue books method is been run
        if key_press == "i":
            print("Current Selection: Issue Books \n")
            Made.Issue_books()

        #when the key press aligns with D the display book method is run
        elif key_press == "d":
            print("Current Selction: Display Books \n")
            Made.display_books()

        #when the key press aligns with a the add books method is run
        elif key_press == "a":
            print("Current Selection: Add Books \n")
            Made.add_books()

        #when the key press aligns with r the return book method is run
        elif key_press == "r":
            print("Current Selection: Return Books \n")
            Made.return_books()

        #when the key press aligns with q the whole loop breaks and in quits
        elif key_press == "q":
            break

        #if none of the elif and the if isn't met then the loop continues
        else:
            continue

#this catches exceptions with the base class Exception and assigns it to a variable e 
except Exception as e:

    #the variable enables this message to be shown.
    print("Something went wrong check your input!!! \n")
        

#class is being instantiated to make an object called L
L =Lms('list_of_books.txt', 'Dams Library')

#the object calls a method
L.Issue_books()