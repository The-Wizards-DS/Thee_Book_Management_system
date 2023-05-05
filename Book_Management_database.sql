!!pip install sqlalchemy
!!pip install ipython_sql

!!pip install psycopg2-binary

%load_ext sql
from sqlalchemy import create_engine

%sql postgresql://postgres:polpol@localhost:5432/booksys

%%sql

CREATE TYPE book_status_type AS ENUM('Available','Sold Out','Ordered');
CREATE TYPE book_type AS ENUM('Hardcopy', 'Softcopy');

CREATE TABLE Books(
    isbn_number SERIAL PRIMARY KEY NOT NULL,
    book_title VARCHAR(250) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    published_year INT NOT NULL,
    category VARCHAR(250) NOT NULL,
    quantity INT NOT NULL,
    total_sales DECIMAL(10,2) NOT NULL,
    book_status book_status_type NOT NULL,
    book_type book_type NOT NULL,
    
    authors_id INT,
    publisher_id INT,
    customer_id INT,
    transaction_id INT 
);


 CREATE TABLE Customers(
  
    customer_id SERIAL PRIMARY KEY NOT NULL,
    first_name VARCHAR(250) NOT NULL,
    last_name VARCHAR(250) NOT NULL,
    residential_address VARCHAR(250) NOT NULL,
    city VARCHAR(250) NOT NULL,
    province VARCHAR(250) NOT NULL,
    postal_code INT NOT NULL,
    contact_details VARCHAR(250) NOT NULL,
    email_address VARCHAR(250) UNIQUE NOT NULL,
    
    user_id INT,
    orders_id INT,
    cart_id INT,
    isbn_number INT,
    transaction_id INT 
);
 


CREATE TYPE gender_type AS ENUM('Female', 'Male');

CREATE TABLE employees(
    employee_id SERIAL PRIMARY KEY NOT NULL,
    first_name VARCHAR(250) NOT NULL,
    last_name VARCHAR(250) NOT NULL,
    residential_address VARCHAR(250) NOT NULL,
    contact_details VARCHAR(20) NOT NULL,
    email_address VARCHAR(250) UNIQUE NOT NULL,
    gender gender_type NOT NULL,
    position VARCHAR(250) NOT NULL,
    
    user_id INT,
    delivery_id INT,
    transaction_id INT 
);



CREATE TABLE Authors(
    authors_id SERIAL PRIMARY KEY NOT NULL,
    first_name VARCHAR(250) NOT NULL,
    last_name VARCHAR(250) NOT NULL,
    contact_details VARCHAR(30) NOT NULL,
    email_address VARCHAR(250) UNIQUE NOT NULL,
    
    isbn_number INT,
    publisher_id INT 
);



CREATE TYPE order_type AS ENUM('Online','In-Store');
CREATE TYPE order_status_type AS ENUM('Ready For Dispatch', 'Partially Dispatched','Dispatched','Delivered');

CREATE TABLE Orders(
    orders_id SERIAL PRIMARY KEY NOT NULL,
    description VARCHAR(250) NOT NULL,
    order_date DATE NOT NULL,
    order_type order_type NOT NULL,
    order_status order_status_type NOT NULL,
    
    delivery_id INT,
    customer_id INT,
    transaction_id INT 
);



CREATE TYPE delivery_status_type AS ENUM('Ready For Dispatch', 'Partially Dispatched','Dispatched','Delivered');

CREATE TABLE Deliveries(
    delivery_id SERIAL PRIMARY KEY NOT NULL,
    delivery_date DATE NOT NULL,
    delivery_time TIMESTAMP NOT NULL,
    delivery_status  delivery_status_type NOT NULL,

    employee_id INT,
    orders_id INT   
);



CREATE TABLE Publishers(
    publisher_id SERIAL PRIMARY KEY NOT NULL,
    publisher_name VARCHAR(250) NOT NULL,
    publishing_date DATE NOT NULL,
    address VARCHAR(250) NOT NULL,
    contact_details VARCHAR(12) NOT NULL,
    email_address VARCHAR(250) UNIQUE NOT NULL,
    
    authors_id INT,
    isbn_number INT 
);



CREATE TABLE Carts(
    cart_id SERIAL PRIMARY KEY NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    total_price DECIMAL(10,2) NOT NULL, 
    
    customer_id INT 
);



CREATE TYPE transaction_type AS ENUM('Debit Card','Credit Card','Voucher','Cash');

CREATE TABLE Transactions(
    transaction_id SERIAL PRIMARY KEY NOT NULL,
    description VARCHAR(250) NOT NULL,
    transaction_date DATE NOT NULL,
    gross_amount DECIMAL(10,2) NOT NULL,
    units INT NOT NULL,
    transaction_type transaction_type NOT NULL,
    
    isbn_number INT,
    customer_id INT,
    orders_id INT  
);



