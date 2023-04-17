
# Function to display all books in the text file
# category = ["fiction" ,"horror", "romance" , "history","fantasy","mystery","memoir","thriller","politics"]
book_path = "/Users/damacm172_/Desktop/Book_Store/The_Book_Management_System/Books.txt"
def display_books():
    try:
        with open(book_path, "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No books found in the library.")
        

