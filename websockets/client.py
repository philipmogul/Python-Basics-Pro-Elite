import socket

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())  # Automatically get the local IP address
ADDR = (SERVER, PORT)

# Create a socket object to connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# Function to send messages to the server
def send_message(msg):
    client.send(msg.encode('utf-8'))  # Send message to server
    # Log the sent message by client 
    print(f"[SENT] {msg}")

    # Optional: Receive acknowledgment from server
    #ack = client.recv(1024).decode('utf-8')
    #print(f"[ACKNOWLEDGMENT] {ack}")

# Example usage
if __name__ == "__main__":
    # Capture user input to send messages
    while True:
        msg = input("Enter message to send (or 'quit' to exit): ")
        if msg.lower() == "quit":
            break
        send_message(msg)
    send_message("DISCONNECT")
    client.close()



