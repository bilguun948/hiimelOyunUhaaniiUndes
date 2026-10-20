# Бүхэл тооны Tuple-н сондгой индекстэй сөрөг элементүүдийн үржвэрийг тооцоол.
a = tuple(map(int, input("Tuple-ийн элементүүд: ").split()))
print(a)

p = 1
found = False

for i in range(1, len(a), 2):
    if a[i] < 0:
        p *= a[i]
        found = True

print("Үржвэр =", p if found else 0)
