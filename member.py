import csv
#This is the member class

class Member:
    """
    This class would be in charge of the library's Member
    A CSV file which would contain the Members Name and Contact details 
    """
    keep = []
    def __init__(self, mem_base):
        self.mem_base = 'member.csv'

        self.mem_dict = {}
        user_key = 101
        with open(self.mem_base) as db:
            read = csv.reader(db)

            for line in read:
                self.mem_dict.update({str(user_key) : {"name":line[0], "member_ID":line[1], "phone_details":line[2], "email":line[3]}})
                user_key = user_key + 5

    def member_details(self):
        print("\t\t--------_______Welcome_________--------")
        
        for keys, values in self.mem_dict.items():
            print(f"{keys} \t  {values['name']} \t -{values['member_ID']} \t -{values['phone_details']} \t  -{values['email']}")

    def search_members(self):
        print("Member Is To be identified by their name!\n")
        print("!!!!\t\t ⚠ Each Name must start with a capital letter in ordrer to find it! \n\n")

        mem_key = input("Type in Member Key: ")

        if not mem_key in self.mem_dict.keys():
            print("Member Name is not found in database")
        else: 
            print(f"Member name is {self.mem_dict [mem_key] ['name']} Member ID is {self.mem_dict [mem_key] ['member_ID']}  Their Phone details: {self.mem_dict [mem_key]['phone_details']} Member email is {self.mem_dict[mem_key]['email']}")
                    
        
    # def add_member(self):
    #     """
    #     This add member method adds new member details by :
    #     reading the csv
    #     writing to the csv
    #     and adding data to the csv
    #     """

    #     def read_file(file):
    #         """Read data from the csv file"""
    #         with open (file, 'r', newline= '') as rf:
    #             r_file = csv.reader(rf)
    #             file_r = list(r_file)
    #         return file_r

    #     def write_to_csv(file, new_data):
    #         with open(file, 'w', newline='') as wf:
    #             w_file = csv.writer(wf)
    #             w_file.writerows(new_data)

    #     def add_data_to_file(file):
    #         existing_file = read_file(file)

    #         new_data = input("Enter new data (seperate name , phone and email with comma's):").split(',')

    #         existing_file.append(new_data)

    #         write_to_csv(file, existing_file)

    #     add_data_to_file(self.mem_base)

    #     print("User has been added to data base")
        
    
    # def __repr__(self):
    #     return f"{self.__class__.__name__}, {self.mem_base}"
    
