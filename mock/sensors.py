import socket
import ssl
import time
import json
import random
import threading

SERVER_IP = '127.0.0.1'
PORT = 8080

def mock_sensor(sensor_id):
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE  
    with socket.create_connection((SERVER_IP, PORT)) as sock:
        with context.wrap_socket(sock, server_hostname=SERVER_IP) as ssock:
            try:
                while True:
                    message = json.dumps({
                        "id": f"sensor_{sensor_id}",
                        "temp": round(random.uniform(20.0, 30.0), 2),
                        "battery": random.randint(60, 100)
                    })
                    ssock.sendall(message.encode('utf-8'))
                    time.sleep(random.uniform(1, 3))
            except KeyboardInterrupt:
                pass

def main():
    threads = []
    for i in range(5): 
        t = threading.Thread(target=mock_sensor, args=(i,), daemon=True)
        t.start()
        threads.append(t)
        time.sleep(random.uniform(0.5, 1))

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping all sensors...")

if __name__ == '__main__':
    main()

