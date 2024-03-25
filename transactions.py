from primary import Member


class Transaction: 
    Transact = []
    def __init__(self, member:str, book_taken:str, issue_date:str, return_date:str = None):
        self.member = member
        self.book_taken = book_taken
        self.issue_date = issue_date
        self.return_date = return_date

        self.member_name = Member.name
        Transaction.Transact.append(self)



    def __repr__(self):
        return f"{self.__class__.__name__}('{self.member}', '{self.book_taken}', '{self.issue_date}', '{self.return_date}', '{self.member_name}')"



pay1 = Transaction('camel', 'a major growth', '12-12-23')


