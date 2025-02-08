
berat_emas = 25 
harga_beli_gram = 650000 
harga_jual_gram = 685000 


total_beli = berat_emas * harga_beli_gram
total_jual = berat_emas * harga_jual_gram

untung_rp = total_jual- total_beli

untung_persen = (untung_rp / total_beli) * 100

print(f"Keuntungan dalam Rupiah: Rp {untung_rp:,}")
print(f"Keuntungan dalam Persen: {untung_persen:.2f}%")
