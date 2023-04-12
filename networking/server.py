import threading
import socket

class TCPServer:
    def __init__(self, host, port, backlog=5):
        self.host = host
        self.port = port
        self.backlog = backlog
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_threads = []
        
    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(self.backlog)
        print(f"Server listening on {self.host}:{self.port}")
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"New client connected from {client_address[0]}:{client_address[1]}")
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket, client_address))
            client_thread.start()
            self.client_threads.append(client_thread)
            
    def stop(self):
        for client_thread in self.client_threads:
            client_thread.join()
        self.server_socket.close()
        print("Server stopped")
        
    def handle_client(self, client_socket, client_address):
        try:
            self.on_connect(client_socket, client_address)
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                self.on_receive(client_socket, client_address, data)
        except Exception as e:
            print(f"Error handling client {client_address}: {e}")
        finally:
            self.on_disconnect(client_socket, client_address)
            client_socket.close()
            
    def on_connect(self, client_socket, client_address):
        pass
    
    def on_disconnect(self, client_socket, client_address):
        pass
    
    def on_receive(self, client_socket, client_address, data):
        pass
    