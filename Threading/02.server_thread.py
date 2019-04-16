# import socket, sys, traceback dan threading
import socket, sys, traceback
from threading import Thread

# jalankan server
def main():
    start_server()

# fungsi saat server dijalankan
def start_server():
    # tentukan IP server
    HOST = "127.0.0.1"
    
    # tentukan port server
    PORT = 8888

    # buat socket bertipe TCP
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # option socket
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("Socket dibuat")

    # lakukan bind
    try:
        soc.bind((HOST, PORT))
    except:
        # exit pada saat error
        print("Bind gagal. Error : " + str(sys.exc_info()))
        sys.exit()

    # listen hingga 5 antrian
    soc.listen(5)
    print("Socket mendengarkan")

    # infinite loop, jangan reset setiap ada request
    while True:
        # terima koneksi
        conn, addr = soc.accept()
        
        # dapatkan IP dan port
        ip, port = str(addr[0]), str(addr[1])
        print("Connected dengan " + ip + ":" + port)

        # jalankan thread untuk setiap koneksi yang terhubung
        try:
            Thread(target=client_thread, args=(conn, ip, port)).start()
        except:
            # print kesalahan jika thread tidak berhasil dijalankan
            print("Thread tidak berjalan.")
            traceback.print_exc()

    # tutup socket
    soc.close()


def client_thread(connection, ip, port, max_buffer_size = 4096):
    # flag koneksi
    is_active = True

    # selama koneksi aktif
    while is_active:

        # terima pesan dari client
        client_input = connection.recv(max_buffer_size)
        
        # dapatkan ukuran pesan
        client_input_size = sys.getsizeof(client_input)
        
        # print jika pesan terlalu besar
        if client_input_size > max_buffer_size:
            print("The input size is greater than expected {}")

        # dapatkan pesan setelah didecode
        decoded_input = client_input.decode("utf-8").rstrip()
        client_input = str(decoded_input)
        
        # jika "quit" maka flag koneksi = false, matikan koneksi
        if "quit" in client_input:
            # ubah flag
            is_active = False
            print("Client meminta keluar")
            
            # matikan koneksi
            connection.close()
            print("Connection " + ip + ":" + port + " ditutup")
            
        else:
            # tampilkan pesan dari client
            print("Processing the input received from " + ip + ":" + port + " Message is: " + client_input)
            
# panggil fungsi utama
if __name__ == "__main__":
    main()