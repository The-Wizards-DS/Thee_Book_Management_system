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