CREATE TABLE Users(
    user_id SERIAL PRIMARY KEY NOT NULL,
    user_name VARCHAR(250) NOT NULL CHECK(length(user_name) >= 4),
    user_password VARCHAR(250) NOT NULL CHECK(length(user_password) >= 8),
    email_address VARCHAR(250) UNIQUE NOT NULL,
    created_on TIMESTAMP(6) NOT NULL,
    last_login TIMESTAMP(6) NOT NULL,
    CHECK(user_name <> user_password),
    
    customer_id INT,
    employee_id INT 
);



CREATE TABLE BookAuthors(
    authors_id INT NOT NULL,
    isbn_number INT NOT NULL
);




INSERT INTO Books (book_title, price, published_year, category, quantity, total_sales, book_status, book_type)
VALUES
('The Great Gatsby', 345.99, 1925, 'Fiction', 100, 34599.00, 'Ordered', 'Softcopy'),
('To Kill a Mockingbird', 142.99, 1960, 'Fiction', 75, 10724.25, 'Available', 'Hardcopy'),
('1984', 91.99, 1949, 'Science Fiction', 50, 4599.50, 'Ordered', 'Softcopy'),
('Pride and Prejudice', 112.99, 1813, 'Romance', 90, 10169.10, 'Available', 'Softcopy'),
('The Catcher in the Rye', 110.99, 1951, 'Fiction', 60, 6659.40, 'Sold Out', 'Hardcopy'); 


INSERT INTO Customers(first_name, last_name, residential_address, city, province, postal_code, contact_details, email_address)
VALUES 
('James', 'Jean', '123 Main St', 'Ghanzi', 'Botswana', 3220, '0763456789', 'jamesjean@yahoo.com'),
('Amahle', 'Nkosi', '770 Bree St', 'Westdene', 'Gauteng', 1550, '0748989762', 'amahlenkosi12@gmail.com'),
('Carol', 'Mdluli', '1881 hazel Rd', 'Pinetown', 'Kwazulu-Natal', 1009, '0835667823', 'carolm19@gmail.com'),
('Jennifer', 'Moore', '4 standford Rd', 'Mbabane', 'Swaziland', 8240, '0762545678', 'jennym101@yahoo.com'),
('Asanda', 'Freedom', '11440 Main reef', 'Qghebeha', 'Eastern Cape', 5206, '0867979890', 'asandafreedom@yahoo.com'),
('Tshepo', 'Modise', '4321 Park St', 'Gaborone', 'Botswana', 1120, '0761234567', 'tshepomodise@gmail.com'),
('Lungelo', 'Ngubane', '7 Hill Rd', 'Durban', 'Kwazulu-Natal', 4001, '0827890987', 'lungelongs@gmail.com'),
('John', 'Doe', '99 Main St', 'Johannesburg', 'Gauteng', 2001, '0115678901', 'johndoe@gmail.com'),
('Sibusiso', 'Mhlongo', '55 Riverside Rd', 'Nelspruit', 'Mpumalanga', 1200, '0834567890', 'sibusisomhlongo@gmail.com'),
('Thato', 'Ramothibe', '10 Church St', 'Maseru', 'Lesotho', 100, '2675643210', 'thatormothibe@gmail.com');



INSERT INTO employees (first_name, last_name, residential_address, contact_details, email_address, gender, position)
VALUES 
('Sandile', 'Mthembu', '456 Main St', '0733578989', 'sandilem@gmail.com', 'Male', 'Driver'),
('Zandi', 'Louw', '321 Oak St', '0823456767', 'zandilouw@yahoo.com', 'Female', 'Manager'),
('John', 'Smith', '712 Broke Rd', '0817897623', 'bobsmith@egmail.com', 'Male', 'Till Operator'),
('Nhlanhla', 'McCoy', '177 Oak St', '0823478989', 'bobsmith@gmail.com', 'Female', 'Clerk'),
('Marcus', 'Sands', '120 Bouw Rd', '0789870899', 'bobsmith@eyahoo.com', 'Male', 'Consultant');


INSERT INTO Authors (first_name, lasst_name, contact_details, email_address)
VALUES 
('J.K.', 'Rowling', '0728989782', 'jkrowling@gmail.com'),
('Stephen', 'King', '0117289876', 'stephenking@gmail.com'),
('Dan', 'Brown', '0827890978', 'danbrown@yahoo.com'),
('Keith and Sons', 'Smith', '0117653456', 'smaith23@gmail.com'),
('Jenny', 'Lee', '0768976523', 'jennyl12n@gmail.com'),
 ('Margaret', 'Atwood', '0114567890', 'm.atwood@gmail.com'),
