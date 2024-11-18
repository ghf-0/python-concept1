li = [
    {
        "name": "Jim",
        "age": "22"
    },
    {
        "name": "Jam",
        "age": "24"
    }
]

def fetchUser(name):
    for users in li:
        if users["name"] == name:
            print(f"Found user {users["name"]}")
            return users
    
    print("FAILED!")
    return {}

u = fetchUser("Jim")
if type(u) == dict:
    print(u)