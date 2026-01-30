def main():
    a = 10;
    b = 10;
    print("a == b:", a == b)   # True, because values are equal
    print("a is b:", a is b)   # True, because both refer to the same object in memory
    print("Id of a:", id(a), "Id of b:", id(b))
    print("Type of a:", type(a), "Type of b:", type(b))

if __name__ == "__main__": main()