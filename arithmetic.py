def main():
    print("Basic arithmetic operations:")

    a = 15
    b = 4

    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    print(f"Division: {a} / {b} = {a / b}")
    print(f"Integer Division: {a} // {b} = {a // b}")
    print(f"Modulus: {a} % {b} = {a % b}")
    print(f"Exponentiation: {a} ** {b} = {a ** b}") # Power operation
    divmod_result = divmod(a, b)
    print(f"Divmod: divmod({a}, {b}) = {divmod_result}") # Gives both quotient and remainder

if __name__ == "__main__": main()