#!/usr/bin/python3

import socket
import csv

def update_data():
    data = ['America', 650, 'US', 'USA']

    with open('/data/data.csv', 'a', encoding='UTF8') as f:
        writer = csv.writer(f)
        # write the data
        writer.writerow(data)
        print("Finish updating the data")
        f.close()
        
    # Only used for test if the data was updated successfully or not
    with open('/data/data.csv', 'r', encoding='UTF8') as f:
        print("Show the updated data below: ")
        reader = csv.reader(f)
        for row in reader:
            print(row)
        f.close()
    
def receive_signal():
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
        print("Got notified from: " + str(address))
        # call filter function and then update the data. This piece will be added later
        
        update_data()
        conn.send(b"Finish updating")  # respond receiver container
        
    # after updating the data, notify the next container to process the data
    send_signal()
            
def send_signal():
    process_host = 'process'  # as both code is running on same pc
    process_port = 8020  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((process_host, process_port))  # connect to the server

    client_socket.send(b"Finished updating")  # send message
    data = client_socket.recv(1024).decode()  # receive response

    print('Received from process: ' + data)  # show in terminal  
    
    client_socket.close()  # close the connection


if __name__ == '__main__':
    receive_signal()

