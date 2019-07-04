# import xmlrpc bagian client saja
import xmlrpc.client

# buat stub (proxy) untuk client
proxy = xmlrpc.client.ServerProxy('http://127.0.0.1:8008')

# lakukan pemanggilan fungsi vote("nama_kandidat") yang ada di server
print(proxy.vote('Iqbal'))

# lakukan pemanggilan fungsi querry() untuk mengetahui hasil persentase dari masing-masing kandidat
print(proxy.query())

# lakukan pemanggilan fungsi lain terserah Anda
# print(proxy.system.listMethods())