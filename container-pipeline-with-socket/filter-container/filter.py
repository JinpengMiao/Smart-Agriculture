#!/usr/bin/python3

import socket

def receive_data():
    filter_host = 'filter'
    filter_port = 8010 

    server_socket = socket.socket()  # get instance
    # bind() function takes tuple as argument, bind host address and port together
    server_socket.bind((filter_host, filter_port))

    server_socket.listen(1)
    print("Listoning at port 8010 ...... ")
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        conn.send(data.encode())  # send data to the client
        
        # after receiving data, call filter function. This piece will be added later
        
        # after filtering data, send it to next container
        send_data(data)
            

def send_data(data):
    process_host = 'process'  # as both code is running on same pc
    process_port = 8020  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((process_host, process_port))  # connect to the server

    client_socket.send(data.encode())  # send message
    data = client_socket.recv(1024).decode()  # receive response

    print('Received from process: ' + data)  # show in terminal  
    
    client_socket.close()  # close the connection


if __name__ == '__main__':
    receive_data()

