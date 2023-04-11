import server as s
class MyTCPServer(s.TCPServer):
    def on_connect(self, client_socket, client_address):
        # Send a welcome message to the new client
        client_socket.sendall(b"Welcome to my Pygame game server!")

    def on_receive(self, client_socket, client_address, data):
        # Handle data received from a client
        print(f"Received data from {client_address}: {data.decode()}")

    def on_disconnect(self, client_socket, client_address):
        # Handle a client disconnection
        print(f"Client {client_address} disconnected")

server = MyTCPServer("localhost", 1234)
server.start()
