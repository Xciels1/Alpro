uang_disimpan = 200000000
target = 400000000
bunga = 0.1
tahun = 0

while uang_disimpan < target :
  uang_disimpan += uang_disimpan * bunga
  tahun += 1

print(f"waktu yang di butuhkan adalah {tahun} tahun")

