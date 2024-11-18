class igets:

    @staticmethod
    def Str(msg):
        while True:
            user_input = input(msg).strip()

            if user_input == "":
                print("(igets) Input cannot be empty.")
                continue

            return user_input
        
    @staticmethod    
    def Int(msg):
        while True:
            user_input = igets.Str(msg)

            try:
                user_input = int(user_input)
                return user_input
            
            except ValueError:
                print("(igets) Input must be an integer.")