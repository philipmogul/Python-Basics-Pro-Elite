def main():
    print(f"String Functions in PYTHON")
    print(f"Python provides a variety of built-in string functions to manipulate and "
          f"handle strings effectively.\n")
    
    sample_string = "  Hello, World! Welcome to Python String Functions.  "
    print(f"Original String: '{sample_string}'")
    
    # Example of some common string functions
    print(f"Length of string: {len(sample_string)}")
    print(f"Capitalized: '{sample_string.capitalize()}'")
    print(f"Title Case: '{sample_string.title()}'")
    print(f"Swap Case: '{sample_string.swapcase()}'")
    
    print(f"Uppercase: '{sample_string.upper()}'")
    print(f"Lowercase: '{sample_string.lower()}'")
    print(f"Stripped String: '{sample_string.strip()}'")
    print(f"Replaced String: '{sample_string.replace('World', 'Universe')}'")
    print(f"Split String: {sample_string.split()}")
    print(f"R split String: {sample_string.rsplit()}")
    print(f"Joined String with hyphen: '{'-'.join(sample_string.split())}'")
    print(f"Joined String with underscore: '{'_'.join(sample_string.split())}'")
    print(f"Joined String with comma: '{', '.join(sample_string.split())}'")
    print(f"Joined String with space: '{' '.join(sample_string.split())}'")
    print(f"Joined String with '-': '{'-'.join(sample_string.split())}'")
    print(f"Joined String: '{' - '.join(sample_string.split())}'")
    print(f"Count of 'o': {sample_string.count('o')}")
    print(f"Index of 'World': {sample_string.index('World')}")
    print(f"Find 'Universe': {sample_string.find('Universe')}")
    print(f"Find 'Python': {sample_string.find('Python')}")
    print(f"Is Alphanumeric: {sample_string.isalnum()}")
    print(f"Is Alphabetic: {sample_string.isalpha()}")
    print(f"Is Digit: {sample_string.isdigit()}")
    print(f"Is Lowercase: {sample_string.islower()}")
    print(f"Is Uppercase: {sample_string.isupper()}")
    print(f"Is Space: {sample_string.isspace()}")
    print(f"Is Printable: {sample_string.isprintable()}")
    print(f"Starts with '  Hello': {sample_string.startswith('  Hello')}")
    print(f"Ends with 'Functions.  ': {sample_string.endswith('Functions.  ')}")

if __name__ == "__main__":
    main() 