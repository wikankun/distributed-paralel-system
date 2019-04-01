# import library SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCServer

# import xmlrpc bagian client
import xmlrpc.client

# buatlah fungsi bernama download()
def file_download():

    # buka file bernama "file_didownload.txt"
    with open("file_didownload.txt",'rb') as handle:
        # kirimkan file tersebut dalam bentuk xml dengan cara memanggil xmlrpc.client.Binary()
        x = handle.read()
        return xmlrpc.client.Binary(x)
        
# buat server pada IP dan port yang telah ditentukan
HOST = '127.0.0.1'
PORT = 8000
server = SimpleXMLRPCServer((HOST, PORT))

# print bahwa "server mendengarkan pada port xxx"
print ("Listening on port", PORT)

# register fungsi download pada server
server.register_function(file_download, 'download')

# jalankan server
server.serve_forever()
