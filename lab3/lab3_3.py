# Монгол хэлнээс англи хэл рүү хэд хэдэн үгийг хөрвүүлэх программ зохио. /Хиймэл оюуны 
# нэршилийн 10-с доошгүй үг/
dict = {"artificial intelligence":"хиймэл оюун","machine learning":"машин сургалт",
        "deep learning":"гүн сургалт","мэдрэлийн сүлжээ":"neural network",
        "data":"өгөгдөл","algorithm":"алгоритм",}

word = input("хиймэл оюуны нэршилийг англиар оруулна уу: ")
print(word)
if word in dict:
    print("монгол хэлээр:", dict[word])
else:
    print("Энэ нэршил тольд байхгүй байна.")