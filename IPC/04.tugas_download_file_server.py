# import library socket karena menggunakan IPC socket
import socket as sc

# definisikan IP untuk binding
HOST = "192.168.1.8"

# definisikan port untuk binding
PORT = 4044

# definisikan ukuran buffer untuk menerima pesan
buffer_size = 1024

# buat socket (bertipe UDP atau TCP?)
s = sc.socket(sc.AF_INET, sc.SOCK_DGRAM)

# lakukan binding ke IP dan port
s.bind((HOST, PORT))

# lakukan listen
s.listen(1)

#  siap menerima koneksi
conn, addr = s.accept()
print ('Connection address:', addr)

# buka file bernama "file_didownload.txt
# masih hard code, file harus ada dalam folder yang sama dengan script python
f = open("file_didownload.txt", "rb")

try:
    # baca file tersebut sebesar buffer 
    byte = f.read(buffer_size)
    
    # selama tidak END OF FILE; pada pyhton EOF adalah b''
    while byte != b'':
        # kirim hasil pembacaan file dari server ke client
        s.send(byte)
        
        # baca sisa file hingga EOF
        byte = f.read(buffer_size)
        
finally:
    print ("end sending")
    
    # tutup file jika semua file telah  dibaca
    f.close()

# tutup socket
s.close()

# tutup koneksi
