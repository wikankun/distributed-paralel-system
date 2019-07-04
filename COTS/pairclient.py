import zmq
import random
import sys
import time

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://localhost:5556")

while True:
    msg = socket.recv()
    print (msg)
    socket.send("client message 1 to server".encode())
    socket.send("client message 2 to server".encode())
    time.sleep(1)