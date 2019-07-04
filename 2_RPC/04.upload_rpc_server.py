# import SimpleXMLRPCServer bagian server
from xmlrpc.server import SimpleXMLRPCServer

# buat fungsi bernama file_upload()
def file_upload(filedata):
    
    # buka file 
    with open("hasil_upload.txt",'wb') as handle:
        #convert from byte to binary IMPORTANT!
        data1 = filedata.data
        
        # tulis file tersebut
        handle.write(data1)

        return True #IMPORTANT
        
# must have return value
# else error messsage: "cannot marshal None unless allow_none is enabled"

# buat server
HOST = '127.0.0.1'
PORT = 8000
server = SimpleXMLRPCServer((HOST, PORT))

# tulis pesan server telah berjalan
print ("Listening on port", PORT)

# register fungsi 
server.register_function(file_upload, 'upload')

# jalankan server
server.serve_forever()
