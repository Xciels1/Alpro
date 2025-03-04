def cek_digit_belakang():
  angka1 = int(input("Masukkan angka pertama : "))
  angka2 = int(input("Masukkan angka kedua : "))
  angka3 = int(input("Masukkan angka ketiga : "))

  hasil1 = angka1 % 10
  hasil2 = angka2 % 10
  hasil3 = angka3 % 10

  if hasil1 == hasil2 or hasil1 == hasil3 or hasil2 == hasil3:
    return True
  
  else:
    return False

print(cek_digit_belakang())
