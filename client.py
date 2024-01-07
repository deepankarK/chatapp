import socket
import threading
from cryptography.fernet import Fernet

def receive_messages(client_socket, cipher_suite):
    while True:
        try:
            message_encrypted = client_socket.recv(1024)
            message = cipher_suite.decrypt(message_encrypted).decode('utf-8')
            print(message)
        except Exception as e:
            print(f"Error: {e}")
            break

def start_client():
    host = "12.12.12.12" # Enter your ipv4 of host
    port = 12345 # Enter your desired port
    username = input("Enter your username: ")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Receive the one-time key from the server
    server_key = client_socket.recv(1024)

    cipher_suite = Fernet(server_key)

    client_socket.send(cipher_suite.encrypt(username.encode('utf-8')))

    welcome_message_encrypted = client_socket.recv(1024)
    print(cipher_suite.decrypt(welcome_message_encrypted).decode('utf-8'))

    connected_users_message_encrypted = client_socket.recv(1024)
    print(cipher_suite.decrypt(connected_users_message_encrypted).decode('utf-8'))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket, cipher_suite))
    receive_thread.start()

    while True:
        message = input()
        client_socket.send(cipher_suite.encrypt(message.encode('utf-8')))

if __name__ == "__main__":
    start_client()
