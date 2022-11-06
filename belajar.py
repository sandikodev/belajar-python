Nama = {}

NIM = {}

BukuPinjam = {}
def menu():
    x = str(input('meminjam buku y/n = '))
    if x == 'y':
        nama()
        ulang()
    else:
        menu()

def nama():
    Nama['Pelanggan 2'] = str(input('Masukkan nama = '))
    print('Nama Anda Telah Diinput')
    nim()

def nim():
    NIM['Pelanggan 2'] =int(input('Masukkan NIM = '))
    print('NIM Anda Telah Diinput')
    buku()
def buku():
    While buku1 in buku:
              print (buku1)
              
              
def ulang():

    print(' ')
    print('======================================')
    print('Rincian Peminjaman Buku Anda :')
    print('Nama        :', Nama['Pelanggan 2'])
    print('Nim         :', NIM['Pelanggan 2'])
    print('Judul Buku  :', BukuPinjam['Pelanggan 2'], BukuPinjam['Pelanggan 3'], BukuPinjam['Pelanggan 2'] )
    print('Selesaii')

menu()