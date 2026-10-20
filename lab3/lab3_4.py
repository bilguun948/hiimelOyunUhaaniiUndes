import random

n = int(input("Жагсаалтын элементийн тоо: "))

A = []

for i in range(n):
    A.append(random.randint(10, 100))

print("Жагсаалт:", A)
