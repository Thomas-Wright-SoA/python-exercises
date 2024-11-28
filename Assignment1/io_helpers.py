# Displays [message] and prompts user for Y/N input, repeats until valid input received
# returns 'yes' for 'y' and 'no' for 'n'
def ask(message):
    user_input = None
    while True:
        user_input = input(f"{message} [Y/N]: ").lower().strip()
        if user_input in ['y', 'n']:
            if user_input == 'y':
                return 'yes'
            else:
                return 'no'
        else:
            print("Invalid input")

# Prompts user with message, only accepts a int in [num_range]
def get_int_in_range(message, num_range):
    user_input = None
    while True:
        user_input = input(message).strip()

        if user_input.replace(".", "").isnumeric() == True:
            print("Sorry, whole numbers only please...")
            continue

        try:
            user_input = int(user_input)
        except:
            print("That's not a number...")

        if user_input not in num_range:
            print(f"Input a number between {min(num_range)} and {max(num_range)}")
            continue
        return user_input

