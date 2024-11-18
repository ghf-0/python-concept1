class CLI:

    @staticmethod
    def handleCommand(user_input, user):
        command = CLI.commands.get(user_input)

        if command:
            command.execute(user)
        else:
            print(f"Unknown command: {user_input}")