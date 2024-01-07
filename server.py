import socket
import threading

# Dictionary to store client connections and their usernames
clients = {}

def handle_client(client_socket, addr):
    username = client_socket.recv(1024).decode('utf-8')
    print(f"User {username} connected from {addr}")
    
    # Add client and its username to the dictionary
    clients[username] = client_socket
    
    # Send a welcome message to the new user
    welcome_message = f"Welcome, {username}! You are now connected to the chat server."
    client_socket.send(welcome_message.encode('utf-8'))
    
    # Display the number of connected users to the new user
    num_connected_users = len(clients)
    connected_users_message = f"There {'is' if num_connected_users == 1 else 'are'} {num_connected_users} user{'s' if num_connected_users != 1 else ''} already in the session."
    client_socket.send(connected_users_message.encode('utf-8'))
    
    # Broadcast the new user's connection to all connected clients
    for client in clients.values():
        if client != client_socket:
            new_user_message = f"{username} has joined the chat."
            client.send(new_user_message.encode('utf-8'))

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break

            # Broadcast the message to all connected clients
            for client in clients.values():
                if client != client_socket:
                    client.send(f"{username}: {message}".encode('utf-8'))
        except Exception as e:
            print(f"Error: {e}")
            break

    # Remove the client from the dictionary when disconnected
    del clients[username]
    print(f"User {username} disconnected")
    client_socket.close()

def start_server():
    host = '0.0.0.0'  # Allow connections from any IP address
    port = 12345  # Choose a suitable port number

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_handler.start()

if __name__ == "__main__":
    start_server()
