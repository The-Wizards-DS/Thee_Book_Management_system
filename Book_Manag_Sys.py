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
