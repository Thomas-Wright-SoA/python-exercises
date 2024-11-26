text = "   Hello, World! Welcome to Python coding.   "

text = text.strip()

print(text.count("o"))

print(text[7:12])

print(text[::-1])


print("The string does %s start with 'hello'" % ("indeed" if text.lower().startswith("hello") else "not"))

print("The string does %s end with 'programming.'" % ("indeed" if text.lower().endswith("programming.") else "not"))

print(text.split(" "))

print(text.replace("! ", "\n"))