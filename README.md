# Smart-Agriculture
Source code for our research project on smart agriculture


## Communication between containers via socket
All data is transferred between containers via socket stream.  

Commands to start the system:  
`cd container-pipeline-with-socket`  
`docker-compose -f edge-server.yaml up`  


## Communication between containers via volume
All data is stored in a volume which is shared between all containers.  
Once a container's finish its own work, it will notify the next container in the pipeline via socket.  

Commands to start the system:  
`cd container-pipeline-with-volume`  
`docker-compose -f edge-server-volume.yaml up`  

