print("Welcome to the gobbledygook books library, pls feel free to share your favourite books")

books = []

while True:
    tell = input("Enter your favourite book (Type done to exit): ")
    
    if tell.lower() == "done":
        break

    books.append(tell)

print("Your favourite book(s) are", books)


a = len(books)
print(f"There are {a} book(s)")

