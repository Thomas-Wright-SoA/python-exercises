def get_number():
    n = None
    while True:
        n = input("Input a number: ")
        try:
            int(n)
            break
        except ValueError:
            print("A valid interger")
    return int(n)

n = get_number()

for i in range(10):
    i += 1
    print(f"{n} x {i} = {n * i}")