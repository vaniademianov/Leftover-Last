import client as c
class MyTCPClient(c.TCPClient):
    def on_receive(self, data):
        # Handle data received from the server
        print(f"Received data from server: {data.decode()}")

client = MyTCPClient("localhost", 1234)
client.connect()
while True:
    req = bytes(str(input("Enter text: ")),"utf-8")
    if req == "stop":
        break
    client.send(req)
    response = client.receive()
    print(f"Server response: {response.decode()}")
client.close()