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
