
tinggi = float(input("Masukkan tinggi dalam satuan meter(m): "))
bmi = float(input("Masukkan BMI yang di harapkan dalam kilogram(kg)): "))

bmi_diharapkan = bmi*(tinggi ** 2)

print(f"Berat badan yang diperlukan untuk mencapai BMI {bmi_diharapkan} dengan tinggi {tinggi} m adalah {bmi:.2f} kg")