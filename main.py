import sys
from igets import igets
from datamanager import Account, Register
class CLI: # not very practicaç
    def __init__(self):
        self.current_account = None

    def displayMenu(self):
        print("\nMenu:")
        print("1. Create Account")
        print("2. Load Account")
        print("3. View Account Info")
        print("4. Change Account Name")
        print("5. Premium Features")
        print("6. Save Account")
        print("7. Exit")
    
    def createAccount(self):
        name = igets.Str("Enter account name: ")
        bank = igets.Str("Enter bank name: ")
        agency = igets.Str("Enter agency number: ")
        is_premium = igets.Str("Is this a premium account? (y/n): ").lower() == 'y'

        self.current_account = Account(name, bank, agency, is_premium)
        print(f"Account {self.current_account.name} created successfully.")

    def loadAccount(self):
        username = igets.Str("Enter the username to load: ")
        self.current_account = Register.loadAccount(username)

    def viewAccountInfo(self):
        if self.current_account:
            self.current_account.showInfo()
        else:
            print("No account loaded.")

    def changeAccountName(self):
        if self.current_account:
            self.current_account.changeAccountName()
        else:
            print("No account loaded.")

    def premiumFeatures(self):
        if self.current_account:
            self.current_account.doPremiumStuff()
        else:
            print("No account loaded.")

    def saveAccount(self):
        if self.current_account:
            Register.saveAccount(self.current_account)
        else:
            print("No account to save.")

    @staticmethod
    def exitApplication():
            print("==========\nExiting...\n==========")
            
            sys.exit(0)

    def run(self):
        while True:
            self.displayMenu()
            choice = igets.Str("Choose an option: ")

            
            if choice == "1":
                self.createAccount()
            elif choice == "2":
                self.loadAccount()
            elif choice == "3":
                self.viewAccountInfo()
            elif choice == "4":
                self.changeAccountName()
            elif choice == "5":
                self.premiumFeatures()
            elif choice == "6":
                self.saveAccount()
            elif choice == "7":
                CLI.exitApplication()
            else:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    cli = CLI()
    cli.run()