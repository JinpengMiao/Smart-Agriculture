#!/usr/bin/python3

import socket
import csv

def write_data():
    header = ['name', 'area', 'country_code2', 'country_code3']
    data = ['Afghanistan', 652090, 'AF', 'AFG']

    with open('/data/data.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        # write the header
        writer.writerow(header)
        # write the data
        writer.writerow(data)
        f.close()
        # after writing data to the file, notify the next container to filter the data
        send_signal()

def send_signal():
    filter_host = 'filter'  # as both code is running on same pc
    filter_port = 8010  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((filter_host, filter_port))  # connect to the server

    client_socket.send(b"Finished writing")  # send message
    data = client_socket.recv(1024).decode()  # receive response

    print('Received from server: ' + data)  # show in terminal

if __name__ == '__main__':
    write_data()
