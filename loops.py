print("WHILE LOOP EXAMPLE:")
i = 0
while i < 5:
    print("i is now {}".format(i))
    i += 1

print("\nFOR LOOP EXAMPLE:")
for j in range(5):
    print("j is now {}".format(j))

print("\nFOR LOOP WITH LIST EXAMPLE:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Current fruit: {}".format(fruit))

print("\nNESTED LOOP EXAMPLE:")
for x in range(3):
    for y in range(2):
        print("x: {}, y: {}".format(x, y))