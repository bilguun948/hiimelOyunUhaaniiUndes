# 2. Массивын дундаж тооцоолол
# Даалгавар: Хэрэглэгчээс массив (жагсаалт) оруулж, тухайн массивын
# дундажийг тооцоолж хэвлэ.

n = int(input("хэдэн тоо оруулах вэ? "))
massiv = []

for i in range(n):
    x = float(input(f"{i+1}-р тоо: "))
    massiv.append(x)

def dundaj(massiv):
    total = 0
    for x in massiv:
        total += x
    return total / len(massiv)
print("Массивын дундаж =", dundaj(massiv))


