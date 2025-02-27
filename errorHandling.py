#looping
while True:
    
  try :
    umur = int(input("Masukkan umur anda\n>> "))

    if umur > 30:
      print("tuwa")
    else:
      print("mudah")

  except ValueError:
    print("input berupa angka")

#try-except

try :
  umur = int(input("Masukkan umur anda\n>> "))

  if umur > 30:
    print("tuwa")
  else:
    print("mudah")

except ValueError:
  print("input berupa angka")
