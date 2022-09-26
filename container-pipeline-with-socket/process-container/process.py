#!/usr/bin/python3

import socket

def receive_data():
    process_host = 'process'
    process_port = 8020 

    server_socket = socket.socket()  # get instance
    # bind() function takes tuple as argument, bind host address and port together
    server_socket.bind((process_host, process_port)) 

    server_socket.listen(1)
    print("Listoning at port 8020 ...... ")
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
    
if __name__ == '__main__':
    receive_data()
   