def main():
    print(f"READING AND WRITING FILES EXAMPLE:")
    print(f"I will use infile and outfile to read and write files.")
    
    infile = open("./files_handling/example.txt", "r")
    outfile = open("./files_handling/output.txt", "w")

    for line in infile:
        print(f"Read line: {line.strip()}")
        outfile.write(line)
    infile.close()
    outfile.close()

if __name__ == "__main__": main()