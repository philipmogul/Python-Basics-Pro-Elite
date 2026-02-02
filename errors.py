def main():
    print("ERRORS IN PYTHON")
    # Opening a file that does not exist
    try:
        with open("non_existent_file.txt", "r") as file:
            content = file.read()
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")

    # Dividing by zero
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")

    # Accessing an invalid index in a list
    try:
        my_list = [1, 2, 3]
        print(my_list[5])
    except IndexError as e:
        print(f"IndexError: {e}")


    # Using an undefined variable
    try:
        print(undefined_variable)
    except NameError as e:
        print(f"NameError: {e}")

    
    # Converting an invalid string to an integer
    try:
        invalid_int = int("invalid_string")
    except ValueError as e:
        print(f"ValueError: {e}")

    #Custom error
    custom_exception_example()


# Raising a custom exception
def custom_exception_example():
    class CustomError(Exception):
        pass

    try:
        raise CustomError("This is a custom error message.")
    except CustomError as e:
        print(f"CustomError: {e}")


if __name__ == "__main__":
    main()