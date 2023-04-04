CREATE DATABASE shop;

USE shop;

CREATE TABLE products (
    id INT(11) NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE customers (
    id INT(11) NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE orders (
    id INT(11) NOT NULL AUTO_INCREMENT,
    customer_id INT(11) NOT NULL,
    product_id INT(11) NOT NULL,
    quantity INT(11) NOT NULL,
    total_price DECIMAL(10,2) NOT NULL,
    order_date DATETIME NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

use shop;
ALTER TABLE orders ADD send BOOLEAN NOT NULL DEFAULT FALSE;
GRANT UPDATE,DELETE ON CUSTOMERS TO 'test'@'localhost';
select * from customers;
select * from products;
select * from orders;

INSERT INTO orders (customer_id, product_id, quantity, total_price, order_date, send)
VALUES
    (4, 1, 10, 199.99, '2022-03-18 10:00:00', 1),
    (5, 4, 7, 149.99, '2022-04-18 22:00:00', 0),
    (3, 2, 5, 42.99, '2022-01-18 2:00:00', 1);