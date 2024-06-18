# Michael Mills

import socket
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    number = sys.argv[1]

    if not number.lstrip('-').isdigit():
        sys.exit(1)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    client_socket.send(number.encode('utf-8'))
    result = client_socket.recv(1024)
    print(f"Sent {number} and received {result}")
    client_socket.close()

if __name__ == '__main__':
    main()
