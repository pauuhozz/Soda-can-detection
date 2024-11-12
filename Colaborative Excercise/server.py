import socket

def start_server(host='192.168.0.107', port=5000):
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Server is listening on port", port)

    while True:
        # Accept a new connection
        client_socket, client_address = server_socket.accept()
        # Print the client address to which the server is connected
        print(f"Connection from {client_address}")

        # Receive the data, decode and print it out on the console
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            print("Received coordinates:", data)

        # Close the client connection
        client_socket.close()
        print("Connection closed.")

# Run the server
start_server()
