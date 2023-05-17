def display():
    %sql SELECT * FROM books;

    result = %sql SELECT * FROM books;
    print(result);
    

def main():
    option = int(input("Please select option From the book system:"))
      
    print("1: Add Book")
    print('2: Edit Details')
    print('3: Search Order')
    print('4: Delete Order')
    print('5: Display Order')
   
    

        
    if option == 1:
        add_book_record()
    elif option == 2:
        edit()
    elif option == 3:
        search()
    elif option == 4:
        delete_book()
    elif option == 5:
        display()
    else:
        print("invalid option")
 
  
main()
