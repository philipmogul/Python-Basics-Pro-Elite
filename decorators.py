def main():
    print(f"Decorators in PYTHON")
    print(f"Decorators are a way to modify or enhance functions or methods without "
          f"changing their actual code.")
    print(f"They are often used for logging, access control, caching, and more.\n")
    def simple_decorator(func):
        def wrapper():
            print("Before calling the function.")
            func()
            print("After calling the function.")
        return wrapper
    
    @simple_decorator # This is how we apply the decorator
    
    def say_hello():
        print("Hello, World!")
    say_hello()

if __name__ == "__main__":
    main()