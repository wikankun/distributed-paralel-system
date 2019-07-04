# import library zeroMQ
import zmq

# membuat context zeroMQ
context = zmq.Context()

# membuat socket dan mengkoneksikannya ke server
print("Connecting to hello world server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://192.168.1.12:5555")

# melakukan perulangan sebanyak 10 kali
for request in range(10):
    # mengirimkan pesan "Hello" yang berupa byte
    print("Sending request %s ..." % request)
    socket.send(b"Hello")

    # menerima pesan dari socket dan menampilkannya
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))
