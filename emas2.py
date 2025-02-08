
berat_awal = 25
berat_tambahan = 15
harga_per_gram_awal = 650000
harga_per_gram_tambahan = 685000

total_harga_beli_awal = berat_awal * harga_per_gram_awal
total_harga_beli_tambahan = berat_tambahan * harga_per_gram_tambahan

total_berat_emas = berat_awal + berat_tambahan
total_harga_beli = total_harga_beli_awal + total_harga_beli_tambahan

harga_per_gram = 715000
total_harga_jual = total_berat_emas * harga_per_gram

keuntungan_rp = total_harga_jual - total_harga_beli

keuntungan_persen = (keuntungan_rp / total_harga_beli) * 100

print(f"Keuntungan dalam Rupiah: Rp {keuntungan_rp:,}")
print(f"Keuntungan dalam Persen: {keuntungan_persen:.2f}%")
