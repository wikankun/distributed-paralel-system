# import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCServer

# import SimpleXMLRPCRequestHandler
from xmlrpc.server import SimpleXMLRPCRequestHandler

import threading

# Batasi hanya pada path /RPC2 saja supaya tidak bisa mengakses path lainnya
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Buat server
with SimpleXMLRPCServer(("127.0.0.1", 8008),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # buat data struktur dictionary untuk menampung nama_kandidat dan hasil voting
    kandidat = {    
        "Bambang": 0,
        "Iqbal": 0,
        "Nurhadi": 0
    }
    
    # kode setelah ini adalah critical section, menambahkan vote tidak boeh terjadi race condition
    # siapkan lock
    lock = threading.Lock()
    
    #  buat fungsi bernama vote_candidate()
    def vote_candidate(x):
        
        # critical section dimulai harus dilock
        lock.acquire()
        # jika kandidat ada dalam dictionary maka tambahkan nilai votenya
        if x in kandidat:
            kandidat[x] += 1
            pesan = "Terimakasih, voting untuk {} diterima".format(x)
        else:
            pesan =  "Kandidat {} tidak terdaftar".format(x)     
        # critical section berakhir, harus diunlock
        lock.release()
        return pesan
    
    # register fungsi vote_candidate() sebagai vote
    server.register_function(vote_candidate, 'vote')

    # buat fungsi bernama querry_result
    def querry_result():
        # critical section dimulai
        lock.acquire()
        
        # hitung total vote yang ada
        total_vote = sum([x for x in kandidat.values()])
        
        persentase = ''
        # hitung hasil persentase masing-masing kandidat
        for i in kandidat:
            persentase += i+ ' ' + str(kandidat[i]/total_vote*100)+'%, '
            
        # critical section berakhir
        lock.release()
        return persentase
        
    # register querry_result sebagai querry
    server.register_function(querry_result, 'query')

    print ("Server voting berjalan...")
    # Jalankan server
    server.serve_forever()
