user = {
    'nama': None,
    'nim': None,
    'buku': []
}


def menu():
    while True:
        print('meminjam buku => yes/no')
        print('1. yes untuk meminjam buku')
        print('2. no untuk keluar')
        x = str(input('> '))
        if (x == 'yes' or x == 'y' or x == '1'):
            simpanNama()
            simpanNim()
            simpanBuku()
            rincian()
        elif (x == 'no' or x == 'n' or x == '1'):
            break
        else:
            print('Perintah tidak dikenal')


def simpanNama():
    user['nama'] = str(input('\nMasukkan nama = '))
    print('Nama Anda telah diinput')


def simpanNim():
    user['nim'] = int(input('Masukkan nim = '))
    print('NIM Anda telah diinput')


def simpanBuku():
    while True:
        Buku = str(input('Masukan buku = '))
        user["buku"].append(Buku)

        action = str(input('\ntambah buku ? '))
        if (action == 'y' or action == 'yes'):
            continue
        elif (action == 'n' or action == 'no'):
            break
        else:
            print('Perintah tidak dikenal')
    print('Buku Anda telah diinput')


def rincian():
    print('\n======================================')
    print('Rincian Peminjaman Buku Anda :')
    print(f'Nama\t: {user["nama"]}')
    print(f'Nim\t: {user["nim"]}')
    print('Buku\t:')
    for index, buku in enumerate(user["buku"], start=1):
        print(f'\t{index}. {buku}')
    print('\nSelesaii\n')


menu()
