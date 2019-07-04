# import library socket karena menggunakan IPC socket
import socket as sc

# definisikan IP server tujuan file akan diupload
HOST = "192.168.1.15"

# definisikan port number proses di server
PORT = 4044

# definisikan ukuran buffer untuk mengirim
buffer_size = 1024

# buat socket (apakah bertipe UDP atau TCP?)
s = sc.socket(sc.AF_INET, sc.SOCK_STREAM)

# lakukan koneksi ke server
s.connect((HOST, PORT))

# buka file bernama "hasil_download.txt bertipe byte
# masih hard code, file harus ada dalam folder yang sama dengan script python
f = open("hasil_download.pdf", "w+b")

# loop forever
while 1:
    # terima pesan dari client
    RECEIVED = s.recv(1024)
    
    # tulis pesan yang diterima dari client ke file kita (result.txt)
    f.write(RECEIVED)
    
    # berhenti jika sudah tidak ada pesan yang dikirim
    if not RECEIVED: break
    
# tutup file_hasil_download.txt    
f.close()

#tutup socket
s.close()