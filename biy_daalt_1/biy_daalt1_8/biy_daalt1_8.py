# 8. JSON өгөгдөл боловсруулах
# Даалгавар: Python дээр json файл уншиж, түүний өгөгдлийг боловсруулж, тодорхой мэдээллийг гаргаж ав.
# Зорилго: Файл унших, JSON форматын өгөгдөлтэй ажиллах
import json

with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

for student in data["students"]:
    print("Нэр:", student["name"])
    print("Нас:", student["age"])
    print("Дүн:", student["grade"])
    print("----------------")

print("Дүн нь 90-ээс дээш оюутнууд:")

for student in data["students"]:
    if student["grade"] >= 90:
        print(student["name"], "-", student["grade"])