('Neil', 'Gaiman', '0836754321', 'ngaiman@yahoo.com'),
('Toni', 'Morrison', '0712345678', 'toni.morrison@gmail.com'),
('J.R.R.', 'Tolkien', '0823456789', 'j.r.r.tolkien@hotmail.com'),
('Haruki', 'Murakami', '0765432198', 'murakamih@gmail.com');


INSERT INTO Orders (description, order_date, order_type, order_status)
VALUES 
('Online', '2023-04-25', 'Online', 'Ready For Dispatch'),
('In-Store', '2023-04-25', 'In-Store', 'Partially Dispatched'),
('Online', '2023-04-24', 'Online', 'Dispatched'),
('In-Store', '2023-04-23', 'In-Store', 'Delivered'),
('In-Store', '2023-04-24', 'In-Store', 'Ready For Dispatch');

 

INSERT INTO Deliveries (delivery_date, delivery_time, delivery_status)
VALUES
      ('2023-04-25', '2023-04-25 14:30:00', 'Ready For Dispatch'),
      ('2023-04-26', '2023-04-25 12:30:00', 'Delivered'),
      ('2023-04-27', '2023-04-25 11:30:00', 'Dispatched'),
      ('2023-04-28', '2023-04-25 09:30:00', 'Delivered'),
      ('2023-04-29', '2023-04-25 07:30:00', 'Partially Dispatched');
      


INSERT INTO Publishers (publisher_name, publishing_date, address, contact_details,email_address)
VALUES 
     ('Pasa', '2022-01-01', '380 Main St', '0115678992', 'pasapublishers@pasa.com'),
     ('Lapa', '2019-01-02', '440 Gart Rd', '0125678930', 'lapapublishers@lapa.com'),
     ('Mpasa', '2012-04-01', '200 Hens St', '0350987629', 'mpasapublishers@mpasa.com'),
     ('Sheer', '2002-07-25', '125 Boolis Rd', '0123989071', 'sheerpublishers@sheer.com'),
     ('Blue Print', '2012-09-10', '990 Level St', '01245608291', 'blueprint1234@blueprint.com'),
     ('Harriman Books', '2022-02-15', '32 Park Avenue', '011-555-7890', 'info@harrimanbooks.com'),
     ('Liberty Press', '2020-05-10', '401 Elm Street', '012-345-6789', 'sales@libertypress.com'),
     ('Merritt Publishing', '2018-09-01', '1123 Main Road', '033-456-7890', 'info@merrittpublishing.com'),
     ('Goldsmith Publications', '2010-12-03', '800 Silver Lane', '011-234-5678', 'sales@goldsmithpublications.com'),
     ('Blue River Books', '2015-06-20', '321 Oak Street', '012-789-4560', 'info@blueriverbooks.com');
     

INSERT INTO Carts (quantity, price, total_price) 
VALUES 
      (2, 100.00, 200.00),
      (3, 150.00, 450.00),
      (1, 120.50, 120.50),
      (2, 110.00, 220.00),
      (1, 90.00, 90.00);
      


INSERT INTO Transactions (description, transaction_date, gross_amount, units, transaction_type)
VALUES 
      ('Payment for Order #123', '2023-04-25', 34599.00, 100, 'Credit Card'),
      ('Payment for Order #124', '2023-04-27', 10724.25, 75, 'Debit Card'),
      ('Payment for Order #125', '2023-04-28', 4599.50, 50, 'Voucher'),
      ('Payment for Order #126', '2023-04-29', 10169.10, 90, 'Credit Card'),
      ('Payment for Order #127', '2023-04-30', 6659.40, 60, 'Cash')
      ('Payment for Order #128', '2023-04-25', 34599.00, 100, 'Credit Card'),
      ('Payment for Order #129', '2023-04-27', 10724.25, 75, 'Debit Card'),
      ('Payment for Order #130', '2023-04-28', 4599.50, 50, 'Voucher'),
      ('Payment for Order #131', '2023-04-29', 10169.10, 90, 'Credit Card'),
      ('Payment for Order #132', '2023-04-30', 6659.40, 60, 'Cash');
      


INSERT INTO Users (user_name, user_password, email_address, created_on, last_login)
VALUES 
      ('Sandile@bkstore.com', 'sasandile12#', 'sandilem@gmail.com', NOW(), NOW()),
      ('Zandi@bkstore.com', 'zandilooo23%', 'zandilouw@yahoo.com', NOW(), NOW()),
      ('James@bkstore.com', 'jamesb123&&@', 'jamesjean@yahoo.com', NOW(), NOW()),
      ('Jennifer@bkstore.com', 'j@nniffer1090', 'jennym101@yahoo.com', NOW(), NOW()),
      ('Bob@bkstore.com', 'bobplum@hous##', 'bobsmith@gmail.com', NOW(), NOW());
      

 
