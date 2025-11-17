# server code that handles all the chat funtionalities 
import socket
import threading

# function that handles the client(s) date, both communication and connection alike
# uses a while-loop to preform this action repeatedly until client(s) data reaches "0", meaning that the client(s) has disconnected
def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        message = data.decode('utf-8')
        print(f"Received message: {message}")
        response = "Server received your message:" + message
        client_socket.sendall(response.encode('utf-8'))
    client_socket.close()