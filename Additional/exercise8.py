word = input("Enter a word: ").strip().lower()

is_palindrome = word == word[::-1]

if is_palindrome:
    print("Yes")
else:
    print("No")

