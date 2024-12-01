from pathlib import Path
from igets import igets
import json

class Account:

    def __init__(self, name, bank, agency, is_premium):
        self.name = name
        self.bank = bank
        self.agency = agency
        self.is_premium = is_premium

    def showInfo(self): #this is useless
        print(f"{self.name}\n{self.bank} {self.agency}\n{"Premium" if self.is_premium else "Not premium"}")

    def serialize(self):
        json = {
            "name": self.name,
            "bank": self.bank,
            "agency": self.agency,
            "isPremium": self.is_premium
        }

        return json
    
    def userConfirmDecision(self, action):
        choice = input(f"Are you sure you want to {action}?").lower()

        if choice == "y":
            return True
        
        else:
            return False
    
    def changeAccountName(self):
        new_name = igets.Str("Enter new name: ")

        if self.userConfirmDecision("change this account's name"):
            self.name = new_name
            print(f"Account's name has been changed to {self.name}")
        else:
            print("Operation cancelled.")
            return

    def doPremiumStuff(self):
        if self.is_premium:
            print(f"{self.name} can do premium stuff!")
            return
        
        print("This account is not premium.")

   


class Register:
       
    @staticmethod
    def saveAccount(account):
        if Path('data.json').is_file():
            data = Register.loadJson()
            account_json = account.serialize()

            data.append(account_json)

            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
                print(f"Account information saved. {account.name}")
        else:
            print("ERROR: Unable to locate file data.json\nAborting save")

    @staticmethod
    def loadJson():
        if Path('data.json').is_file():
            with open('data.json', 'r') as file:
                data = json.load(file)
                return data
        
        else:
            print("File not found.")
            return {}

    @staticmethod   
    def loadAccount(username):
        data = Register.loadJson()
        #print(data)

        for accounts in data:
            if accounts["name"] == username:
                loaded_account = Account(accounts["name"], accounts["bank"], accounts["agency"], accounts["isPremium"])
                print(f"==Account loaded== {accounts["name"]}")
                return loaded_account

        print("User not found...")

    @staticmethod
    def deleteAccount(username):
        data = Register.loadJson()

        updated = [account for account in data if account["name"] != username]

        if len(updated) == len(data):
            print(f"Account not found: {username}")
        
        else:
            with open('data.json', 'w') as file:
                json.dump(updated, file, indent=4)
            
            print(f"{username} account has been deleted.")