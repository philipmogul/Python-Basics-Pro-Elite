def main():
    print("Generator function in PYTHON")
    usegenerator()

def usegenerator():
    def simple_generator():
        yield "First value"
        yield "Second value"
        yield "Third value"

    gen = simple_generator()
    for value in gen:
        print(value)

    # Yield is used to produce a series of values over time, pausing after each yield statement.
    # This allows the function to maintain its state between calls, 
    # making it memory efficient for large datasets.


if __name__ == "__main__":
    main()