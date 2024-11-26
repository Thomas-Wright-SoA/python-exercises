for i in range(1, 21):
    multipleof3 = not i % 3
    mulitpleof5 = not i % 5
    if multipleof3 or mulitpleof5:
        if multipleof3 and mulitpleof5:
            print("FizzBuzz")
        elif multipleof3:
            print("Fizz")
        else:
            print("Buzz")
    else:
        print(i)
