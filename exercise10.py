def check_n(n):
    if int(n) % 2:
        return "odd"
    return "even"

n = None
while True:
    n = input("Enter a number: ").strip()
    try: 
        int(n)
        break
    except ValueError:
        try:
            float(n)
            print("No floats!")
        except ValueError:
            print("No strings!")

result = check_n(n)
print(f"{n} is a {result} number")



