# Smart-Agriculture
Source code for our research project on smart agriculture

## Algorithms for prediction of animals' future locations
'predict' folder contains the code, data, and dockerfile for 3 proposed layouts.
The algorithms are deployed on edge server with docker containers.
- `cd layout[X]`
- `docker build -t layout[X] .`
- `docker run -d layout[X]`
- `docker ps -a`
- `docker logs [CONTAINER ID]`


## Communication between containers via socket
All data is transferred between containers via socket stream.  

Commands to start the system:  
- `cd container-pipeline-with-socket`  
- `docker-compose -f edge-server.yaml up`  


## Communication between containers via volume
All data is stored in a volume which is shared between all containers.  
Once a container's finish its own work, it will notify the next container in the pipeline via socket.  

Commands to start the system:  
- `cd container-pipeline-with-volume`  
- `docker-compose -f edge-server-volume.yaml up`  

