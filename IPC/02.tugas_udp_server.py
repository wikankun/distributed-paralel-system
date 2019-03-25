# import library socket karena akan menggunakan IPC socket
import socket as sc

# definisikan alamat IP bind dari server
UDP_HOST = "192.168.43.77"

# definisikan port number untuk bind dari server
UDP_PORT = 4044

# buat socket bertipe UDP
s = sc.socket(sc.AF_INET, sc.SOCK_DGRAM)

# lakukan bind
s.bind((UDP_HOST, UDP_PORT))

# loop forever
while True:
    # terima pesan dari client
    RECEIVED = s.recv(1024).decode()
    
    # menampilkan hasil pesan dari client
    #print (addr)
    print(RECEIVED)
    
