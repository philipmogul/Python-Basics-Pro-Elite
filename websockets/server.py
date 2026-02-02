import socket
import threading

PORT = 5050
SERVER = "192.168.100.2" # My local IP address
# To automatically get the local IP address, uncomment the following line:
# SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)



# Create a socket object to open this server to other local devices
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# The above means we are using IPv4 and TCP protocols
# socket.AF_INET: Address Family - IPv4
# socket.SOCK_STREAM: TCP - Transmission Control Protocol
# Bind the server to the specified IP address and port
server.bind(ADDR)

# Handles individual client connections
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg = conn.recv(1024).decode('utf-8') # Receive message from client
        if msg:
            print(f"[{addr}] {msg}")
            if msg == "DISCONNECT":
                connected = False

            # Send acknowledgment back to the client from the server : OPTIONAL 
            # conn.send("Message received".encode('utf-8'))
    conn.close()
    print(f"[DISCONNECTED] {addr} disconnected.")


# Starts the server and listens for incoming connections
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}:{PORT}")
    while True:
        conn, addr = server.accept() # Wait for a new connection
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
print("[STARTING] Server is starting...")
start()

