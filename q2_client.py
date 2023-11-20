import socket

def receive_messages(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen()
            print(f"Waiting for a connection on {host}:{port}")
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                data = ""
                while data.lower() != "bye":
                    data = conn.recv(1024)
                    print(f"Received message: {data.decode()}")
                    if data.lower() != "bye":
                        message_to_send = input("Enter your reply: ")
                        conn.sendall(message_to_send.encode())
    except Exception as e:
        print(f"Error receiving message: {e}")

if __name__ == "__main__":
    sender_host = "localhost"  # Replace with the sender's IP address or hostname
    sender_port = 12345  # Replace with the sender's port number

    receive_messages(sender_host, sender_port)
