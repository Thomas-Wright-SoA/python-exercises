import random

def get_number():
    n = None
    while True:
        n = input("Guess a number: ")
        print()
        try:
            int(n)
            break
        except ValueError:
            print("A valid interger")
    return int(n)

MAXATTEMPTS = 10
MAXNUMBERS = 5
MAXRANDOMNUM = 20
numbers = []
attempts = MAXATTEMPTS

for i in range(MAXNUMBERS):
    random_number = random.randint(1, MAXRANDOMNUM)
    while random_number in numbers:
        random_number = random.randint(1, MAXRANDOMNUM)
    numbers.append(random.randint(1, MAXRANDOMNUM))
    
print(numbers)

print(f"""Here I have a list of {MAXNUMBERS} random numbers 1-{MAXRANDOMNUM}
I will give you {MAXATTEMPTS} attempts to guess all {MAXNUMBERS}\n""")

while attempts > 0:
    n = get_number()
    attempts -= 1
    if n in numbers:
        print(f"{n} is in the list of numbers\n")
        numbers.remove(n)
    else:
        print(f"Nope {n} is not in there\n")
    numbers_remaining = len(numbers)
    if numbers_remaining == 0:
        break
    print(f"You have {attempts} remaining attempts and {numbers_remaining} numbers left to find\n")

remaining_numbers = len(numbers)

if remaining_numbers == 0:
    print(f"You found all the numbers in {MAXATTEMPTS - attempts} attempts")
else:
    print(f"You found {MAXNUMBERS - remaining_numbers} out of {MAXNUMBERS} numbers")
