fruits = ["алим", "банан", "жүрж", "гүзээлзгэнэ", "усан үзэм", "лийр"]

fruit_colors = {
    "алим": "улаан",
    "банан": "шар",
    "жүрж": "улбар шар",
    "гүзээлзгэнэ": "улаан",
    "усан үзэм": "ногоон",
    "лийр": "ногоон"
}

fruit_prices = [
    ("алим", 5000),
    ("банан", 6000),
    ("жүрж", 7000),
    ("гүзээлзгэнэ", 12000),
    ("усан үзэм", 10000),
    ("лийр", 5500)
]


def get_unique_colors():
    
    return set(fruit_colors.values())


def find_fruits_by_color(color):
    result = []

    for fruit, fruit_color in fruit_colors.items():
        if fruit_color == color:
            result.append(fruit)

    return result


def find_fruits_by_price(price):
    result = []

    for fruit, fruit_price in fruit_prices:
        if fruit_price == price:
            result.append(fruit)

    return result


def show_all_information():

    print("\n===== ЖИМСНИЙ МЭДЭЭЛЭЛ =====")

    print("\nЖимсний нэрс:")
    print(fruits)

    print("\nЖимс ба өнгө:")
    for fruit, color in fruit_colors.items():
        print(f"{fruit} -> {color}")

    print("\nӨвөрмөц өнгөнүүд:")
    print(get_unique_colors())

    print("\nЖимс ба үнэ:")
    for fruit, price in fruit_prices:
        print(f"{fruit} -> {price}₮")

show_all_information()

color = input("\nЖимсний өнгө оруулна уу: ")

color_result = find_fruits_by_color(color)

print("Тухайн өнгөтэй жимс:", color_result)

price = int(input("\nЖимсний үнэ оруулна уу: "))

price_result = find_fruits_by_price(price)

print("Тухайн үнэтэй жимс:", price_result)
