import socket

def sender():
    # Create a socket object
    sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the receiver's address and port
    receiver_address = 'localhost'
    receiver_port = 5001

    try:
        # Connect to the receiver
        sender_socket.connect((receiver_address, receiver_port))

        while True:
            # Get user input to send a message
            message = input("Enter a message to send (type 'exit' to quit): ")
            
            # Check if the user wants to exit
            if message.lower() == 'exit':
                break
            
            # Send the message to the receiver
            sender_socket.send(message.encode())

        # Close the socket connection
        sender_socket.close()

    except Exception as e:
        print(f"Error: {e}")
        sender_socket.close()

if __name__ == "__main__":
    sender()
