# import library socket karena menggunakan IPC socket


# definisikan IP server tujuan file akan diupload


# definisikan port number proses di server


# definisikan ukuran buffer untuk mengirim


# buat socket (apakah bertipe UDP atau TCP?)


# lakukan koneksi ke server


# buka file bernama "file_diupload.txt bertipe byte
# masih hard code, file harus ada dalam folder yang sama dengan script python


try:
    # baca file tersebut sebesar buffer 
    
    
    # selama tidak END OF FILE; pada pyhton EOF adalah b''
    while byte != b'':
        # kirim hasil pembacaan file
        
        
        # baca sisa file hingga EOF
        
        #print(byte)
finally:
    print ("end sending")
    
    # tutup file jika semua file telah  dibaca
    

# tutup koneksi setelah file terkirim
