def main():
    print("FUNCTION ARGUMENTS IN PYTHON")
    print("*args include in a function allows it to accept a variable number of " \
    "positional arguments.")
    example_args(1, 2, 3, "four", "five")
    print("\n**kwargs include in a function allows it to accept a variable number of " \
    "keyword arguments.")
    example_kwargs(name="Alice", age=30, city="New York")

def example_args(*args):
    for index, value in enumerate(args):
        print(f"Argument {index}: {value}")

def example_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"Keyword argument {key}: {value}")

if __name__ == "__main__":
    main()