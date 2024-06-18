# Michael Mills
import socket

def sum_of_digits(number):
    abs_number = abs(number)
    return sum(int(digit) for digit in str(abs_number)) + 100

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server listening on port 12345")

    while True:
        client_socket, client_address = server_socket.accept()
        data = client_socket.recv(1024)
        if not data:
            break

        number = int(data.decode('utf-8'))
        result = sum_of_digits(number)
        client_socket.send(str(result).encode('utf-8'))
        client_socket.close()

if __name__ == '__main__':
    main()
