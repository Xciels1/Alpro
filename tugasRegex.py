#8.1
def cek_anagram(kalimat1, kalimat2):
    kalimat1 = kalimat1.replace(" ", "").lower()
    kalimat2 = kalimat2.replace(" ", "").lower()


    if len(kalimat1) != len(kalimat2):
        return False

    return sorted(kalimat1) == sorted(kalimat2)


kalimat1 = input("Masukkan kata pertama: ")
kalimat2 = input("Masukkan kata kedua: ")

if cek_anagram(kalimat1, kalimat2):
    print(f"'{kalimat1}' adalah anagram dari '{kalimat2}'")
else:
    print(f"'{kalimat1}' bukan anagram dari '{kalimat2}'")

#8.2
import re

def hitung_kemunculan(teks, kata_dicari):
    
    teks_bersih = re.sub(r'[^a-zA-Z\s]', '', teks)
  
    teks_bersih = teks_bersih.lower()
    kata_dicari = kata_dicari.lower()


    daftar_kata = teks_bersih.split()

    jumlah = daftar_kata.count(kata_dicari)

    return jumlah


teks = input("Masukkan teks: ")
kata_dicari = input("Masukkan kata yang ingin dicari dalam teks: ")

jumlah = hitung_kemunculan(teks, kata_dicari)
print(f"Kata '{kata_dicari}' muncul sebanyak {jumlah} kali.")

#8.3
import re

def hapus_spasi_berlebih(teks):
    teks_bersih = re.sub(r'\s+', ' ', teks.strip())
    return teks_bersih


teks = input("Masukkan teks: ")
hasil = hapus_spasi_berlebih(teks)
print(f"Hasil: '{hasil}'")


#8.4
import re

def cari_kata_terpendek_terpanjang(kalimat):

    kalimat_bersih = re.sub(r'[^a-zA-Z\s]', '', kalimat)

    kalimat_bersih = kalimat_bersih.lower()

    daftar_kata = kalimat_bersih.split()


    if not daftar_kata:
        return None, None

    terpendek = min(daftar_kata, key=len)
    terpanjang = max(daftar_kata, key=len)

    return terpendek, terpanjang


kalimat = input("Masukkan kalimat: ")
terpendek, terpanjang = cari_kata_terpendek_terpanjang(kalimat)

print(f"Kata terpendek: {terpendek}")
print(f"Kata terpanjang: {terpanjang}")


#8.5
import re

hari_bulan = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def kabisat(tahun):
    if tahun % 4 == 0 and (tahun % 100 != 0 or tahun % 400 == 0):
        return True
    return False

def hitung_hari(tahun, bulan, hari):
    total = (tahun - 1) * 365
    total += (tahun - 1) // 4
    total -= (tahun - 1) // 100
    total += (tahun - 1) // 400
    for i in range(bulan - 1):
        total += hari_bulan[i]
    if bulan > 2 and kabisat(tahun):
        total += 1
    total += hari
    return total

teks = """Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan nasional,
seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki Hajar Dewantara (1889-05-02)."""

tahun_skrg = 2025
bulan_skrg = 4
hari_skrg = 27
hari_sekarang = hitung_hari(tahun_skrg, bulan_skrg, hari_skrg)

tanggal = re.findall(r'\d{4}-\d{2}-\d{2}', teks)

for tgl in tanggal:
    tahun, bulan, hari = map(int, tgl.split('-'))
    hari_lalu = hitung_hari(tahun, bulan, hari)
    selisih = hari_sekarang - hari_lalu
    print(f"{hari:02d}-{bulan:02d}-{tahun} selisih {selisih} hari")


#8.6
import re
import random
import string

# contoh input teks
teks = """
Berikut adalah daftar email dan nama pengguna dari mailing list:
anton@mail.com dimiliki oleh antonius
budi@gmail.co.id dimiliki oleh budi anwari
slamet@getnada.com dimiliki oleh slamet slumut
matahari@tokopedia.com dimiliki oleh toko matahari
"""


pattern = r'([\w\.-]+)@[\w\.-]+'


usernames = re.findall(pattern, teks)

def generate_password(length=8):
    karakter = string.ascii_letters + string.digits
    return ''.join(random.choice(karakter) for _ in range(length))

emails = re.findall(r'[\w\.-]+@[\w\.-]+', teks)

for email, username in zip(emails, usernames):
    password = generate_password()
    print(f"{email} username: {username} , password: {password}")

