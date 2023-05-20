import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import psycopg2
from tkinter import messagebox

# ---------------------------------FUNCTIONS----------------------------------------#
conn = psycopg2.connect(database="book_management_system", user="postgres", password="", host="localhost", port="5432")
cur = conn.cursor()

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
        if confirmation in ['YES','yes','Y','y']:
            cur.execute(f"UPDATE books SET deleted = True WHERE isbn_number = '{isbn_number}'")
            conn.commit()
            messagebox.showinfo("Success", "The book with this particular ISBN number has been soft-deleted from the system")
        elif confirmation in ['NO','no','N','n']:
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
        
def login():
    username = usernameEntry.get()
    password = passwordEntry.get()

    if len(username) >= 4 and len(password) >= 8:
        query = f"UPDATE users SET user_name = '{username}', user_password = '{password}' WHERE user_id = 1"
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

# ---------------------------------FRAMES--------------------------------------------#
root = tk.Tk()

root.title("Wizards Book Store")
root.geometry("700x350")
root.attributes('-fullscreen', True)
root.configure(bg="blue")

# Create a custom style for the frame
style = ttk.Style()

mainFrame = ttk.Frame(root, style='MainFrame.TFrame')
mainFrame.grid(row=0, column=0, sticky="NSEW")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

style.configure('MainFrame.TFrame', borderwidth=4, relief="solid")

loginFrame = ttk.Frame(mainFrame, style='MainFrame.TFrame')
loginFrame.grid(row=0, column=0,pady=10, sticky="NSEW")

logoFrame = ttk.Frame(mainFrame, style='MainFrame.TFrame')
logoFrame.grid(row=0, column=1, padx=50,pady=10, sticky="NSEW")

displayFrame = ttk.Frame(mainFrame, style='MainFrame.TFrame')
displayFrame.grid(row=0 ,column=2, padx=50,pady=10,sticky="NSEW")

addFrame = ttk.Frame(mainFrame, style='MainFrame.TFrame')
addFrame.grid(row=1, column=0, padx=10, pady= 10,sticky="NSEW")

editFrame = ttk.Frame(mainFrame, style='MainFrame.TFrame')
editFrame.grid(row=1, column=1, padx=10,pady=50,sticky="NSEW")

searchFrame = ttk.Frame(mainFrame, style='MainFrame.TFrame')
searchFrame.grid(row=1 ,column=2, padx=10,pady=30,sticky="NSEW")

deleteFrame = ttk.Frame(mainFrame, style='MainFrame.TFrame')
deleteFrame.grid(row=2, column=0, padx=10,pady=5, sticky="NSEW")


# -------------------------OBJECTS--------------------------------------

LogoImageObject = Image.open("/Users/damacm172_/Desktop/Book_Store/The_Book_Management_System/logo.jpeg").resize((270, 250))
LogoImage = ImageTk.PhotoImage(LogoImageObject)

# -----------------------LOGIN LABELS--------------------------------------

username = ttk.Label(loginFrame, text="User ID: ")
username.grid(row=0, column=0, sticky="W", pady=10, padx=10)
username.configure(
)

password = ttk.Label(loginFrame, text="Password: ")
password.grid(row=1, column=0, sticky="W", pady=10, padx=10)
password.configure(
)

# -----------------------LOGIN ENTRY--------------------------------------
usernameEntry = ttk.Entry(loginFrame, font=("Helvetica", 14))
usernameEntry.insert(0, "")
usernameEntry.grid(row=0, column=1, sticky="W", pady=10, padx=10)
userEntry = usernameEntry.get()

passwordEntry = ttk.Entry(loginFrame, show="*", font=("Helvetica", 14))
passwordEntry.insert(0, "")
passwordEntry.grid(row=1, column=1, sticky="W", pady=10, padx=10)
passEntry = passwordEntry.get()

# ------------------------LOGIN BUTTON---------------------------------------

SignIn = ttk.Button(loginFrame, text="Sign In",command=login)
SignIn.grid(row=2, column=0, sticky="W", pady=10, padx=10)
SignIn.configure(
)

SignUp = ttk.Button(loginFrame, text="Sign Up",command=signup)
SignUp.grid(row=2, column=1, sticky="W", pady=10, padx=10)
SignUp.configure(
)

