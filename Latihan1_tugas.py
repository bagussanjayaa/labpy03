import random

n = int(input("Masukkan nilai N: "))

count = 1

while count < n+1:

    angka = random.random()

    if angka < 0.5:
        print(f"data ke {count} = {angka}")
        count += 1
