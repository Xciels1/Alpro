def hitungips():
    
    jumlah_mata_kuliah = int(input("Masukkan jumlah mata kuliah: "))
    total_bobot = 0
    sks_total = jumlah_mata_kuliah * 3
    print("Hitung IPS")
    print("==========")
    for i in range(1, jumlah_mata_kuliah +1):
        nilai = input(f"Masukkan nilai mata kuliah ke-{i}: ")
        if nilai == "A":
            total_bobot += 4
        elif nilai == "B":
            total_bobot += 3
        elif nilai == "C":
            total_bobot += 2
        elif nilai == "D":
            total_bobot += 1
        else:
            print("Nilai tidak valid! Masukkan A, B, C, atau D.")
    total_bobot = total_bobot * 3
    ips = total_bobot / sks_total
    print(f"IPS Anda adalah: {ips:.2f}")


hitungips()
