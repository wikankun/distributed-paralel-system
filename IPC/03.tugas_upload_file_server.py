# import library socket karena menggunakan IPC socket
import socket as sc

# definisikan IP untuk binding
HOST = "192.168.1.8"

# definisikan port untuk binding
PORT = 4044

# definisikan ukuran buffer untuk menerima pesan
buffer_size = 1024

# buat socket (bertipe UDP atau TCP?)
s = sc.socket(sc.AF_INET, sc.SOCK_STREAM)

# lakukan binding ke IP dan port
s.bind((HOST, PORT))

# lakukan listen
s.listen(1)

#  siap menerima koneksi
conn, addr = s.accept()
print ('Connection address:', addr)

# buka/buat file bernama hasil_upload.txt untuk menyimpan hasil dari file yang dikirim server
# masih hardcoded nama file, bertipe byte
f = open("hasil_upload.pdf", "w+b")

# loop forever
while 1:
    # terima pesan dari client
    RECEIVED = conn.recv(1024)

    # tulis pesan yang diterima dari client ke file kita (result.txt)
    f.write(RECEIVED)
    
    # berhenti jika sudah tidak ada pesan yang dikirim
    if not RECEIVED: break
    
# tutup file result.txt    
f.close()

#tutup socket
s.close()

# tutup koneksi
