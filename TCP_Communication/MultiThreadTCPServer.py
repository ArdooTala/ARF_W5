import socket
import threading


def handle_client(addr, conn):
    while True:
        bytes_received = conn.recv(1024)

        if bytes_received == b'':
            break

        message = bytes_received.decode()
        print(f"{addr} says: {message}")

        respond = f"I Heard you: {message}"
        conn.sendall(respond.encode())

    conn.close()
    print(f"{addr} Disconnected...")


ip = ''
port = 9999
server_address = (ip, port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_address)
server.listen(5)
print("Listening...")

try:
    while True:
        conn, addr = server.accept()
        print(f"Connected to {addr}")

        th = threading.Thread(target=handle_client, args=[addr, conn])
        th.start()

finally:
    server.close()