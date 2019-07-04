# import library zeroMQ
import zmq

# membuat context zeroMQ
context = zmq.Context()

# membuat socket pull dan mengkoneksikan dengan IP push
sock = context.socket(zmq.PULL)
sock.connect("tcp://192.168.1.12:5690")

while True:
    # menerima message dan menampilkannya
    message = sock.recv()
    print ("Received: {msg}".format(msg=message))