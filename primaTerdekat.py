n = int(input("Masukkan nilai n: "))

for i in range(2, n):
    if i == 2 or (i > 2 and all(i % j != 0 for j in range(2, int(i ** 0.5) + 1))):
        print(i, end=' ')
