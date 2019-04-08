# import paho
import paho.mqtt.client as mqtt

# definsi broker yang digunakan
broker_address = "192.168.1.14"

# buat client bernama P1
print("creating new instance")
client = mqtt.Client("P1")

# client terkoneksi ke broker
print("connecting to broker")
client.connect(broker_address, port=1883)

# print "baca file"
print("read file")

# buka file surf.jpg
f = open("surf.jpg", "rb")

# baca semua isi file
data = f.read()

# ubah file dalam bentuk byte gunakan fungsi byte()
data = data

# publish dengan topik photo dan data dipublish adalah file
print("publish foto")
client.publish("photo", data)

# client loop mulai
client.loop_start()

# tutup file
f.close()