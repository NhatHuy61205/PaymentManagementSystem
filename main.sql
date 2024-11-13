DROP DATABASE IF EXISTS cafe_payment_system;
CREATE DATABASE cafe_payment_system;
USE cafe_payment_system;

------------- DRINK TABLE 
 CREATE TABLE drinks (
    ID VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    ingredient VARCHAR(255),
    volume VARCHAR(50),
    temperature VARCHAR(50),
    price DECIMAL(10, 2),
    additives VARCHAR(255),
    preparation VARCHAR(255),
    description TEXT
);

INSERT INTO drinks (ID, name, ingredient, volume, temperature, price, additives, preparation, description)
VALUES
('D001', 'Espresso', 'Coffee beans', '30ml', 'Hot', 2.50, '', 'Brewed with high pressure', 'Strong and rich coffee shot.'),
('D002', 'Latte', 'Coffee beans, Milk', '240ml', 'Hot', 3.50, 'Vanilla syrup', 'Steamed milk with espresso', 'Smooth and creamy coffee with milk.'),
('D003', 'Iced Tea', 'Tea leaves, Sugar', '300ml', 'Cold', 2.00, 'Lemon slice', 'Brewed tea with ice', 'Refreshing iced tea with a hint of lemon.'),
('D004', 'Americano', 'Coffee beans, Water', '180ml', 'Hot', 2.20, '', 'Diluted espresso', 'Simple black coffee with a lighter taste.'),
('D005', 'Mocha', 'Coffee beans, Milk, Chocolate', '240ml', 'Hot', 4.00, 'Whipped cream', 'Espresso with chocolate and milk', 'Chocolatey coffee with a creamy finish.');

-------------- ACCOUNT TABLE 
CREATE TABLE account (
    username VARCHAR(50) PRIMARY KEY,
    password VARCHAR(255) NOT NULL,
    role ENUM('admin', 'user') NOT NULL
);

INSERT INTO account (username, password, role)
VALUES
('admin_user', 'adminpass123', 'admin'),
('john_doe', 'userpass456', 'user'),
('jane_smith', 'userpass789', 'user'),
('manager', 'managerpass111', 'admin');
