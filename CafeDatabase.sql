-- Drop the my_cafe database if it exists
DROP DATABASE IF EXISTS my_cafe;

-- Create the my_cafe database
CREATE DATABASE my_cafe;

-- Use the my_cafe database
USE my_cafe;

-- Drop tables if they exist (in case you want to recreate them)
DROP TABLE IF EXISTS order_product_junction;
DROP TABLE IF EXISTS order_courier_junction;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS couriers;

-- Create the products table
CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(255) NOT NULL,
    product_price DECIMAL(10, 2) NOT NULL
);

-- Create the couriers table
CREATE TABLE couriers (
    courier_id INT PRIMARY KEY AUTO_INCREMENT,
    courier_name VARCHAR(255) NOT NULL,
    courier_phone VARCHAR(20) NOT NULL
);

-- Create the orders table
CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    order_name VARCHAR(255) NOT NULL,
    order_address VARCHAR(255) NOT NULL,
    order_phone VARCHAR(20) NOT NULL,
    order_status VARCHAR(50) NOT NULL
);

-- Create the order_product_junction table
CREATE TABLE order_product_junction (
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    PRIMARY KEY (order_id, product_id)
);

-- Create the order_courier_junction table
CREATE TABLE order_courier_junction (
    order_id INT NOT NULL,
    courier_id INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (courier_id) REFERENCES couriers(courier_id) ON DELETE CASCADE,
    PRIMARY KEY (order_id, courier_id)
);