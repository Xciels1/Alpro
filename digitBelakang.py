#1
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

#2
def cek_digit_belakang(angka1, angka2, angka3):

  hasil1 = angka1 % 10
  hasil2 = angka2 % 10
  hasil3 = angka3 % 10

  if hasil1 == hasil2 or hasil1 == hasil3 or hasil2 == hasil3:
    return True
  
  else:
    return False

#TEST CASE

# print(cek_digit_belakang(30, 20, 18)) true
# print(cek_digit_belakang(145, 5, 100)) true
# print(cek_digit_belakang(71, 187, 18)) false
# print(cek_digit_belakang( 1024, 14, 94)) true
# print(cek_digit_belakang( 53, 8900, 658)) false
