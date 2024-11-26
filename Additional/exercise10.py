text = input("Enter a sentence: ").strip()

count = 0
for char in text:
    if char.isalpha():
        count += 1

print(f"There are {count} characters in the sentence")