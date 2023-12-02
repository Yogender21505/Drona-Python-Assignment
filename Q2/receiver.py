import socket

def receiver():
    # Create a socket object
    receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    receiver_address = 'localhost'
    receiver_port = 5001
    receiver_socket.bind((receiver_address, receiver_port))

    # Listen for incoming connections
    receiver_socket.listen()

    print(f"Receiver is listening on {receiver_address}:{receiver_port}")

    try:
        # Accept a connection from the sender
        sender_socket, sender_address = receiver_socket.accept()
        print(f"Connected to {sender_address}")

        while True:
            # Receive the message from the sender
            message = sender_socket.recv(1024).decode()

            # Check if the sender has closed the connection
            if not message:
                break

            # Display the received message
            print(f"Received message: {message}")

        # Close the sockets
        sender_socket.close()
        receiver_socket.close()

    except Exception as e:
        print(f"Error: {e}")
        receiver_socket.close()

if __name__ == "__main__":
    receiver()
