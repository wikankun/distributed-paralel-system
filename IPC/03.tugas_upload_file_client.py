# import library socket karena menggunakan IPC socket
import socket as sc

# definisikan IP server tujuan file akan diupload
HOST = "192.168.1.8"

# definisikan port number proses di server
PORT = 4044

# definisikan ukuran buffer untuk mengirim
buffer_size = 1024

# buat socket (apakah bertipe UDP atau TCP?)
s = sc.socket(sc.AF_INET, sc.SOCK_STREAM)

# lakukan koneksi ke server
s.connect((HOST, PORT))

# buka file bernama "file_diupload.txt bertipe byte
# masih hard code, file harus ada dalam folder yang sama dengan script python
f = open("file_diupload.txt", "rb")

try:
    # baca file tersebut sebesar buffer 
    byte = f.read(buffer_size)

    # selama tidak END OF FILE; pada pyhton EOF adalah b''
    while byte != b'':
        # kirim hasil pembacaan file
        s.send(byte)
        
        # baca sisa file hingga EOF
        byte = f.read(buffer_size)

finally:
    print ("end sending")
    
    # tutup file jika semua file telah  dibaca
    f.close()

# tutup koneksi setelah file terkirim
s.close()