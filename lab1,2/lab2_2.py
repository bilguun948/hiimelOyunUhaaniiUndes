Hour = int(input("Hour = "))
Minut = int(input("Minut = "))
Dura = int(input("Dura = "))

total = Hour * 60 + Minut + Dura

end_hour = (total // 60) % 24
end_minut = total % 60

print("Дуусах цаг:", end_hour)
print("Дуусах минут:", end_minut)