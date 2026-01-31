def main():
    print("Using break and continue and end statements in loops:")

    print("Using break statement:")
    for i in range(10):
        if i == 5:
            break
        print(i, end=' ')
    print("Loop ended.")

    print("Using continue statement:")
    for i in range(10):
        if i % 2 == 0:
            continue
        print(i, end=' ')
    print("Loop ended.")

if __name__ == "__main__": main()