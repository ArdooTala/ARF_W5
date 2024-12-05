import socket


ip = ''
port = 9999
server_address = (ip, port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_address)
server.listen(5)
print("Listening...")

try:
    conn, addr = server.accept()
    print(f"Connected to {addr}")
    
    while True:
        bytes_received = conn.recv(1024)
        if bytes_received == b'':
            break

        message_received = bytes_received.decode()
        print(f"{addr} says: {message_received}")

        response = f"I heared: {message_received}"
        bytes_response = response.encode()
        conn.sendall(bytes_response)

    conn.close()
finally:
    server.close()
