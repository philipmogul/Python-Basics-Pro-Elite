print("READING FROM A FILE EXAMPLE:")

fh = open("./files_handling/files.txt", "r")
for line in fh.readlines():
    print("{}".format(line.strip()))
