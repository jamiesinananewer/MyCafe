import pymysql
import os
from dotenv import load_dotenv
from MyCafeFunctions import *

# Load environment variables from .env file
load_dotenv()
host_name = os.environ.get("mysql_host")
database_name = os.environ.get("mysql_db")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")

# Establish database connection using environment variables
connection = pymysql.connect(
    host=host_name,
    database=database_name,
    user=user_name,
    password=user_password,
    cursorclass=pymysql.cursors.DictCursor              # Ensure the cursor returns dictionaries
)

cursor = connection.cursor()

# Retrieve all products from the database
cursor.execute('SELECT * FROM products')
products = cursor.fetchall()

# Retrieve all couriers from the database
cursor.execute('SELECT * FROM couriers')
couriers = cursor.fetchall()

# Retrieve all orders from the database
cursor.execute('SELECT * FROM orders')
ordRows = cursor.fetchall()
orders = []

# Process each order
for order in ordRows:
    order_id = order['order_id']
    order_name = order['order_name']
    order_address = order['order_address']
    order_phone = order['order_phone']
    order_status = order['order_status']

    # Retrieve associated product IDs for the order
    cursor.execute('''
    SELECT p.product_id
    FROM products p
    JOIN order_product_junction opj ON p.product_id = opj.product_id
    WHERE opj.order_id = %s
    ''', (order_id,))
    
    product_ids = [row['product_id'] for row in cursor.fetchall()]

    # Retrieve associated courier IDs for the order
    # cursor.execute('''
    # SELECT c.courier_id
    # FROM couriers c
    # JOIN order_courier_junction ocj ON c.courier_id = ocj.courier_id
    # WHERE ocj.courier_id = %s
    # ''', (order_id,))

    # courier_ids = [row['courier_id'] for row in cursor.fetchall()]

    cursor.execute('''
    SELECT c.courier_id
    FROM couriers c
    JOIN order_courier_junction ocj ON c.courier_id = ocj.courier_id
    WHERE ocj.order_id = %s
    ''', (order_id,))

    courier_ids = [row['courier_id'] for row in cursor.fetchall()]
    
    # Create a dictionary for the order and append to the orders list
    order_dict = {
        'order_id': order_id,
        'order_name': order_name,
        'order_address': order_address,
        'order_phone': order_phone,
        'order_status': order_status,
        'order_items': product_ids,
        'order_courier': courier_ids
    }
    orders.append(order_dict)


while True:  # Use while loop to return to beginning once an operation is performed
    
    ClearScreen()       #clears the screen before displating the menu
    
    startScreen = input('''MAIN MENU: Please select an option:  
                               
0 = Save & Exit
1 = View product options
2 = View courier options
3 = View order options
                        
Option: ''')  # Create main menu input

    if startScreen == '0':  # Create exit application option
        confirmSave = input('Save changes and exit (y/n)? ')

        if confirmSave == 'y':
            SaveChanges(products, couriers, orders, cursor, connection)
            print('Exiting program..')
            exit()
        elif confirmSave == 'n':
            pass
        else:
            pass

    elif startScreen == '1':  # Create product menu as option 1
        
        while True:
            
            prodOption = input('''PRODUCTS MENU
0 = Return to main menu
1 = View current products
2 = Add new product
3 = Update existing product
4 = Delete product
Please select an option: ''')
            
            if prodOption == '0':
                break
                
            elif prodOption == '1':
                ClearScreen()
                print('VIEW CURRENT PRODUCTS\n')
                print(f'Current products are as follows:')
                PrintProducts(products)
            
            elif prodOption == '2':
                ClearScreen()
                print('ADD NEW PRODUCT\n')
                AddProduct(products)

            elif prodOption == '3':
                ClearScreen()
                print('UPDATE EXISTING PRODUCT\n')
                UpdateProduct(products)

            elif prodOption == '4':
                ClearScreen()
                print('DELETE EXISTING PRODUCT\n')
                DeleteProduct(products, orders)
            
            else:
                print('Invalid input, please try again')

    elif startScreen == '2':  # Create courier menu as option 2
        
        while True:
            
            courOption = input('''COURIERS MENU
0 = Return to main menu
1 = View current couriers
2 = Add new courier
3 = Update existing courier
4 = Delete courier
Please select an option: ''')
            
            if courOption == '0':
                ClearScreen()
                break
                
            elif courOption == '1':
                ClearScreen()
                print('VIEW CURRENT COURIERS\n')
                print(f'Current couriers are as follows:')
                PrintCouriers(couriers)
            
            elif courOption == '2':
                ClearScreen()
                print('ADD NEW COURIER\n')
                AddCourier(couriers)

            elif courOption == '3':
                ClearScreen()
                print('UPDATE EXISTING COURIER\n')
                UpdateCourier(couriers)

            elif courOption == '4':
                ClearScreen()
                print('DELETE EXISTING COURIER\n')
                DeleteCourier(couriers, orders)
            
            else:
                print('Invalid input, please try again')

    elif startScreen == '3':  # Create order menu as option 3
        
        while True:
            
            ordOption = input('''ORDERS MENU\nPlease select an option:\n
0 = Return to main menu
1 = View current orders
2 = View orders by status                              
3 = View orders by courier
4 = Add new order
5 = Update existing order status
6 = Update existing order
7 = Delete existing order

Option: ''')

            if ordOption == '0':
                ClearScreen()
                break

            elif ordOption == '1':
                ClearScreen()
                print('VIEW CURRENT ORDERS\n')
                print('Current orders are as follows:\n')
                PrintOrders(orders)
            
            elif ordOption == '2':
                ClearScreen()
                print('VIEW ORDERS BY STATUS\n')
                DisplayOrdersByStatus(orders)
            
            elif ordOption == '3':
                ClearScreen()
                print('VIEW ORDERS BY COURIER\n')
                DisplayOrdersByCourier(orders, couriers)

            elif ordOption == '4':
                ClearScreen()
                print('ADD NEW ORDER:\n')
                AddOrder(orders, products, couriers)
            
            elif ordOption == '5':
                ClearScreen()
                print('UPDATE ORDER STATUS\n')
                UpdateOrderStatus(orders)
            
            elif ordOption == '6':
                ClearScreen()
                print('UPDATE EXISTING ORDER\n')
                UpdateOrder(orders, products, couriers)
            
            elif ordOption == '7':
                ClearScreen()
                print('DELETE EXISTING ORDER\n')
                DeleteOrder(orders)
            
            else:
                print('Invalid input, please try again')

    else:
        print('Invalid input, please try again')
