

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
        

# Function to add a book to the text file
def add_book():
   
    book_name = input("Enter the name of the book: ")
    author_name = input("Enter the name of the author: ")
    price = input("Enter the price of the book: R")
    isbn_number = input("Enter the isbn number of the book: ")
    published_year = input("Enter the published year of the book: ")
    category = input("Enter the category of the book: ")
    quantity = input("Please enter the quantity of the book: ")
        
    book = str(book_name ) + " ," + str(author_name) + " ," +  str(price) + " ," + str(isbn_number)  + " ," + str(published_year) + " ," + str(category) + " ," + str(quantity)
    
    with open(book_path, 'a') as f:
        for i in f:
            if isbn_number in i:
                print("Book Already exists, added a copy")
                quantity = quantity + 1
                f.write(f"{book_name} by {author_name},{price},{isbn_number},{published_year},{category},{quantity}\n")
            else:
                f.write(book+ "\n")
        
    print("Book Added Successfully!")

# Function to edit a book in the text file
def edit_book():
    try:
        isbn_number = input("Enter the isbn of the book to edit: ")
        with open(book_path, "r+") as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                if isbn_number in line:
                    new_attributes = input("Enter new book attributes in the following format: 'Name,Author,Price,ISBN,Published Year,Category,Quantity': ")
                    lines[i] = f"{new_attributes}\n"
                    break
            else:
                print("Book not found!")
                return
            file.seek(0)
            file.truncate()
            file.writelines(lines)
        print("Book edited successfully!")
    except FileNotFoundError:
        print("No books found in the library.")



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

# Function to delete a book from the text file
def delete_book():
    isbn = input("Enter the isbn of the book to delete: ")
    try:
        with open(book_path, "r") as file:
            lines = file.readlines()
        with open(book_path, "w") as file:
            found = False
            for line in lines:
                if isbn in line:
                    found = True
                else:
                    file.write(line)
            if found:
                print("Book deleted successfully!")
            else:
                print("Book not found.")
    except FileNotFoundError:
        print("No books found.")

# Main function to run the program
def main():
    while True:
        print("\nWelcome to the book management system!")
        print("1. Display all books")
        print("2. Add a book")
        print("3. Search for a book")
        print("4. Edit a book")
        print("5. Delete a book")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            display_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            edit_book()
        elif choice == "5":
            delete_book()
        elif choice == "6":
            print("Thank you for visiting the book store, Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if name == "main":
    main()


