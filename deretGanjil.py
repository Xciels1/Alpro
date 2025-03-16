def ganjil():
  batas_atas = int(input("Masukkan batas atas: "))
  batas_bawah = int(input("Masukkan batas bawah: "))

  if batas_atas < batas_bawah:
    for i in range(batas_bawah, batas_atas -1, -1):
        if i % 2 != 0:
          print(i, end=" ")
  elif batas_atas > batas_bawah:
    for i in range(batas_bawah, batas_atas, 1):
        if i % 2 != 0:
          print(i, end=" ")

ganjil()
