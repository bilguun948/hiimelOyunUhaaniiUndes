import matplotlib.pyplot as plt
import seaborn as sns

subjects = ["Математик", "Монгол хэл", "Англи хэл", "Програмчлал"]
scores = [85, 90, 78, 95]

sns.barplot(x=subjects, y=scores)

plt.title("Хичээлүүдийн дүн")
plt.xlabel("Хичээл")
plt.ylabel("Дүн")

plt.show()
