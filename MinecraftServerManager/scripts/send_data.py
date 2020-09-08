from socket import socket, AF_INET, SOCK_STREAM
import json


def main():
    options = {}
    with open('../configuration/options.json', 'r') as json_file:
        options = json.load(json_file)


    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect((options['host'], options['port']))
        s.sendall(b'{"type": "EventProcess", "title": "stop"}')
#        data = s.recv(1024)
    

if __name__ == '__main__':
    main()
