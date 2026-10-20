
class EnvironmentAgent:
    def __init__(self, pollution_level):
        if not 0 <= pollution_level <= 100:
            raise ValueError("Бохирдлын түвшин 0-100 хооронд байна.")

        self.pollution_level = pollution_level

    def act(self):
        if self.pollution_level > 70:
            return "Бохирдол өндөр байна. Агаар шүүгч асаана уу."
        elif self.pollution_level > 30:
            return "Бохирдол дунд зэрэг байна. Цонхоо хаана уу."
        else:
            return "Бохирдол бага байна. Бүх зүйл хэвийн."


# Туршилт
try:
    pollution_level = int(
        input("Орчны бохирдлын түвшин (0-100): ")
    )

    agent = EnvironmentAgent(pollution_level)
    print("Agent:", agent.act())

except ValueError as error:
    print("Алдаа:", error)
