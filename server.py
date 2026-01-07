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

# main (hehe) body of the server code that creates a socket to listen to empty ports and other fun socket tings
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creates a TCP(Transmission Control Protocol/ .SOCK_STREAM) socket that uses IPv4(internet protocol/ .AF_INET) context manger type
    host= '127.0.0.1' # test ip address that points to current user system(local host)
    port= 12345 # random inhibatied port number, safe for chatting :)
    server_socket.bind((host,port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")
    
    # while-loop allows the connection of multiple clients via threading
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accpted connection from {client_address}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ =="__main__":
    main()