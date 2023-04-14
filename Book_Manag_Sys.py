# Function to search for a book in the text file
def search_book():
    search_cat = input("search for book by category, author, genre or isbn: ")
    
    try:
        with open(book_path, "r") as file:
            found = False
            for line in file:
                if search_cat in line:
                    found = True
                    print(line.strip())
            if not found:
                print("Book not found in the library.")
    except FileNotFoundError:
        print("No books found in the library.")