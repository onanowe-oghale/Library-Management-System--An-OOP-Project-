import time #the time module helps with interaction with our code, it helps to slow down how things are shown
            #and helps the reader be able to see things happening in the terminal.



#importing modules built for the library


from library import Library_Books
from member import Member
from transaction import Transaction


"""
Methods from the Library class:
    -Display Books: display_book()
    -Add Books: add_books()
    -Delete Books: delete_book()

Methods from the Member class :
    -Member details: member_details()
    -Search: search_member()

Methods from the Transaction class:
    -Library State: library_state()
    -Issue Books: issue_books()
    -Return Books: return_book()
"""

#instantiate the objects

#objects are made from the classes passing the necessary files as the needed argument
My_library = Library_Books('library_books.txt')
My_member = Member('member.csv')
My_transaction = Transaction('library_books.txt')


#try this code
try:
    lib_name = input("Type In Library Name to continue😁: ")
    time.sleep(2)
    print(f"\n-----------_________Welcome To {lib_name} Library Management System💡________--------------\n\n")

    lib_dict = {"B": "Handle Books", "M": "Member Handling", "T": "Book Transactions", "E": "End"}
    
    lib_choice = False
    while not (lib_choice == 'e'):# as long as the input is not e do the loop
        for keys, values in lib_dict.items():
            print(f"Press {keys} to {values}")
        lib_choice = input("\n What Would You Like To Do In The Library Today?😁_ ").lower()

        if lib_choice == 'b': #if it is b the Libary_Books class and its methods are accessed
            print(f"Welcome to the {lib_name} Library Book Handler\n📖📕")
            b_choice = False

            while b_choice != 'q':
                print("""
                        📕
                        Press D to Display Books
                        Press A to Add Books
                        Press DB to Delete Books
                        Press Q to Quit Or Go Back
                        ⌛                      ⏳
                    """)
                
                #when inner choices are inputed the code block inside each is executed
                b_choice = input("Type In Command:_ ").lower()
                
                #displays the books
                if b_choice == 'd':

                    print("Displaying Books!📕😁\n ")
                    time.sleep(1)
                    My_library.display_books()
                
                #Adds books
                elif b_choice == 'a':
                    print("Adding Books!➕📕 \n ") 
                    time.sleep(1)
                    My_library.display_books()
                

                #delete books
                elif b_choice == 'db':
                    print("Delete Books ⚠📕\n")
                    time.sleep(1)
                    My_library.delete_book()
                
                #quits the operation, basically exitting this inner while loop
                elif b_choice == 'q':
                    print("Quitting............📕🚀")
                    time.sleep(1.5)
                    break
                
                #gives a message that the inputted key is not correct and continues the loop
                else:
                    print("Choice is invalid, try again📕🤲🏿\n")
                    continue
        
        #when m is inputed the Member class is being accessed
        elif lib_choice == 'm':
            print(f"Welcome To the {lib_name} Library Member Handler📕😁\n")
            
            m_choice = False

            while m_choice != 'q':
                print("""
                    Press D for all Member details
                    Press S to search For a Member 
                    Press Q to quit or go back   
                    """) 
                
                m_choice = input("What Would You like to do?_ ").lower()  #when inner choices are inputed the code block inside each is executed
                time.sleep(0.5)
                
                #this helps to access all available member details
                if m_choice == 'd':
                    print("\n Acessing All Member Details!📕⚡ \n")
                    time.sleep(1)
                    My_member.member_details()
                
                #this is to search for the members
                elif m_choice == 's':
                    print("\n Member Search📕🔎\n")
                    time.sleep(1)
                    My_member.search_members()
                
                #ends the member handling part, basically leaving the while loop!
                elif m_choice == 'q':
                    print("Quitting......📖")
                    break
                
                #gives an error message and continues the loop
                else:
                    print("Invalid Choice!❗❗❌")
                    continue
        
        #when choice is t the Transaction class is accessed with its methods
        elif lib_choice == 't':
            print(f"Welcome to {lib_name} library transaction Handler📕💡 \n")

            l_choice = False
            l_c_dict = {"S":"Access Library Book State", "I":"Issue Book", "R":"Return Book", "Q": "Quit"}

            #as far as the input is not q perform this
            while not l_choice == 'q':
                for keys, values in l_c_dict.items():
                    print(f"Press {keys} to {values}\n")

                l_choice = input("Press Your choice📕: ").lower() #when inner choices are inputed the code block inside each is executed

                #this is to access all the books in the library if they are available or not
                if l_choice ==  's':
                    print("Accessing Books!🔎📕\n")
                    time.sleep(1)
                    My_transaction.library_state()

                #this is to issue the books in the library 
                elif l_choice == 'i':
                    print("Issue Books!📕📕 \n")
                    time.sleep(1)
                    My_transaction.issue_books()

                #this is to return books that were issued
                elif l_choice == 'r':
                    print("Return Books!📕📌 \n")
                    time.sleep(1)
                    My_transaction.return_books()

                #this helps to quit the inner while loop
                elif l_choice == 'q':
                    print("Quitting!👍📕")
                    break
                
                #gives an error message and continues the loop
                else:
                    print("Invalid choice, Try again!❌❗❌ ")
                    continue
        
        #ends the entire loop totally
        elif lib_choice =='e':
            print("Ending!Library operations...............📕")
            time.sleep(0.7)
            print("Thank You.................")
            break

        #this displays and error message for wrong input and continues the loop 
        else:
            print("Wrong Input, Try again💥")
            continue

#raises an exception message if the code in the try block goes wrong.
except Exception as e:
    print("Wrong Key")


