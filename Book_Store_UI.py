import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import psycopg2
from PIL import ImageTk
try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

conn = psycopg2.connect(database="book_management_system", user="postgres", password="", host="localhost", port="5432")
cur = conn.cursor()

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Login Page",
                            command=lambda: controller.show_frame("PageOne"))
        button1.pack()
        
        self.imagePath = ImageTk.PhotoImage(file="BackgroundPic.jpeg")

        background_label = tk.Label(self, image=self.imagePath)
        background_label.pack(side="left", fill="x", expand=True)
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        def login():
            username = usernameEntry.get()
            password = passwordEntry.get()
            if len(username) >= 4 and len(password) >= 8:
                query = f"SELECT * FROM users WHERE user_id = 1"
                try:
                    cur.execute(query)
                    conn.commit()
                    messagebox.showinfo(title="Login", message="Login Successfully.")
                except Exception as e:
                    messagebox.showerror(title="Error", message=str(e))

        def signup():
            username = usernameEntry.get()
            password = passwordEntry.get()
            if len(username) >= 4 and len(password) >= 8:
                query = f"UPDATE users SET user_name = '{username}', user_password = '{password}' WHERE user_id = 1"
                cur.execute(query)
                conn.commit()
                messagebox.showinfo(title="Sign Up", message="Sign Up Successfully.")
            else:
                messagebox.showinfo(title="Invalid Input", message="Username must be at least 4 characters long and password must be at least 8 characters long.")


        usernamelbl = tk.Label(self, text="User ID: ")
        usernamelbl.grid(row=0, column=0, sticky="W", pady=10, padx=10)
        
        passwordlbl = tk.Label(self, text="Password: ")
        passwordlbl.grid(row=1, column=0, sticky="W", pady=10, padx=10)

        usernameEntry = tk.Entry(self, font=("Helvetica", 14))
        usernameEntry.insert(0, "")
        usernameEntry.grid(row=0, column=1, sticky="W", pady=10, padx=10)
       
        passwordEntry = tk.Entry(self, show="*", font=("Helvetica", 14))
        passwordEntry.insert(0, "")
        passwordEntry.grid(row=1, column=1, sticky="W", pady=10, padx=10)

        SignIn = tk.Button(self, text="Sign In ",
                            command=login)
        SignIn.grid(row=2, column=0, sticky="W", pady=10, padx=10)

        SignUp = tk.Button(self, text="Sign Up", 
                           command=signup)
        SignUp.grid(row=2, column=1, sticky="W", pady=10, padx=10)
        
        booksAll = tk.Button(self, text="Books Page",
                            command=lambda: controller.show_frame("PageTwo"))
        booksAll.grid(row=3, column=1, sticky="W", pady=10, padx=10)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.displayFrame = ttk.Frame(self, style='MainFrame.TFrame')
        self.displayFrame.grid(row=3, column=0, sticky="NSEW")

        self.addFrame = ttk.Frame(self, style='MainFrame.TFrame')
        self.addFrame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

        self.editFrame = ttk.Frame(self, style='MainFrame.TFrame')
        self.editFrame.grid(row=0, column=0, padx=350, pady=10, sticky="NSEW")

        self.searchFrame = ttk.Frame(self, style='MainFrame.TFrame')
        self.searchFrame.grid(row=0, column=0, padx=620, pady=10, sticky="NSEW")

        self.deleteFrame = ttk.Frame(self, style='MainFrame.TFrame')
        self.deleteFrame.grid(row=0, column=0 ,padx=950, pady=10, sticky="NSEW")

        self.open()

    def open(self):
        
        def add_book_record():
            isbn = isbnNumberEntry.get()
            isbnNumberEntry.delete(0, tk.END)
            book_title = bookTypeEntry.get()
            bookTypeEntry.delete(0, tk.END)
            price = float(priceEntry.get())
            priceEntry.delete(0, tk.END)
            published_year = int(yearEntry.get())
            yearEntry.delete(0, tk.END)
            category = categoryEntry.get()
            categoryEntry.delete(0, tk.END)
            quantity = int(quantityEntry.get())
            quantityEntry.delete(0, tk.END)
            total_sales = price * quantity
            book_status = statusEntry.get()
            statusEntry.delete(0, tk.END)
            book_type = typeEntry.get()
            typeEntry.delete(0, tk.END)
    
            query = f"INSERT INTO books (isbn_number, book_title, price, published_year, category, quantity, total_sales, book_status, book_type) VALUES ('{isbn}', '{book_title}', '{price}', '{published_year}', '{category}', '{quantity}', '{total_sales}', '{book_status}', '{book_type}')"
            cur.execute(query)
            conn.commit()
            messagebox.showinfo(title="Add Book",message="Book added successfully.")

        def edit():
            isbn = editISBN.get()
            editISBN.delete(0, tk.END)
            field = editField.get()
            editField.delete(0, tk.END)
            changer = editChanger.get()
            editChanger.delete(0, tk.END)

            confirmation = messagebox.askquestion("Confirmation", f"Are you sure you want to change the {field} of the book with ISBN {isbn}?")
            if confirmation == 'yes':
               query = f"UPDATE books SET {field} = %s WHERE isbn_number = %s"
               cur.execute(query, (changer, isbn))
               conn.commit()

               edited_info = f"ISBN: {isbn}\nField: {field}\nNew Value: {changer}"
               messagebox.showinfo("Edit Information", edited_info)
            else:
               messagebox.showinfo("No change made.")

        def search():
           searchCombo = searchCbx.get()
           searchCbx.delete(0, tk.END)
           searchValue = searchItem.get()
           searchItem.delete(0, tk.END)

           query_map = {
               "isbn_number": f"SELECT * FROM books WHERE isbn_number = '{searchValue}'",
               "book_title": f"SELECT * FROM books WHERE book_title = '{searchValue}'",
               "price": f"SELECT * FROM books WHERE price = '{searchValue}'",
               "published_year": f"SELECT * FROM books WHERE published_year = '{searchValue}'",
               "category": f"SELECT * FROM books WHERE category = '{searchValue}'"
            }
           
           query = query_map.get(searchCombo)
           if query:
               cur.execute(query)
               result = cur.fetchall()
               if len(result) == 0:
                    messagebox.showinfo("No book found with the given search criteria.")
               else:
                    book_info = ""
                    for row in result:
                        book_info += f"ISBN: {row[0]}\nTitle: {row[1]}\nPrice: {row[2]}\nPublished Year: {row[3]}\nCategory: {row[4]}\nQuantity: {row[5]}\nTotal Sales: {row[6]}\nBook Status: {row[7]}\nBook Type: {row[8]}\nPublisher ID: {row[9]}\nCustomer ID: {row[10]}\nTransaction ID: {row[11]}\nAuthors ID: {row[12]}\n\n"
                        messagebox.showinfo("Book Information", book_info)
           else:
                messagebox.showinfo("Invalid search field.")

        def delete_book():
            isbn_number = deleteEnt.get()
            deleteEnt.delete(0, tk.END)
            cur.execute(f"SELECT * FROM books WHERE isbn_number = '{isbn_number}'")
            test = cur.fetchall()
            if len(test) > 0:
                confirmation = messagebox.askquestion("Confirmation", f"Are you sure you want to delete the book with ISBN number {isbn_number}?")
                if confirmation == 'Yes':
                    cur.execute(f"UPDATE books SET deleted = True WHERE isbn_number = '{isbn_number}'")
                    conn.commit()
                    messagebox.showinfo("Success", "The book with this particular ISBN number has been soft-deleted from the system")
                elif confirmation == 'No':
                    messagebox.showinfo("Cancellation", "The book has not been deleted")
            else:
                messagebox.showinfo("Book Not Found", "There is no book with this particular ISBN number in the system")

        def display():
            cur.execute("SELECT * FROM books")
            result = cur.fetchall()
            displayList.delete(0, tk.END)
            for row in result:
                book_info = f"ISBN: {row[0]}, Title: {row[1]}, Price: {row[2]}, Published Year: {row[3]}, Category: {row[4]}"
                displayList.insert(tk.END, book_info)
        
        def clear():
            displayList.delete(0, tk.END)
        
        isbnlabel = ttk.Label(self.addFrame, text="ISBN Number: ")
        isbnlabel.grid(row=0, column=0, padx=10, sticky="NSEW")

        bookTitlelabel = ttk.Label(self.addFrame, text="Book Title")
        bookTitlelabel.grid(row=1, column=0, padx=10, sticky="NSEW")

        pricelabel = ttk.Label(self.addFrame, text="Price: ")
        pricelabel.grid(row=2, column=0, padx=10, sticky="NSEW")

        yearlabel = ttk.Label(self.addFrame, text="Published Year: ")
        yearlabel.grid(row=3, column=0, padx=10, sticky="NSEW")

        categorylabel = ttk.Label(self.addFrame, text="Category: ")
        categorylabel.grid(row=4, column=0, padx=10, sticky="NSEW")

        quantitylabel = ttk.Label(self.addFrame, text="Quantity: ")
        quantitylabel.grid(row=5, column=0, padx=10, sticky="NSEW")

        bookStatuslabel = ttk.Label(self.addFrame, text="Book Status: ")
        bookStatuslabel.grid(row=6, column=0, padx=10, sticky="NSEW")

        bookTypelabel = ttk.Label(self.addFrame, text="Book Type: ")
        bookTypelabel.grid(row=7, column=0, padx=10, sticky="NSEW")
        
        book_Status_Options = ["Available", "Sold Out", "Ordered"]
        selected_status_option = tk.StringVar()
        selected_status_option.set(book_Status_Options[0])

        book_Type_Options = ["Hardcopy", "Softcopy"]
        selected_type_option = tk.StringVar()
        selected_type_option.set(book_Type_Options[0])

        quantity_Options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
        selected_quantity_option = tk.StringVar()
        selected_quantity_option.set(quantity_Options[0])

        category_Options = ["Action", "Sci-Fi", "Animation", "Comedy", "Love", "Romance", "Crime", "Documentary", "Thriller", "Fantasy", "Drama", "Mystery", "War"]
        selected_category_option = tk.StringVar()
        selected_category_option.set(category_Options[0])

        change_Options = ["isbn_number", "book_title", "price", "published_year", "category", "quantity", "book_status", "book_type"]
        selected_change_option = tk.StringVar()
        selected_change_option.set(change_Options[0])

        search_Options = ["isbn_number", "book_title", "price", "published_year", "category"]
        selected_search_option = tk.StringVar()
        selected_search_option.set(search_Options[0])
        
        isbnNumberEntry = ttk.Entry(self.addFrame, font=("Helvetica", 14))
        isbnNumberEntry.grid(row=0, column=1, sticky="W", pady=10, padx=10)

        bookTypeEntry = ttk.Entry(self.addFrame, font=("Helvetica", 14))
        bookTypeEntry.grid(row=1, column=1, sticky="W", pady=10, padx=10)

        priceEntry = ttk.Entry(self.addFrame, font=("Helvetica", 14))
        priceEntry.grid(row=2, column=1, sticky="W", pady=10, padx=10)

        yearEntry = ttk.Entry(self.addFrame, font=("Helvetica", 14))
        yearEntry.grid(row=3, column=1, sticky="W", pady=10, padx=10)

        categoryEntry = ttk.Combobox(self.addFrame, values=category_Options, font=("Helvetica", 14))
        categoryEntry.grid(row=4, column=1, sticky="W", pady=10, padx=10)

        quantityEntry = ttk.Combobox(self.addFrame, values=quantity_Options, font=("Helvetica", 14))
        quantityEntry.grid(row=5, column=1, sticky="W", pady=10, padx=10)

        statusEntry = ttk.Combobox(self.addFrame, values=book_Status_Options, textvariable=selected_status_option, font=("Helvetica", 14))
        statusEntry.grid(row=6, column=1, sticky="W", pady=10, padx=10)

        typeEntry = ttk.Combobox(self.addFrame, values=book_Type_Options, textvariable=selected_type_option, font=("Helvetica", 14))
        typeEntry.grid(row=7, column=1, sticky="W", pady=10, padx=10)

        AddBook = ttk.Button(self.addFrame, text="Add Book", command=add_book_record)
        AddBook.grid(row=8, column=1, sticky="W", pady=10, padx=10)
        AddBook.configure()
        
        isbnNumberedit = ttk.Label(self.editFrame, text="ISBN_Number:")
        isbnNumberedit.grid(row=1, column=1, sticky="NSEW", padx=5, pady=10)

        field_edit = ttk.Label(self.editFrame, text="Field:")
        field_edit.grid(row=2, column=1, sticky="NSEW", padx=5, pady=10)

        field_changer = ttk.Label(self.editFrame, text="New Input:")
        field_changer.grid(row=3, column=1, sticky="NSEW", padx=5, pady=10)

        editISBN = ttk.Entry(self.editFrame, font=("Helvetica", 14))
        editISBN.grid(row=1, column=2, sticky="W", pady=10, padx=5)

        editField = ttk.Combobox(self.editFrame, values=change_Options, font=("Helvetica", 14))
        editField.grid(row=2, column=2, sticky="W", pady=10, padx=5)

        editChanger = ttk.Entry(self.editFrame, font=("Helvetica", 14))
        editChanger.grid(row=3, column=2, sticky="W", pady=10, padx=5)

        EditBook = ttk.Button(self.editFrame, text="Edit Book", command=edit)
        EditBook.grid(row=4, column=2, sticky="W", pady=10, padx=5)

        searchLabel = ttk.Label(self.searchFrame, text="Search By: ")
        searchLabel.grid(row=1, column=1, sticky="NSEW", pady=10, padx=5)

        enterLabel = ttk.Label(self.searchFrame, text="Enter Item: ")
        enterLabel.grid(row=2, column=1, sticky="NSEW", pady=10,padx=5)

        searchCbx = ttk.Combobox(self.searchFrame, values=search_Options, font=("Helvetica"))
        searchCbx.insert(0, "")
        searchCbx.grid(row=1, column=1, sticky="W", pady=10,padx=110) 

        searchItem = ttk.Entry(self.searchFrame, font=("Helvetica"))
        searchItem.insert(0, "")
        searchItem.grid(row=2, column=1, sticky="W", pady=10,padx=110) 

        searchBook = ttk.Button(self.searchFrame, text="Search Book", command=search)
        searchBook.grid(row=3, column=1, sticky="W", pady=30, padx=130)
        
        
        deletelbl = ttk.Label(self.deleteFrame, text="Delete By: ")
        deletelbl.grid(row=0, column=4, sticky="NSEW", pady=10, padx=5)

        deleteEnt = ttk.Entry(self.deleteFrame, font=("Helvetica"))
        deleteEnt.insert(0, "")
        deleteEnt.grid(row=0, column=4, sticky="W", pady=10, padx=120)

        deleteBook = ttk.Button(self.deleteFrame, text="Delete Book", command=delete_book)
        deleteBook.grid(row=1, column=4, sticky="W", pady=10, padx=20)
        
        displayList = ttk.Button(self.displayFrame, text="Display All Books",
                            command=display)
        displayList.grid(row=1, column=0, sticky="W", pady=10, padx=50)

        clearBook = ttk.Button(self.displayFrame, text="Clear Book List", 
                               command=clear)
        clearBook.grid(row=1, column=1, sticky="W", pady=10, padx=10)

        displayList = tk.Listbox(self.displayFrame, selectmode=tk.SINGLE, width=75, height=15)
        displayList.grid(row=2, column=0, columnspan=2, sticky="E", pady=2, padx=20)
        
        displayBook = ttk.Button(self.displayFrame, text="Go Back To The First Page",
                            command=lambda: self.controller.show_frame("StartPage"))
        displayBook.grid(row=3, column=0, sticky="W", pady=10, padx=50)
        
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()