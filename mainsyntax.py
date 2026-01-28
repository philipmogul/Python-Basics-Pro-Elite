def main():
    print("This is the main function.")
    helper()

def helper():
    print("This will be called in main before the method is executed.")
    print("Otherwise if user calls this method directly, these lines won't be printed.")

if __name__ == "__main__": main()