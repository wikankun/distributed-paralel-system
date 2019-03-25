# import library socket karena akan menggunakan IPC socket
import socket as sc

# definisikan alamat IP binding  yang akan digunakan 
HOST = "192.168.43.126"

# definisikan port number binding  yang akan digunakan 
PORT = 4044

# definisikan ukuran buffer untuk mengirimkan pesan
buffer_size = 1024

# buat socket bertipe TCP
s = sc.socket(sc.AF_INET, sc.SOCK_STREAM)

# lakukan bind
s.bind((HOST, PORT))

# server akan listen menunggu hingga ada koneksi dari client
s.listen(1)

# lakukan loop forever
while 1:
	# menerima koneksi
    conn, addr = s.accept()
	
	# menampilkan koneksi berupa IP dan port client yang terhubung menggunakan print
    print('Get connection from {}'.format(addr))
	
	# menerima data berdasarkan ukuran buffer
    RECEIVED = conn.recv(1024).decode()
	
	# menampilkan pesan yang diterima oleh server menggunakan print
    print(RECEIVED)
	
	# mengirim kembali data yang diterima dari client kepada client
    conn.send(RECEIVED.encode())

# tutup koneksi	
s.close()
