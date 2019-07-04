# import library time dan zeroMQ
import time
import zmq

# membuat context zeroMQ, socket dan binding socket pada IP localhost
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://192.168.1.18:5555")

# looping forever
while True:
    # menerima pesan dari socket dan menampilkannya
    message = socket.recv()
    print("Received request: %s" % message)

	# do some work
    time.sleep(1)

    # mengirimkan pesan "World" yang berupa byte
    socket.send(b"World")
