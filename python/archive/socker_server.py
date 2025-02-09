import socket
import binascii

def server():
    # Get the hostname of the server
    host = socket.gethostname()

    # Specify the port to listen on
    port = 8100

    # Create a socket object
    s = socket.socket()

    # Bind the socket to the host and port
    # s.bind((host, port))
    s.bind(("localhost", port))

    # Listen for incoming connections, allowing up to 2 clients in the queue
    s.listen(1)

    # Accept an incoming connection
    c, address = s.accept()
    print(f"Connected to: {address}")

    while True:
        # Receive data from the client (up to 1024 bytes) and decode it
        # data = c.recv(1024).decode('ascii')

        hexdata = binascii.hexlify(c.recv(1024))
        print(hexdata)

        # If no data is received, break the loop
        if not data:
            break

        print(f"Received from client: {data}")

        # Get user input and send it to the client after encoding
        # response = input("Enter response to send to client: ")
        # c.send(response.encode())
    # Close the client connection
    c.close()


if __name__ == "__main__":
    # Start the server
    server()