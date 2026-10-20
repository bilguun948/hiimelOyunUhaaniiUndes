# reviews.txt файлыг унших
with open("reviews.txt", "r", encoding="utf-8") as file:
    reviews = file.readlines()

# Эерэг болон сөрөг үгс
positive_words = ["love", "amazing", "fantastic", "recommend", "great"]
negative_words = ["worst", "disappointed", "not worth", "regret", "bad"]

results = []

# Сэтгэгдэл бүрийг шинжлэх
for review in reviews:
    review_lower = review.lower().strip()

    if any(word in review_lower for word in positive_words):
        sentiment = "Positive"
    elif any(word in review_lower for word in negative_words):
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    result = f"{review.strip()} -> Sentiment: {sentiment}"
    results.append(result)

# Үр дүнг файлд хадгалах
with open("results.txt", "w", encoding="utf-8") as output_file:
    for result in results:
        output_file.write(result + "\n")

# Үр дүнг дэлгэц дээр харуулах
print("=== Sentiment Analysis Results ===")

for result in results:
    print(result)

print("---------------------------------")
print(f"Total reviews analyzed: {len(reviews)}")
print("Results saved to results.txt")