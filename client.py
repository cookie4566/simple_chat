# client code of the chat program
import socket
import threading

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host ='127.0.01'
    port=12345
    client_socket.connect((host,port))
    
    while True:
        message = input("Enter your message:")
        client_socket.sendall(message.encode('utf-8'))
        data = client_socket.recv(1024)
        response = data.decod('utf-8')
        print(f"Server response: {response}")

if __name__ == "__main__":
    main()