Logolabel = ttk.Label(logoFrame, image=LogoImage, background="#0F1110")
Logolabel.grid(row=0, column=0, padx=10, sticky="NSEW")

# -------------------------ADD LABELS-------------------------------------

isbnlabel = ttk.Label(addFrame, text="ISBN Number: ")
isbnlabel.grid(row=0, column=0, padx=10, sticky="NSEW")

bookTitlelabel = ttk.Label(addFrame, text="Book Title")
bookTitlelabel.grid(row=1, column=0, padx=10, sticky="NSEW")

pricelabel = ttk.Label(addFrame,  text="Price: ")
pricelabel.grid(row=2, column=0, padx=10, sticky="NSEW")

yearlabel = ttk.Label(addFrame, text="Published Year: ")
yearlabel.grid(row=3, column=0, padx=10, sticky="NSEW")

categorylabel = ttk.Label(addFrame, text="Category: ")
categorylabel.grid(row=4, column=0, padx=10, sticky="NSEW")

quantitylabel = ttk.Label(addFrame,  text="Quantity: ")
quantitylabel.grid(row=5, column=0, padx=10, sticky="NSEW")

bookStatuslabel = ttk.Label(addFrame, text="Book Status: ")
bookStatuslabel.grid(row=6, column=0, padx=10, sticky="NSEW")

bookTypelabel = ttk.Label(addFrame, text="Book Type: ")
bookTypelabel.grid(row=7, column=0, padx=10, sticky="NSEW")

# -------------------ADD DROPDOWN SET---------------------------------------
book_Status_Options = ["Available","Sold Out","Ordered"]
selected_status_option = StringVar()
selected_status_option.set(book_Status_Options[0])

book_Type_Option = ["Hardcopy", "Softcopy"]
selected_type_option = StringVar()
selected_type_option.set(book_Type_Option[0])

quantity_Option = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]
quantity_Option_en= StringVar()
quantity_Option_en.set(quantity_Option[0])

category_Option = ["Action","Sci-Fi","Animation","Comedy","Love","Romance","Crime","Documentary","Thriller","Fantasy","Drama","Mystery","War"]
category_Option_Com= StringVar()
category_Option_Com.set(category_Option[0])

change_Option = ["isbn_number","book_title","price","published_year","category","quantity","book_status","book_type"]
change_Option_fie= StringVar()
change_Option_fie.set(change_Option[0])

search_Option = ["isbn_number","book_title","price","published_year","category"]
search_Option_fie= StringVar()
search_Option_fie.set(search_Option[0])

# -------------------ADD ENTRY--------------------------------------------
isbnNumberEntry = ttk.Entry(addFrame, font=("Helvetica", 14))
isbnNumberEntry.insert(0, "")
isbnNumberEntry.grid(row=0, column=1, sticky="W", pady=10, padx=10)

bookTypeEntry = ttk.Entry(addFrame, font=("Helvetica", 14))
bookTypeEntry.insert(0, "")
bookTypeEntry.grid(row=1, column=1, sticky="W", pady=10, padx=10)

priceEntry = ttk.Entry(addFrame, font=("Helvetica", 14))
priceEntry.insert(0, "")
priceEntry.grid(row=2, column=1, sticky="W", pady=10, padx=10)

yearEntry = ttk.Entry(addFrame, font=("Helvetica", 14))
yearEntry.insert(0,"")
yearEntry.grid(row=3,column=1, sticky="W", pady=10, padx=10)

categoryEntry = ttk.Combobox(addFrame, values=category_Option, font=("Helvetica", 14))
categoryEntry.insert(0, "")
categoryEntry.grid(row=4, column=1, sticky="W", pady=10, padx=10)

quantityEntry = ttk.Combobox(addFrame,values=quantity_Option, font=("Helvetica", 14))
quantityEntry.insert(0, "")
quantityEntry.grid(row=5, column=1, sticky="W", pady=10, padx=10)

statusEntry = ttk.Combobox(addFrame, values= book_Status_Options,textvariable= selected_status_option,font=("Helvetica", 14))
statusEntry.insert(0, "")
statusEntry.grid(row=6, column=1, sticky="W", pady=10, padx=10)

