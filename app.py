import sys
from igets import igets
from datamanager import Account, Register

class Command:
    def __init__(self, name, action, description):
        self.name = name
        self.action = action
        self.description = description

class App:
    def __init__(self):
        self.name = "py-concept-1"
        self.current_account = None
        self.commands = [
            Command("new", self.createAccount, "Create new profile"),
            Command("load", self.loadAccount, "Load profile"),
            Command("info", self.viewAccountInfo, "Displays data information about the currently loaded profile"),
            Command("rename", self.changeAccountName, "Rrename current profile"),
            Command("premium", self.premiumFeatures, "Access premium menu if available"),
            Command("save", self.saveAccount, "Saves current profile data"),
            Command("delete", self.deleteAccount, "Deletes saved accounts based on name input"),
            Command("exit", self.exitApplication, "Shuts down"),
            Command("help", self.displayInfo, "Displays all available commands")
        ]

    def handleCommand(self, inpt):
        for command in self.commands:
            if command.name == inpt:
                command.action()
                return
        
        print(f"'{inpt}' is not a recognized command")

    
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

    def deleteAccount(self):
        username = igets.Str("Enter account name: ")
        Register.deleteAccount(username)

    def displayInfo(self):
        print("\nCOMMAND LIST\n")
        for command in self.commands:
            print(f"-{command.name}\t\t{command.description}.")

    def exitApplication(self):
            print("\n==========\nExiting...\n==========")
            
            sys.exit(0)

