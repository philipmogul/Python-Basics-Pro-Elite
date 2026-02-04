def main():
    print(f"String Formatting in PYTHON")
    print(f"Python provides several ways to format strings for better readability and "
          f"presentation of data.\n")
    
    name = "Alice"
    age = 30
    height = 5.7
    string = "This is a sample string."
    
    # Using f-strings (Python 3.6+)
    print(f"Using f-strings: {name} is {age} years old and {height} feet tall.")
    
    # Using str.format() method
    print("Using str.format(): {} is {} years old and {} feet tall.".format(name, age, height))
    
    # Using string.format() with positional and keyword arguments for string
    print("Using string.format() with positional args: {0} is {1} years old and {2} feet tall.".format(name, age, height))
    print("Using string.format() with keyword args: {name} is {age} years old and {height} feet tall.".format(name=name, age=age, height=height))
    print("Using string.format() for string: {}".format(string))
    

if __name__ == "__main__":
    main()