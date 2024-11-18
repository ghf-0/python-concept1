class Account:
    def __init__(self, name, bank, agency, is_premium):
        self.name = name
        self.bank = bank
        self.agency = agency
        self.is_premium = is_premium

test_account = Account("Rutger", "0246", "102", False)

def getString(msg):
    while True:
        string = input(msg).strip()

        if string == "":
            print("Input cannot be empty.")
            continue

        return string

def editName(acc):
    new_name = getString("Enter new name: ")
    
    acc.name = new_name
    print(f"NAME UPDATED: {acc.name}")

print(test_account.name)
editName(test_account)
print(test_account.name)