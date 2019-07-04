# import library zeroMQ
import zmq

# membuat context zeroMQ
context = zmq.Context()

# membuat socket subsriber
sock = context.socket(zmq.SUB)

# mengatur option_name dan option_len
sock.setsockopt(zmq.SUBSCRIBE, b"1")
# mengkoneksikan socket ke alamat IP publisher
sock.connect("tcp://192.168.1.18:5680")

while True:
    # menerima massage dan menampilannya
    message = sock.recv()
    print (message)