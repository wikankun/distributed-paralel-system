import zmq
import random
import sys
import time

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:5556")

while True:
    socket.send("Server message to client".encode())
    msg = socket.recv()
    print (msg)
    time.sleep(1)
 