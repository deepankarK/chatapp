# chatapp

# Simple Encrypted Chat Application

This is a simple encrypted chat application built in Python using sockets and the cryptography library. The application allows users to securely communicate with each other over a network.

## Features

- **Encrypted Communication:** Messages exchanged between the server and clients are encrypted using the `cryptography` library to ensure secure communication.

- **Dynamic Key Generation:** The server generates a one-time key for each client session, enhancing the security of message encryption.

- **Graceful Shutdown:** The server can be gracefully shut down by typing "exit" in the server console, which closes all running processes.

## How to Use

### Server

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/simple-encrypted-chat.git

