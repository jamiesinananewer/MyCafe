import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

host_name = os.environ.get("mysql_host")
database_name = os.environ.get("mysql_db")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")

with pymysql.connect(       # Establish connection to MySQL database
    host=host_name,
    database=database_name,
    user=user_name,
    password=user_password
) as connection:
    
    cursor = connection.cursor()

    # Fill products table
    productFill = """
        INSERT INTO products (product_name, product_price)
        VALUES (%s, %s)
    """
    productData = [
        ('BLT', 4.5),
        ('Ploughman', 4.2),
        ('Coke', 1.2),
        ('Fanta', 1.2)
    ]
    cursor.executemany(productFill, productData)

    # Fill couriers table
    courierFill = """
        INSERT INTO couriers (courier_name, courier_phone)
        VALUES (%s, %s)
    """
    courierData = [
        ('Pete', '07894561256'),
        ('Bas', '07934514861'),
        ('Derek', '07892393826')
    ]
    cursor.executemany(courierFill, courierData)

    # Fill orders table
    orderFill = """
        INSERT INTO orders (order_name, order_address, order_phone, order_status)
        VALUES (%s, %s, %s, %s)
    """
    orderData = [
        ('John Doe', '123 Elm Street', '07712345678', 'Preparing'),
        ('Jane Smith', '456 Oak Avenue', '07787654321', 'Ready for Collection')
    ]
    cursor.executemany(orderFill, orderData)

    # Fill order-products junction table
    orderProductFill = """
        INSERT INTO order_product_junction (order_id, product_id)
        VALUES (%s, %s)
    """
    orderProductData = [
        (1, 1),  # Order 1 with product BLT
        (1, 3),  # Order 1 with product Coke
        (2, 2),  # Order 2 with product Ploughman
        (2, 4)   # Order 2 with product Fanta
    ]
    cursor.executemany(orderProductFill, orderProductData)

    # Fill order-courier junction table
    orderCourierFill = """
        INSERT INTO order_courier_junction (order_id, courier_id)
        VALUES (%s, %s)
    """
    orderCourierData = [
        (1, 1),  # Order 1 assigned to courier Pete
        (2, 2)   # Order 2 assigned to courier Bas
    ]
    cursor.executemany(orderCourierFill, orderCourierData)

    # Commit changes to the database
    connection.commit()

    # Retrieve and print products
    cursor.execute('SELECT product_name, product_price FROM products')
    productList = cursor.fetchall()
    print('Products:')
    print(productList)

    # Retrieve and print couriers
    cursor.execute('SELECT courier_name, courier_phone FROM couriers')
    courierList = cursor.fetchall()
    print('Couriers:')
    print(courierList)

    # Retrieve and print orders
    cursor.execute('SELECT order_name, order_address, order_phone, order_status FROM orders')
    orderList = cursor.fetchall()
    print('Orders:')
    print(orderList)

    # Retrieve and print order-products junction table
    cursor.execute('SELECT order_id, product_id FROM order_product_junction')
    orderProductList = cursor.fetchall()
    print('Order-Products:')
    print(orderProductList)

    # Retrieve and print order-couriers junction table
    cursor.execute('SELECT order_id, courier_id FROM order_courier_junction')
    orderCourierList = cursor.fetchall()
    print('Order-Couriers:')
    print(orderCourierList)

    cursor.close()
