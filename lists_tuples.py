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

    # important notes about tuples
    print("Tuples are created using commas, not parentheses.")
    tup = 1,
    print("Single element tuple:", tup)
    print("Type of single element tuple:", type(tup))
    print("Lists can be created using the list() constructor:")
    li = list((1, 2, 3))
    li2 = list(range(11))
    print("List created from tuple:", li)
    print("List created from range:", li2)

    print("Tuples can be created using the tuple() constructor:")
    tup2 = tuple([1, 2, 3])
    print("Tuple created from list:", tup2)
    print("Tuples can be used as keys in dictionaries, while lists cannot.")

    print("Dictionaries can be created using the dict() constructor:")
    d = dict([(1, "one"), (2, "two"), (3, "three")])
    print("Dictionary created from list of tuples:", d)


if __name__ == "__main__": main()