#!/usr/bin/python3

import socket

def send_data():
    filter_host = 'filter'  # as both code is running on same pc
    filter_port = 8010  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((filter_host, filter_port))  # connect to the server

    client_socket.send(b"Hello from receiver")  # send message
    data = client_socket.recv(1024).decode()  # receive response

    print('Received from server: ' + data)  # show in terminal

if __name__ == '__main__':
    send_data()
