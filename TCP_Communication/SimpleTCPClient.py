import socket

ip = '127.0.0.1'
port = 9999
server_address = (ip, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_address)

while True:
    message = input("Message to send > ")
    if message == "":
        break
    
    bytes_message = message.encode()
    client.sendall(bytes_message)

    bytes_response = client.recv(1024)
    response = bytes_response.decode()
    print(response)

client.close()
