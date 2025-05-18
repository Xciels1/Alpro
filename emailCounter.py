# Meminta input nama file
txtfile = input('Masukkan nama file : ')

try:
    fhandle = open(txtfile)
except:
    print('File tidak dapat dibuka:', txtfile)
    quit()

# Buat dictionary kosong
diksioneri = dict()

# Membaca tiap baris dalam file
for baris in fhandle:
    # Hanya proses baris yang dimulai dengan 'From '
    if baris.startswith('From '):
        words = baris.split()
        email = words[1]  # Email ada di indeks ke-1
        diksioneri[email] = diksioneri.get(email, 0) + 1  # Tambahkan

print(diksioneri)
