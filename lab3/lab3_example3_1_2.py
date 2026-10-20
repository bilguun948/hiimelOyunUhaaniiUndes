import random

# 1. Номнууд нэмэх (Толь бичгийн жагсаалт)
library_books = []

def add_book(title, author, year):
    book = {"title": title, "author": author, "year": year}
    library_books.append(book)
    print(f"Book '{title}' added.")

# 2. Зохиогчдыг нэмэх (өвөрмөц зохиолчдын олонлог)
unique_authors = set()

def update_authors():
    for book in library_books:
        unique_authors.add(book["author"])

# 3. Номын дэлгэрэнгүйг нэрээр нь жагсаах 
book_details = {}

def create_book_lookup():
    book_details.clear()
    for book in library_books:
        book_details[book["title"]] = book

def get_book_details_by_title(title):
    book = book_details.get(title)
    if book:
      return (f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")
    else:
        return ("Book not found.")

# 4. Жилд авах номыг тоолох.(tuple-д жил ба номын тоог хадгална)  
book_counts_per_year = ()

def calculate_book_counts_per_year():
    counts = {}

    for book in library_books:
        year = book["year"]
        counts[year] = counts.get(year, 0) + 1

    global book_counts_per_year
    book_counts_per_year = tuple(sorted(counts.items()))

def get_book_count_by_year(year):
    for year_count, count in book_counts_per_year:
        if year_count == year:
            return f"Books published in {year}: {count}"
    return f"No books published in {year}."

# 5. Find Books by Author
def find_books_by_author(author):
    books_found = []
    for book in library_books:
        if book["author"] == author:
            books_found.append(book)
    if books_found:
        return books_found
    else:
      return "No books found by that author."

# 6. Номыг хуваалцсан зохиогчдыг олох
def find_shared_authors(titles):
  authors_for_titles = []
  for title in titles:
    if title in book_details:
        authors_for_titles.append(book_details[title]["author"])
  author_set = set(authors_for_titles)
  if len(author_set) < len(authors_for_titles):
    return f"Shared authors among titles: {author_set}"
  else:
     return f"No shared authors among titles, or all authors are different."


#Доорх өгөгдлийг ашиглан эхлүүлнэ үү 
add_book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979)
add_book("Pride and Prejudice", "Jane Austen", 1813)
add_book("1984", "George Orwell", 1949)
add_book("The Lord of the Rings", "J.R.R. Tolkien", 1954)
add_book("To Kill a Mockingbird", "Harper Lee", 1960)
add_book("The Cat in the Hat", "Dr. Seuss", 1957)
add_book("The Hobbit", "J.R.R. Tolkien", 1937)
add_book("The Little Prince", "Antoine de Saint-Exupéry", 1943)
add_book("Jane Eyre", "Charlotte Brontë", 1847)
add_book("Moby Dick", "Herman Melville", 1851)
add_book("The Picture of Dorian Gray", "Oscar Wilde", 1890)
add_book("The Wonderful Wizard of Oz", "L. Frank Baum", 1900)

update_authors()
create_book_lookup()
calculate_book_counts_per_year()

# Хэрэглээний жишээ
print("\n--- Номын сангийн үйл ажиллагаа ---")

# Номын сангийн бүх номын нэрийн жагсаалт
print("\nНомын сан дахь бүх номын нэр:")
for book in library_books:
  print(f" - {book['title']}")

# Номын тухай дэлгэрэнгүй мэдээлэл
print("\nНомын дэлгэрэнгүйг номын нэрээр нь харуул:")
print(get_book_details_by_title("1984"))
print(get_book_details_by_title("Nonexistent Book"))


# Номын сан дахь бүх өвөрмөц зохиолчдыг харуул
print("\nНомын сан дахь бүх өвөрмөц зохиолчид:", unique_authors)

# Тодорхой жилийн номын тоог авна
print("\nЖилд хэвлэгддэг ном:")
print(get_book_count_by_year(1954))
print(get_book_count_by_year(1901))


# Тодорхой зохиолчийн номыг хайж олох
print("\nТодорхой зохиолчийн номыг хайж олох:")
print(find_books_by_author("J.R.R. Tolkien"))
print(find_books_by_author("Nonexistent Author"))

# Хуваалцсан зохиогчдыг хайж олох
print("\nНомын нэрсийн дундаас хуваалцсан зохиолчдыг олно:")
print(find_shared_authors(["The Hobbit", "The Lord of the Rings"]))
print(find_shared_authors(["The Hobbit", "1984"]))
print(find_shared_authors(["Pride and Prejudice", "Jane Eyre", "Moby Dick"]))
