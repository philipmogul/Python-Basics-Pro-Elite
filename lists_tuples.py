def main():
    lists = [1, 2, 3]
    tuples = (1, 2, 3, 4, 5, 6)
    print("List:", lists)
    print("Length of List:", len(lists))
    print("Lists are mutable! Can add, remove, or change elements.")
    print("Tuple:", tuples)
    print("Length of Tuple:", len(tuples))
    print("Tuples are immutable! Cannot add, remove, or change elements.")

    slices = "Hello, World!"
    print("String Slices:")
    print("First 5 characters:", slices[:5])
    print("Characters from index 7 to 12:", slices[7:12])

if __name__ == "__main__": main()