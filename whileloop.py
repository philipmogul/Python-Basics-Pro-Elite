def main():
    print("While Loop in Python:")
    count = 0
    print("Counting from 0 to 4:")
    while count < 5:
        print(count)
        count += 1

    print("Using while loop to sum numbers from 1 to 10:")
    total = 0
    num = 1
    while num <= 10:
        total += num
        num += 1
    print("Total sum from 1 to 10 is:", total)

    print("Using while loop with break statement:")
    n = 0
    while True:
        print(n)
        n += 1
        if n >= 5:
            print("Breaking the loop as n reached", n)
            break

    print("Using while loop with continue statement:")
    i = 0
    while i < 10:
        i += 1
        if i % 2 == 0:
            continue
        print(i, "is an odd number")


    print("Fibonacci sequence using while loop:")
    a, b = 0, 1
    while a < 20:
        print(a, end=', ')
        a, b = b, a + b

if __name__ == "__main__": main()