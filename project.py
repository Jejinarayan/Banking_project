class bank():
    def __init__(self,username,password,balance=5000):
        self.username = username
        self.password = password
        self.balance = balance
    def checkpassword(self,password):
      return self.password == password
    def deposit(self,deposit_amount):
        self.deposit_amount = deposit_amount
        self.balance = deposit_amount + self.balance
        print("--------------------------")
        print("amount credited:", self.deposit_amount)
        print("Available balance: ", self.balance)
    def withdraw(self,withdraw_amount):
        self.withdraw_amount = withdraw_amount
        withdraw_amount = self.balance - w_amount
        print("--------------------------")
        print("amount withdraw: ",w_amount)
        print("Available balance: ", withdraw_amount)
        self.balance = withdraw_amount
    def bal(self,bal_enq):
        self.bal_enq = bal_enq
        bal_enq = total+ self.balance
        print("--------------------------")
        print("Your available bal:",bal_enq)
    def mini(self,dep_amt,with_amt):
        self.dep_amt = dep_amt
        self.with_amt = with_amt
        dep_amt = st + self.deposit_amount
        with_amt = total + w_amount
        print("--------------------------")
        print("Your recent transactions: ")
        print("Deposit amount: ", dep_amt)
        print("Withdraw amount: ", with_amt)
        print("Your account bal: ",self.balance)
        print("--------------------------")

total = (0)
st = (0)
accounts = []
login=None
while True:
    print("Welcome to Python bank")
    print("1.Creat Account\n 2.Login")
    option = int(input("Welcome to python bank,Enter option: "))
    if option ==1:
        username=input("Enter username: ")
        password=int(input("Enter password: "))
        accounts.append(bank(username,password))
        print(f"{username} your account has been succesfully created")
    elif option==2:
        username=input("Enter username: ")
        password=int(input("Enter password: "))
        for i in accounts:
            if i.username==username and i.checkpassword(password):
                login=accounts
                print(f"{username} Login successfully")
                break
        if login is None:
            print("Enter valid credantials")
        else:
            print("Welcome to python bank")
            break
    else:
        print("Please enter valid option")
    break

while True:
    choice = int(input("To continue banking type 1, or 2 for exit:"))
    if choice == 1:
        print("--------------------------")
        print("1.Deposit")
        print("2.Withdraw")
        print("3.Balance Enquiry")
        print("4.Ministatemant")
        option = int(input("Enter the option: "))
        if option == 1:
            for i in accounts:
                if i.username==username and i.checkpassword(password):
                    dep= int(input("Enter amount to deposit: "))
                    i.deposit(dep)
        elif option == 2:
            for i in accounts:
                if i.username==username and i.checkpassword(password):
                    w_amount = int(input("Enter withdraw amount: "))
                    i.withdraw(w_amount)
        elif option == 3:
            for i in accounts:
                if i.username==username and i.checkpassword(password):
                    i.bal(total)
        elif option == 4:
            for i in accounts:
                if i.username==username and i.checkpassword(password):
                    i.mini(st,total)
        else:
            print("Please enter valid option")
    elif choice == 2:
        break
    else:
        print("Please enter valid option")
