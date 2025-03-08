#NO LAMBDA
konversi = int(input("Konversi Ke\n1.Fahrenheit\n2.Reamur\n>>"))
while konversi < 1 or konversi > 2:
  print("input todak valid")
  konversi = int(input("Konversi Ke\n1.Fahrenheit\n2.Reamur\n>>"))


if konversi == 1:
  print("Konversi celcius ke fahrenheit")
  def konversi_Fahrenheit():
    c = float(input("Masukkan nilai celcius : "))
    fahrenheit = (9/5) * c + 32

    return f"F = {fahrenheit}"
  print(konversi_Fahrenheit())
else:
    print("Konversi celcius ke reamur")
    def konversi_Reamur():
     c = float(input("Masukkan nilai celcius : "))
     reamur = 0.8 * c
   
     return f"R = {reamur}"
    print(konversi_Reamur()) 

#WITH LAMBDA
konversi = int(input("1. Suhu Celcius ke Fahrenheit\n2. Suhu Fahrenheit ke Celcius\n>>"))

while konversi < 1 or konversi > 2:
  print("Inputan tidak valid")
  konversi = int(input("1. Suhu Celcius ke Fahrenheit\n2. Suhu Fahrenheit ke Celcius\n>>"))

if konversi == 1:
  print("Konversi Suhu Celcius ke Fahrenheit")
  celcius = float(input("Masukkan suhu dalam Celcius : "))
  fahrenheit = lambda celcius : (celcius * 9/5) + 32
  print("Suhu dalam Fahrenheit adalah", fahrenheit(celcius))

else:
  print("Konversi Suhu Celcius  ke reamur")
  celcius = float(input("Masukkan suhu dalam celcius : "))
  reamur = lambda celcius : 0.8 * celcius
  print("Suhu dalam reamur adalah", reamur(celcius))
