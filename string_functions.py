def main():
    print(f"String Functions in PYTHON")
    print(f"Python provides a variety of built-in string functions to manipulate and "
          f"handle strings effectively.\n")
    
    sample_string = "  Hello, World! Welcome to Python String Functions.  "
    print(f"Original String: '{sample_string}'")
    
    # Example of some common string functions
    print(f"Length of string: {len(sample_string)}")
    print(f"Uppercase: '{sample_string.upper()}'")
    print(f"Lowercase: '{sample_string.lower()}'")
    print(f"Stripped String: '{sample_string.strip()}'")
    print(f"Replaced String: '{sample_string.replace('World', 'Universe')}'")
    print(f"Split String: {sample_string.split()}")
    print(f"Find 'Python': {sample_string.find('Python')}")
    print(f"Is Alphanumeric: {sample_string.isalnum()}")
    print(f"Starts with '  Hello': {sample_string.startswith('  Hello')}")
    print(f"Ends with 'Functions.  ': {sample_string.endswith('Functions.  ')}")

if __name__ == "__main__":
    main() 