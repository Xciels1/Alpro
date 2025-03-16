def perkalian():
    pengali = int(input("Masukkan angka pengali: "))
    dikali = int(input("Masukkan angka yang dikali: "))
    hasil = 0
    print(f"{pengali} x {dikali} =", end=" ")
    for i in range(pengali):
        hasil += dikali
        if i == pengali - 1:
            print(dikali, "=", hasil)
        else:
            print(dikali, "+", end=" ")

perkalian()
