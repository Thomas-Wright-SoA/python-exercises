names = []

while True:
    new_name = input("Please enter a name: ")
    names.append(new_name)
    to_continue = input("Would you like to add another name? [Y / N] ").lower()
    if to_continue == "n":
        break

for name in names: print(f"Hello, {name}.")