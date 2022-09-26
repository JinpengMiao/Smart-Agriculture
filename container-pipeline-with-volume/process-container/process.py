#!/usr/bin/python3

import socket
import csv

def update_data():
    data = ['Canada', 124, 'CA', 'CAN']

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
        print("Got notified from: " + str(address))
        # call process function and then update the data. This piece will be added later
        
        update_data()
        conn.send(b"Finish processing")  # respond receiver container
    
if __name__ == '__main__':
    receive_signal()
   