def main():
    print("Enumerators in Python:")
    fruits = ['apple', 'banana', 'cherry']
    print("List of fruits:", fruits)
    print("Using enumerate to get index and value:")
    for index, fruit in enumerate(fruits):
        print(f"Index: {index}, Fruit: {fruit}")

if __name__ == "__main__": main()