def main():
    print(f"READING BINARY FILES EXAMPLE: FOR TEXTS OR IMAGES")
    print(f"I will use infile to read a binary file and print its contents.")
    print(f"Then I will write the binary data to another file using outfile.")
    buffersize = 50000
    infile = open("./files_handling/example.txt", "rb")
    outfile = open("./files_handling/output_binary.txt", "wb")
    buffer = infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        print(f"Read {len(buffer)} bytes and wrote to output_binary.txt")
        buffer = infile.read(buffersize)
    print(f"Finished reading and writing binary data.")
    infile.close()
    outfile.close()

    print(f"FOR IMAGES: ")
    imgbuffersize = 50000
    imginfile = open("./files_handling/bg.png", "rb")
    imgoutfile = open("./files_handling/output_bg.png", "wb")
    imgbuffer = imginfile.read(imgbuffersize)
    while len(imgbuffer):
        imgoutfile.write(imgbuffer)
        print(f"Read {len(imgbuffer)} bytes and wrote to output_bg.png")
        imgbuffer = imginfile.read(imgbuffersize)
    print(f"Finished reading and writing binary data.")
    imginfile.close()
    imgoutfile.close()
    


if __name__ == "__main__": main()