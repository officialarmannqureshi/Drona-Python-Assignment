import socket

def send_message(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            while True:
                message_to_send = input("Enter message to send (type 'bye' to exit): ")
                s.sendall(message_to_send.encode())
                if message_to_send.lower() == "bye":
                    break
                data = s.recv(1024)
                print(f"Received reply: {data.decode()}")
    except Exception as e:
        print(f"Error sending/receiving message: {e}")

if __name__ == "__main__":
    receiver_host = "localhost"  # Replace with the receiver's IP address or hostname
    receiver_port = 12345  # Replace with the receiver's port number

    send_message(receiver_host, receiver_port)
