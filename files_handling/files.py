print("Working with Files Example:")

# Writing to a file
with open("./files_handling/example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a file handling example.\n")

# Reading from a file
with open("./files_handling/example.txt", "r") as file:
    content = file.read()
    print("File Content:\n{}".format(content))