def get_number():
    n = None
    while True:
        n = input("Number: ")
        try:
            float(n)
            break
        except ValueError:
            continue
    return n

def get_operator():
    operator = None
    while True:
        operator = input("Operator: ").lower()
        if operator in ['+', '-', '/', '*']:
            break
        elif operator == 'q':
            exit()
    return operator

print("""How to use this calculator:
      - When prompted for a number enter a number
      - When prompted for a operator you can choose from the following options
      -- [+] - Addition
      -- [-] - Subtraction
      -- [*] - Multiply
      -- [/] - Divide
      -- [q] - Quit""")

result = get_number()
while True:
    operator = get_operator()
    operand = get_number()
    result = str(eval(result + operator + operand))
    print(f"Result: {result}")



