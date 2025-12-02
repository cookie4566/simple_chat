# client code of the chat program
# base code from https://pandeyshikha075.medium.com/building-a-chat-server-and-client-in-python-with-socket-programming-c76de52cc1d5
import socket
import threading

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host ='127.0.0.1'
    port= 12345
    client_socket.connect((host,port))
    
    while True:
        message = input("Enter your message:")
        client_socket.sendall(message.encode('utf-8'))
        data = client_socket.recv(1024)
        response = data.decode('utf-8')
        print(f"Server response: {response}")

if __name__ == "__main__":
    main()