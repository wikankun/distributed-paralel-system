# import xmlrpc bagian client
import xmlrpc.client

# buat proxy untuk mengakses server. Gunakan parameter URL server yang akan diakses berupa IP dan port. Bentuk http://IP:port
proxy = xmlrpc.client.ServerProxy('http://127.0.0.1:8000')

# buat/buka file baru dengan nama "hasil_download.txt" sebagai hasil download dari server
with open("hasil_download.pdf","wb") as handle:
    
    # tulis/isi file hasil_download.txt dengan hasil dari memanggil fungsi "download" yang berada server
    # ubah file menjadi binary dengan menambahkan .data
    x = proxy.download().data
    handle.write(x)

print("Download file selesai")
