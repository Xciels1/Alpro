def keuangan_budi(gaji_jam, jam_minggu):
    minggu_kerja = 5
    total_pendapatan = gaji_jam * jam_minggu * minggu_kerja
    
    pajak = 0.14 * total_pendapatan
    pendapatan_bersih = total_pendapatan - pajak
    
    pakaianAksesoris = 0.10 * pendapatan_bersih
    alat_tulis = 0.01 * pendapatan_bersih
    
    sisa_uang = pendapatan_bersih - pakaianAksesoris - alat_tulis
    sedekah = 0.25 * sisa_uang
    
    anak_yatim = 0.30 * sedekah
    kaum_dhuafa = sedekah - anak_yatim
    
    return total_pendapatan, pendapatan_bersih, pakaianAksesoris, alat_tulis, sedekah, anak_yatim, kaum_dhuafa


gaji_jam = float(input("Masukkan gaji per jam: "))
jam_minggu = float(input("Masukkan jumlah jam kerja per minggu: "))


total_pendapatan, pendapatan_bersih, pakaianAksesoris, alat_tulis, sedekah, anak_yatim, kaum_dhuafa = keuangan_budi(gaji_jam, jam_minggu)


print(f"Pendapatan sebelum pajak: Rp {total_pendapatan}")
print(f"Pendapatan setelah pajak: Rp {pendapatan_bersih}")
print(f"Pengeluaran untuk pakaian dan aksesoris: Rp {pakaianAksesoris}")
print(f"Pengeluaran untuk alat tulis: Rp {alat_tulis}")
print(f"Jumlah uang yang disedekahkan: Rp {sedekah}")
print(f"Jumlah uang yang diterima anak yatim: Rp {anak_yatim}")
print(f"Jumlah uang yang diterima kaum dhuafa: Rp {kaum_dhuafa}")