typeEntry = ttk.Combobox(addFrame, values=book_Type_Option,textvariable=selected_type_option ,font=("Helvetica", 14))
typeEntry.insert(0, "")
typeEntry.grid(row=7, column=1, sticky="W", pady=10, padx=10)

AddBook = ttk.Button(addFrame, text="Add Book",command= add_book_record)
AddBook.grid(row=8, column=1, sticky="W", pady=10, padx=10)
AddBook.configure(
)
# ------------------------EDIT LABELS--------------------------------------
isbnNumberedit = ttk.Label(editFrame, text="ISBN_Number: ")
isbnNumberedit.grid(row=1, column=2, sticky="NSEW",pady=10, padx=5)

field_edit = ttk.Label(editFrame, text="Field: ")
field_edit.grid(row=2, column=2, sticky="NSEW",pady=10, padx=5)

field_changer = ttk.Label(editFrame, text="New Input: ")
field_changer.grid(row=3, column=2, sticky="NSEW",pady=10, padx=5)

# -----------------------EDIT ENTRY ---------------------------------------
editISBN = ttk.Entry(editFrame, font=("Helvetica", 14))
editISBN.insert(0, "")
editISBN.grid(row=1, column=2, sticky="W", pady=10, padx=100)

editField = ttk.Combobox(editFrame,values=change_Option,font=("Helvetica", 14))
editField.insert(0, "")
editField.grid(row=2, column=2,sticky="W", pady=10, padx=50)

editChanger = ttk.Entry(editFrame,  font=("Helvetica", 14))
editChanger.insert(0, "")
editChanger.grid(row=3, column=2,sticky="W", pady=10, padx=75)

EditBook = ttk.Button(editFrame, text="Edit Book",command=edit)
EditBook.grid(row=4, column=2, sticky="W", pady=10, padx=50)
EditBook.configure(
)

# ------------------------SEARCH LABELS--------------------------------------
searchLabel = ttk.Label(searchFrame, text="Search By: ")
searchLabel.grid(row=1, column=1, sticky="NSEW", pady=10, padx=5)

enterLabel = ttk.Label(searchFrame, text="Enter Item: ")
enterLabel.grid(row=2, column=1, sticky="NSEW", pady=10,padx=5)

# -----------------------SEARCH ENTRY ---------------------------------------
searchCbx = ttk.Combobox(searchFrame,values=search_Option, font=("Helvetica"))
searchCbx.insert(0, "")
searchCbx.grid(row=1, column=1, sticky="W", pady=10,padx=110) 

searchItem = ttk.Entry(searchFrame, font=("Helvetica"))
searchItem.insert(0, "")
searchItem.grid(row=2, column=1, sticky="W", pady=10,padx=110) 

searchBook = ttk.Button(searchFrame, text="Search Book",command=search)
searchBook.grid(row=3, column=1, sticky="W", pady=30, padx=130)
searchBook.configure(
)

# ------------------------DELETE LABELS--------------------------------------
deletelbl = ttk.Label(deleteFrame, text="Delete By: ")
deletelbl.grid(row=0, column=4, sticky="NSEW", pady=10, padx=5)

# -----------------------DELETE ENTRY ---------------------------------------

deleteEnt= ttk.Entry(deleteFrame, font=("Helvetica"))
deleteEnt.insert(0, "")
deleteEnt.grid(row=0, column=4, sticky="W", pady=10, padx=120)

deleteBook = ttk.Button(deleteFrame, text="Delete Book",command=delete_book)
deleteBook.grid(row=1,column=4, sticky="W", pady=10, padx=20)
deleteBook.configure(
)

# -----------------------DISPLAY BUTTON ---------------------------------------
displayBook = ttk.Button(displayFrame, text="Display All Book",command=display)
displayBook.grid(row=1,column=5, sticky="W", pady=10, padx=50)
displayBook.configure(   
)

clearBook = ttk.Button(displayFrame, text="Clear Book List",command=clear)
clearBook.grid(row=1,column=5, sticky="W", pady=10, padx=240)
clearBook.configure(   
)

displayList = Listbox(displayFrame, selectmode=SINGLE, width=75, height=15)
displayList.grid(row=2, column=5, sticky=E, pady=2,padx=20)
# --------------------GRIDS------------------------------
mainFrame.columnconfigure(2, weight=1)
mainFrame.rowconfigure(1, weight=1)

root.mainloop()
