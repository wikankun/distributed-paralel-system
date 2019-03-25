# import library socket karena akan menggunakan IPC socket
import socket as sc

# definisikan target IP server yang akan dituju
UDP_HOST = "192.168.43.77"

# definisikan target port number server yang akan dituju
UDP_PORT = 4044

#print ("target IP:", UDP_IP)
print("target IP: ", UDP_HOST)
#print ("target port:", UDP_PORT)
print("target PORT: ", UDP_PORT)

# definisikan pesan yang akan dikirim
MESSAGE = "Hello world"
print("pesan: ", MESSAGE)

# buat socket bertipe UDP
s = sc.socket(sc.AF_INET, sc.SOCK_DGRAM)

# lakukan loop 10 kali
for x in range(10):
    # kirim pesan    
    s.sendto(MESSAGE.encode(), (UDP_HOST, UDP_PORT))