numbers = [5, 8, 12, 15, 18, 21, 24]

for num in numbers:
    if num % 3:
        print("Not divisible by 3: %d" % num)
        continue
    print("Divisible by 3: %d" % num)

count = 0
while count < 5:
    count += 1
    print(count)