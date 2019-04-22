# import mpi4py
from mpi4py import MPI

# import library random untuk generate angka integer secara random
import random

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
size = comm.Get_size()

# generate angka integer secara random untuk setiap proses
angka = int(random.uniform(1, 100))

# lakukan penjumlahan dengan teknik reduce, root reduce adalah proses dengan rank 0
sum = comm.reduce(angka, op=MPI.SUM, root=0)

# jika saya proses dengan rank 0 maka saya akan menampilkan hasilnya
if rank == 0:
    print("Rank 0 worked out the total " + str(sum))
