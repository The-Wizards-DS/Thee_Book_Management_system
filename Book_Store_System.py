def search():
    isbn = input("Enter ISBN Number to search for: ")
    query = f"SELECT * FROM books WHERE isbn_number = '{isbn}'"
    result = %sql $query
    

    if len(result) == 0:
        print("No book found with the given ISBN number.")
    else:
       print("Book information:")
       for row in result:
           print(f"ISBN: {row.isbn_number}")
           print(f"Title: {row.book_title}")
           print(f"Price: {row.price}")
           print(f"Published Year: {row.published_year}")
           print(f"Category: {row.category}")
           print(f"Quantity: {row.quantity}")
           print(f"Total Sales: {row.total_sales}")
           print(f"Book Status: {row.book_status}")
           print(f"Book Type: {row.book_type}")
           print(f"Publisher ID: {row.publisher_id}")
           print(f"Customer ID: {row.customer_id}")
           print(f"Transaction ID: {row.transaction_id}")
           print(f"Authors ID: {row.authors_id}");