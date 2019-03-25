# import library socket karena menggunakan IPC socket


# definisikan IP untuk binding


# definisikan port untuk binding


# definisikan ukuran buffer untuk menerima pesan


# buat socket (bertipe UDP atau TCP?)


# lakukan binding ke IP dan port


# lakukan listen


#  siap menerima koneksi

print ('Connection address:', addr)

# buka/buat file bernama hasil_upload.txt untuk menyimpan hasil dari file yang dikirim server
# masih hardcoded nama file, bertipe byte



# loop forever
while 1:
    # terima pesan dari client
    
    
    # tulis pesan yang diterima dari client ke file kita (result.txt)
    
    
    # berhenti jika sudah tidak ada pesan yang dikirim
    if not data: break
    
# tutup file result.txt    


#tutup socket


# tutup koneksi

