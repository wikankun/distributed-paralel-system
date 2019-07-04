# import library zeroMQ dan time
import zmq
import time

# membuat context zeroMQ
context = zmq.Context()

# membuat socket publisher dan binding dengan IP server
sock = context.socket(zmq.PUB)
sock.bind("tcp://192.168.1.18:5680")

id = 0

while True:
    # sleep selama 1 detik
    time.sleep(1)
    # mengupdate nilai id dan now dengan waktu saat ini
    id, now = id+1, time.ctime()

    # mengirimkan id dan waktu sekarang jika option_len = 1
    message = "1-Update! >> #{id} >> {time}".format(id=id, time=now)
    sock.send(message.encode('ascii'))

    # mengirimkan id dan waktu sekarang jika option_len = 2
    message = "2-Update! >> #{id} >> {time}".format(id=id, time=now) 
    sock.send(message.encode('ascii'))

    id += 1