class WeatherAgent:
    def respond(self, weather):

        if weather.lower() == "rainy":
            return "Борооны шүхэр аваарай!"

        elif weather.lower() == "sunny":
            return "Нарны шилээ мартуузай!"

        elif weather.lower() == "snowy":
            return "Дулаан хувцас өмсөөрэй!"

        else:
            return "Цаг агаарын мэдээлэл тодорхойгүй байна."


agent = WeatherAgent()

user_input = input(
    "Цаг агаар ямар байна? (rainy, sunny, snowy): "
)

print("Agent:", agent.respond(user_input))
