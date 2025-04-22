#PASSWORD CHECK
import re

def cek_kekuatan_password(password):
    # Cek panjang password
    if len(password) < 6 or len(password) > 20:
        return "Password tidak valid (panjang harus antara 6 hingga 20 karakter)"

    # Cek karakteristik password
    huruf_besar = re.search(r'[A-Z]', password)
    huruf_kecil = re.search(r'[a-z]', password)
    angka = re.search(r'\d', password)

    # Hitung jumlah kriteria yang terpenuhi
    kekuatan = sum([bool(huruf_besar), bool(huruf_kecil), bool(angka)])

    if kekuatan == 3:
        return "Password Kuat"
    elif kekuatan == 2:
        return "Password Sedang"
    elif kekuatan == 1:
        return "Password Lemah"
    else:
        return "Password tidak valid (tidak mengandung huruf besar/kecil/angka)"

# Contoh penggunaan
password_input = input("Masukkan password: ")
print(cek_kekuatan_password(password_input))

#SENSOR NOMOR
import re

def sensor_nomor_hp(kalimat):
    def sensor(nomor):
        if len(nomor) <= 6:
            return nomor
        awal = nomor[:3]
        akhir = nomor[-3:]
        tengah = 'x' * (len(nomor) - 6)
        return awal + tengah + akhir

    # Temukan semua nomor dengan minimal 7 digit
    nomor_ditemukan = re.findall(r'\b\d{7,}\b', kalimat)
    # Sensor semua nomor
    nomor_tersensor = [sensor(nomor) for nomor in nomor_ditemukan]
    return nomor_tersensor

# Contoh penggunaan
kalimat = "nomor hp saya adalah 0101029117 dan nomor hp teman saya adalah 10030110471"
hasil = sensor_nomor_hp(kalimat)
print(hasil)
print('\n'.join(hasil))
