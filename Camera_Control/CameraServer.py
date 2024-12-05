import socket
import threading
import cv2
from datetime import datetime


def run_server(server_address):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(server_address)
    server.listen(5)
    print("Listening...")

    conn, addr = server.accept()
    print(f"Connected to {addr}")

    try:
        while True:
            bytes_received = conn.recv(1024)

            if bytes_received == b'':
                break

            message = bytes_received.decode()

            if message == 'capture':
                print(f"{addr} Requested Capture")
                request_event.set()
            
                capture_event.wait()
                conn.sendall("frame captured".encode())
                capture_event.clear()
            else:
                conn.sendall("What...?".encode())

        conn.close()
        print(f"{addr} Disconnected...")
    
    finally:
        print("Disconnecting Server")
        server.close()


ip = ''
port = 9999
server_address = (ip, port)

request_event = threading.Event()
capture_event = threading.Event()

th = threading.Thread(target=run_server, args=[server_address])
th.daemon = True
th.start()

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    
try:
    while True:
        ret, frame = cap.read()
        if ret == False:
            print("Capture Failed")
            break

        cv2.imshow("Camera Frame", frame)
        if cv2.waitKey(1) == ord('q'):
            break

        if not th.is_alive():
            print("Server Stopped...Stopping the stream")
            break

        if request_event.is_set():
            t = datetime.now().strftime("%Y%m%d-%H%M%S")
            cv2.imwrite(f"IMG_{t}.png", frame)
            
            request_event.clear()
            capture_event.set()

finally:
    cap.release()
