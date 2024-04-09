## Driving Simulation Data Connector

This project includes a python server (titled DC_server.py) written using the Flask library,
 which has separate documentation included. An example python client is provided (titled DC_client_example.py) 
with examples of how to make requests to the server. Also included is curltest.cpp,
that provides an example of C++ code using the curl library. This code be used as a basis 
for integrating into the C++ code of the simulator.

To run this project, follow the steps below:  
1. Run the server (DC_server.py) by typing 'python DC_server.py' in the command line.  
2. Run DC_playback, which will update the data in the server at the appropriate times in the example parquet file 
(meant to simulate how the simulator updates the data in real-tme).  
3. To check whether the data is updating, type the IP Address of the machine running the server with port number 5000.
