# import library socket karena akan menggunakan IPC socket
import socket as sc

# definisikan tujuan IP server
HOST = "192.168.1.7"

# definisikan port dari server yang akan terhubung
PORT = 4044

# definisikan ukuran buffer untuk mengirimkan pesan
buffer_size = 1024

# definisikan pesan yang akan disampaikan
MESSAGE = "Hello World"

# buat socket TCP
s = sc.socket(sc.AF_INET, sc.SOCK_STREAM)

# lakukan koneksi ke server dengan parameter IP dan Port yang telah didefinisikan
s.connect((HOST, PORT))

# kirim pesan ke server
s.send(MESSAGE.encode())

# terima pesan dari server
RECEIVED = s.recv(1024).decode()

# tampilkan pesan/reply dari server
print(RECEIVED)

# tutup koneksi
s.close()

