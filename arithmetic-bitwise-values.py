def main():
    print("Bitwise operations:")

    a = 15 # 1111 in binary
    b = 4  # 0100 in binary

    print(f"Bitwise AND: {a} & {b} = {a & b}")
    print(f"Bitwise OR: {a} | {b} = {a | b}")
    print(f"Bitwise XOR: {a} ^ {b} = {a ^ b}")
    print(f"Left Shift: {a} << 1 = {a << 1}")
    print(f"Right Shift: {a} >> 1 = {a >> 1}")

if __name__ == "__main__": main()