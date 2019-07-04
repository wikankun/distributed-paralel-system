# import library zeroMQ dan time
import zmq
import time

# membuat context zeroMQ
context = zmq.Context()

# membuat socket push dan binding dengan IP server
sock = context.socket(zmq.PUSH)
sock.bind("tcp://192.168.18:5690")

id = 0

while True:
    # sleep selama 1 detik
    time.sleep(1)
    # mengupdate nilai id dan now dengan waktu saat ini
    id, now = id+1, time.ctime()
    # mengirimkan message dan menampilkan message yang dikirim
    message = "{id} - {time}".format(id=id, time=now)
    sock.send(message.encode())
    print ("Sent: {msg}".format(msg=message))