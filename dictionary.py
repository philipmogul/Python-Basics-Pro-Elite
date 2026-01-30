def main():
    print("Dictionaries in Python:")
    d = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    print("Dictionary:", d)
    print("Accessing value for 'key2':", d['key2'])
    print("Adding a new key-value pair: d['key4'] = 'value4'")
    d['key4'] = 'value4'
    print("Updated Dictionary:", d)

    print("Printing keys:")
    for key in d.keys():
        print(key)

    print("Printing values:")
    for value in d.values():
        print(value)

    print("Printing key-value pairs:")
    for key, value in d.items():
        print(f"{key}: {value}")


if __name__ == "__main__": main()