ALTER TABLE books
 
 ADD CONSTRAINT fk_book_authors_id
      FOREIGN KEY(authors_id)
      REFERENCES Authors(authors_id),
    
 ADD CONSTRAINT fk_book_publisher_id
      FOREIGN KEY(publisher_id)
      REFERENCES Publishers(publisher_id),
    
 ADD CONSTRAINT fk_book_customer_id
      FOREIGN KEY(customer_id)
      REFERENCES Customers(customer_id),
    
 ADD CONSTRAINT fk_book_transaction_id
      FOREIGN KEY(transaction_id)
      REFERENCES Transactions(transaction_id);

         
 
 ALTER TABLE customers
    
 ADD CONSTRAINT fk_customer_user_id
      FOREIGN KEY(user_id)
      REFERENCES Users(user_id),
      
 ADD CONSTRAINT fk_customer_orders_id
      FOREIGN KEY(orders_id)
      REFERENCES Orders(orders_id),
      
 ADD CONSTRAINT fk_customer_cart_id
      FOREIGN KEY(cart_id)
      REFERENCES Carts(cart_id),
      
 ADD CONSTRAINT fk_customer_isbn_number
      FOREIGN KEY(isbn_number)
      REFERENCES Books(isbn_number),
      
 ADD CONSTRAINT fk_customer_transaction_id
      FOREIGN KEY(transaction_id)
      REFERENCES Transactions(transaction_id)


ALTER TABLE employees
ADD CONSTRAINT fk_user_id
      FOREIGN KEY(user_id)
      REFERENCES Users(user_id)
      
     


ALTER TABLE authors  
ADD CONSTRAINT fk_authors_isbn_number
      FOREIGN KEY(isbn_number)
      REFERENCES Books(isbn_number),
      
ADD CONSTRAINT fk_authors_publisher_id
      FOREIGN KEY(publisher_id)
      REFERENCES Publishers(publisher_id)


ALTER TABLE Orders
ADD CONSTRAINT fk_orders_delivery_id
      FOREIGN KEY(delivery_id)
      REFERENCES Deliveries(delivery_id),
      
ADD CONSTRAINT fk_orders_customer_id
      FOREIGN KEY(customer_id)
      REFERENCES Customers(customer_id),
    
ADD CONSTRAINT fk_orders_transaction_id
      FOREIGN KEY(transaction_id)
      REFERENCES Transactions(transaction_id)



ALTER TABLE Deliveries
    
ADD CONSTRAINT fk_deliveries_employee_id
      FOREIGN KEY(employee_id)
      REFERENCES Employees(employee_id),
      
ADD CONSTRAINT fk_deliveries_order_id
      FOREIGN KEY(orders_id)
      REFERENCES Orders(orders_id)
                   




ALTER TABLE Publishers
ADD CONSTRAINT fk_publishers_authors_id
      FOREIGN KEY(authors_id)
      REFERENCES Authors(authors_id),
      
ADD CONSTRAINT fk_publishers_isbn_number
      FOREIGN KEY(isbn_number)
      REFERENCES Books(isbn_number)



ALTER TABLE carts
ADD CONSTRAINT fk_carts_customer_id
FOREIGN KEY (customer_id)
REFERENCES customers (customer_id);


ALTER TABLE Transactions
ADD CONSTRAINT fk_transaction_isbn_number
      FOREIGN KEY(isbn_number)
      REFERENCES Books(isbn_number),
      
ADD CONSTRAINT fk_transactions_customer_id
      FOREIGN KEY(customer_id)
      REFERENCES Customers(customer_id),
      
ADD CONSTRAINT fk_transactions_orders_id
      FOREIGN KEY(orders_id)
      REFERENCES Orders(orders_id) 
      

ALTER TABLE Users 
ADD CONSTRAINT fk_users_customer_id
  FOREIGN KEY(customer_id)
  REFERENCES Customers(customer_id),
      
ADD CONSTRAINT fk_users_employee_id
  FOREIGN KEY(employee_id)
  REFERENCES Employees(employee_id)


ALTER TABLE BookAuthors
ADD CONSTRAINT fk_bookauthors_author_id
      FOREIGN KEY(authors_id)
      REFERENCES Authors(authors_id),
    
ADD CONSTRAINT fk_bookauthors_isbn_number
      FOREIGN KEY(isbn_number)
      REFERENCES Books(isbn_number)
      
     


      

