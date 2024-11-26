vowels = ['a', 'e', 'i', 'o', 'u']

text = input("Enter some text: ")

count = 0

for char in text:
    if char in vowels:
        count += 1

print(f"The text contains {count} vowels")