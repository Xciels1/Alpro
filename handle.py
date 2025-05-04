def kuis_sederhana():
    soal_kuis = "soal.txt"
    print(f"nama file1: {soal_kuis}")

    file = open(soal_kuis, "r")
    for line in file:
        if "||" in line:
            soal, jawaban_benar = line.strip().split("||")
            soal = soal.strip()
            jawaban_benar = jawaban_benar.strip().lower()

            print(soal)
            jawaban_user = input("Jawab: ").strip().lower()

            if jawaban_user == jawaban_benar:
                print("Jawaban benar!")
            else:
                print("Jawaban salah!")
    file.close()

kuis_sederhana()
