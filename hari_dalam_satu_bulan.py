while True:
  try:
    bulan = int(input("Masukkan bulan(1-12) : "))
    jumlah_hari = 31

    if 1 <= bulan <= 12:
        break
    else:
      print("bulan antara (1-12)")

  except Exception as e:
    print(e)
    print("bulan harus berupa angka")

if bulan % 2 == 0 and bulan != 2:
    jumlah_hari = jumlah_hari-1
    print(jumlah_hari)
elif bulan == 2:
    jumlah_hari = jumlah_hari - 3
    print(jumlah_hari)
else:
   print("jumlah hari pada bulan ini adalah :", jumlah_hari)
