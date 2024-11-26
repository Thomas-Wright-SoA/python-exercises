while True:
    print("""Please choose from the following options:
[1] Say hello
[2] Add numbers
[3] Quit\n""")
    
    option = input("Option: ")
    print()
    if option == '1':
        print("Hello\n")
    if option == '2':
        numbers = input("Enter 2 numbers seperated with a space: ").strip().split()
        print(f"{int(numbers[0]) + int(numbers[1])}\n")
        
    if option == '3':
        exit()