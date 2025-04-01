import os

#Helper functions


def GetNextID(items, name =''):                     #generates auto incremented id for new products/couriers/orders,
                                                    #so they can be created and then used in the program before saving to the database
    max_id = max((item[f'{name}_id'] for item in items if item[f'{name}_id'] is not None), default=0)
    
    return max_id + 1

def PrintList(list):                #Prints items in a list with their indexes
    for i, item in enumerate(list):
        print(f'{i} = {item}')

def ClearScreen(): #Clears the terminal screen based on the operating system.
    # Clear screen command for Windows and Unix-like systems
    os.system('cls' if os.name == 'nt' else 'clear')



#Product Functions


def AddProduct(products):        #creates new product with auto-incremented ID
    name = input("Enter product name: ")
    price = input('Enter price: ')
    new_id = GetNextID(products, name ='product')
    products.append({'product_id': new_id, 'product_name': name, 'product_price' : price})


def PrintDict(dictionary, name=''):
    # Loop through the dictionary items
    for j, (key, value) in enumerate(dictionary.items()):
        # If not the last item
        if j < len(dictionary) - 1:
            if key.lower() == f'{name}_id':  # Skip the ID field
                pass
            elif key.lower() == f'{name}_price':  # Format price fields
                print(f'£{value}', end=', ')
            else:
                print(f'{value}', end=', ')  # Print other fields
        else:  # If the last item
            if key.lower() == f'{name}_id':  # Skip the ID field
                pass
            elif key.lower() == f'{name}_price':  # Format price fields
                print(f'£{value}', end='')
            else:
                print(f'{value}', end='')  # Print other fields
    print()  # New line at the end


def PrintProducts(products):
    # Loop through the products and print each
    for dictionary in products:
        print(f"{dictionary['product_id']}: ", end='')  # Print product ID
        PrintDict(dictionary, name='product')  # Print the rest of the product details


def UpdateProduct(products):
    PrintProducts(products)  # Print the list of products
    product_id = input("Enter product ID to UPDATE: ")  # Get the product ID to update
    for product in products:
        if product['product_id'] == int(product_id):
            print('Update product details (Enter to skip)')

            # Update product name if provided
            product_name = input('Update product name: ')
            if product_name != '':
                product['product_name'] = product_name

            # Update product price if provided
            product_price = input('Update product price: ')
            if product_price != '':
                product['product_price'] = product_price
            return  # Exit after updating

    print('Product not found, please try again')  # Message if product ID is not found


def DeleteProduct(products, orders):
    PrintProducts(products)  # Print the list of products
    product_id = input("Enter product ID to DELETE: ")  # Get the product ID to delete
    
    for product in products:
        if product['product_id'] == int(product_id):
            confirm = input(f"Are you sure you want to DELETE {product['product_name']} (y/n)? ")
            if confirm.lower() == 'y':  # Confirm deletion
                # Remove product from the products list
                products.remove(product)
                
                # Remove references to this product in all orders
                for order in orders:
                    if int(product_id) in order['order_items']:
                        order['order_items'].remove(int(product_id))
                
                print('Product deleted, product list is now:')
                PrintProducts(products)  # Print the updated list of products
                print()
            else:
                print('DELETE cancelled, returning to product menu')
                print()
            break
    else:
        print("Product ID not found.")



# Courier Functions


def AddCourier(couriers):  # Creates new courier with auto-incremented ID
    name = input("Enter courier name: ")
    phone = input('Enter phone: ')
    new_id = GetNextID(couriers, name='courier')  # Get the next ID
    couriers.append({'courier_id': new_id, 'courier_name': name, 'courier_phone': phone})  # Add the new courier


def PrintCouriers(couriers):
    # Loop through the couriers and print each
    for dictionary in couriers:
        print(f"{dictionary['courier_id']}: ", end='')  # Print courier ID
        PrintDict(dictionary, name='courier')  # Print the rest of the courier details


def UpdateCourier(couriers):
    PrintCouriers(couriers)  # Print the list of couriers
    courier_id = input("Enter courier ID to UPDATE: ")  # Get the courier ID to update
    for courier in couriers:
        if courier['courier_id'] == int(courier_id):
            print('Update courier details (Enter to skip)')

            # Update courier name if provided
            courier_name = input('Update courier name: ')
            if courier_name != '':
                courier['courier_name'] = courier_name

            # Update courier phone if provided
            courier_phone = input('Update courier phone: ')
            if courier_phone != '':
                courier['courier_phone'] = courier_phone
            return  # Exit after updating


def DeleteCourier(couriers, orders):
    PrintCouriers(couriers)  # Print the list of couriers
    courier_id = input("Enter courier ID to DELETE: ")  # Get the courier ID to delete
    
    courier_found = False
    for courier in couriers:
        if courier['courier_id'] == int(courier_id):
            confirm = input(f"Are you sure you want to DELETE {courier['courier_name']} (y/n)? ")
            if confirm.lower() == 'y':  # Confirm deletion
                couriers.remove(courier)  # Remove the courier
                courier_found = True
                
                print('Courier deleted, courier list is now:')
                PrintCouriers(couriers)  # Print the updated list of couriers
                print()
                
                # Remove references to this courier in all orders and reassign new courier_id
                for order in orders:
                    if order['order_courier'][0] == int(courier_id):
                        PrintCouriers(couriers)
                        new_courier_id = input(f"Order {order['order_id']} was assigned to deleted courier {courier_id}. Please enter a new courier ID: ")
                        while not any(c['courier_id'] == int(new_courier_id) for c in couriers):
                            print("Invalid courier ID. Please choose a valid courier ID from the list above.")
                            new_courier_id = input(f"Please enter a new courier ID for order {order['order_id']}: ")
                        order['order_courier'] = [int(new_courier_id)]
                
                break
            else:
                print('DELETE cancelled, returning to courier menu')
                print()
                return
    
    if not courier_found:
        print("Courier ID not found.")

# Order Functions

def PrintSingleOrder(order):
    # Loop through the order items
    for j, (key, value) in enumerate(order.items()):
        if j < len(order) - 1:  # If not the last item
            if key.lower() == 'order_id':  # Skip the ID field
                pass
            elif key.lower() == 'order_items':  # Format order items
                print(f'Items : {value}', end=', ')
            elif key.lower() == 'order_courier':  # Format courier field
                print(f'Courier: {value}', end=', ')
            else:
                print(f'{value}', end=', ')  # Print other fields
        else:  # If the last item
            if key.lower() == 'order_id':  # Skip the ID field
                pass
            elif key.lower() == 'order_items':  # Format order items
                print(f'Items: {value}', end='')
            elif key.lower() == 'order_courier':  # Format courier field
                print(f'Courier: {value}', end='')
            else:
                print(f'{value}', end='')  # Print other fields
    print()  # New line at the end

def PrintOrders(orders):
    # Loop through the orders and print each
    for order in orders:
        print(f"Order {order['order_id']}:")
        PrintSingleOrder(order)
        print()

def AddOrder(orders, products, couriers):
    order_name = input("Enter order name: ")
    order_address = input("Enter order address: ")
    order_phone = input("Enter order phone: ")
    order_status = 'Preparing'

    PrintProducts(products)  # Print available products
    product_ids = []
    while True:
        add_product = input('Add item ID to order (press f when finished): ')
        if any(str(product['product_id']) == add_product for product in products):
            product_ids.append(int(add_product))  # Add product to order
        elif add_product.lower() == 'f':
            break  # Exit the loop
        else:
            print('Invalid entry, please try again')

    PrintCouriers(couriers)  # Print available couriers

    while True:
        add_courier = input('Enter courier ID: ')
        if any(str(courier['courier_id']) == add_courier for courier in couriers):
            order_courier = int(add_courier)  # Assign courier to order
            break  # Exit the loop
        else:
            print("Invalid courier ID. Please try again.")

    new_order = {
        'order_id': GetNextID(orders, name='order'),
        'order_name': order_name,
        'order_address': order_address,
        'order_phone': order_phone,
        'order_status': order_status,
        'order_items': product_ids,
        'order_courier': order_courier if isinstance(order_courier, list) else [order_courier]     #turns courier into a list for displaying purposes
    }
    orders.append(new_order)  # Add the new order to the list

    print('New order added:')
    PrintSingleOrder(new_order)

def PrintOrderStatuses(orders):
    # Loop through the orders and print their statuses
    for order in orders:
        print(f"Order {order['order_id']}: Status: {order['order_status']}")

def UpdateOrderStatus(orders):
    statuses = ['Preparing', 'Ready for Collection', 'Out for Delivery', 'Completed']
    PrintOrderStatuses(orders)  # Print the current statuses
    print()

    while True:  # Loop until a valid order ID is entered
        choose_status_update = input('Choose an order to update: ')

        for order in orders:
            if str(order['order_id']) == choose_status_update:
                PrintList(statuses)  # Print available statuses

                while True:  # Loop until a valid status index is entered
                    update_status = input('Choose status index to update to: ')

                    if update_status.isdigit() and 0 <= int(update_status) < len(statuses):
                        order['order_status'] = statuses[int(update_status)]
                        print(f"Order {order['order_id']} new status: {order['order_status']}")
                        return  # Exit the function after updating status
                    else:
                        print("Invalid status index. Please try again.")

        print("Invalid order ID. Please try again.")  # If the order ID was not found

def UpdateOrder(orders, products, couriers):
    PrintOrders(orders)  # Print the list of orders
    print()
    choose_order_update = input('Choose order to update: ')

    for order in orders:
        if str(order['order_id']) == choose_order_update:
            print(f'Update Order {order['order_id']} details (leave blank & press Enter to skip)\n')

            # Update order name if provided
            update_name = input('Update order name: ')
            if update_name != '':
                order['order_name'] = update_name

            # Update order address if provided
            update_address = input('Update order address: ')
            if update_address != '':
                order['order_address'] = update_address

            # Update order phone if provided
            update_phone = input('Update order phone: ')
            if update_phone != '':
                order['order_phone'] = update_phone

            updating_items = True
            while updating_items:
                update_items = input('Update Items (y/n)? ')
                print()

                if update_items.lower() == 'y':
                    PrintProducts(products)  # Print available products
                    order['order_items'] = []  # Reset the items list
                    while True:
                        add_product = input('Add item ID to order (press f when finished): ')

                        if add_product.lower() == 'f':
                            updating_items = False
                            break  # Exit the inner loop

                        if any(str(product['product_id']) == add_product for product in products):
                            order['order_items'].append(int(add_product))  # Add product to order
                        else:
                            print('Invalid product ID, please try again.')

                elif update_items.lower() == 'n':
                    updating_items = False  # Exit the outer loop

                else:
                    print('Invalid entry, please try again.')

            PrintCouriers(couriers)  # Print available couriers
            while True:
                update_courier = input('Update Courier ID (Enter to skip): ')
                if update_courier != '':
                    if any(str(courier['courier_id']) == update_courier for courier in couriers):
                        order['order_courier'] = update_courier if isinstance(update_courier, list) else [update_courier]
                        break  # Exit the loop
                    else:
                        print('Invalid courier ID. Please try again.')
                else:
                    break
            print()
            print('Updated order:')
            PrintSingleOrder(order)
        else:
            print('Invalid entry, please try again')

def DeleteOrder(orders):
    while True:
        PrintOrders(orders)  # Print the list of orders
        order_id = input("Enter order ID to DELETE: ")

        if any(str(order['order_id']) == order_id for order in orders):
            while True:
                confirm = input(f"Are you sure you want to DELETE order {order_id} (y/n)? ")
                if confirm.lower() == 'y':  # Confirm deletion
                    for order in orders:
                        if str(order['order_id']) == order_id:
                            orders.remove(order)  # Remove the order
                            print('Order deleted, order list is now:')
                            PrintOrders(orders)  # Print the updated list of orders
                            return
                elif confirm.lower() == 'n':
                    print('DELETE cancelled, returning to order menu')
                    return
                else:
                    print('Invalid input. Please enter "y" for yes or "n" for no.')
        else:
            print('Invalid order ID, please try again.')

def DisplayOrdersByStatus(orders):
    # Print available statuses for user to choose
    statuses = ['Preparing', 'Ready for Collection', 'Out for Delivery', 'Completed']
    
    while True:
        # Print statuses with indexes
        PrintList(statuses)
        
        # Ask user to choose a status to filter orders by index
        statusChoiceIndex = input('Choose a status number to filter orders by: ')
        
        if not statusChoiceIndex.isdigit():
            print('Invalid input, please enter a correct status number.')
            continue
        
        statusChoiceIndex = int(statusChoiceIndex)
        
        if statusChoiceIndex < 0 or statusChoiceIndex >= len(statuses):
            print('Invalid status number. Please try again.')
            continue
        
        # Get the status based on the chosen index
        statusChoice = statuses[statusChoiceIndex]
        break  # Exit loop once a valid index is entered

    # Filter orders based on chosen status
    filteredOrders = [order for order in orders if order['order_status'] == statusChoice]

    if filteredOrders:
        # Print orders with the chosen status
        print(f'Orders with status "{statusChoice}":\n')
        for order in filteredOrders:
            print(f'{order['order_id'] }: ', end = '')
            PrintSingleOrder(order)
        print()
    else:
        # Inform user if no orders match the chosen status
        print(f'No orders found with status "{statusChoice}"')
        print()

def DisplayOrdersByCourier(orders, couriers):
    # Print list of couriers for user reference
    PrintCouriers(couriers)
    print()

    while True:
        # Ask user to enter a courier ID to filter orders
        courierId = input('Enter courier ID to filter orders: ')

        if not courierId.isdigit():
            print('Invalid input. Please enter a valid courier ID.')
            continue

        courierId = int(courierId)

        # Check if the courier ID exists in the couriers list
        if courierId not in [courier['courier_id'] for courier in couriers]:
            print('Invalid courier ID. Please try again.')
            continue
        
        break  # Exit loop once a valid courier ID is entered

    # Filter orders based on chosen courier ID
    filteredOrders = [order for order in orders if courierId in order['order_courier']]

    if filteredOrders:
        # Print orders assigned to the chosen courier ID
        print(f'Orders assigned to courier ID {courierId}:\n')
        for order in filteredOrders:
            print(f"{order['order_id']}: ", end='')
            PrintSingleOrder(order)
        print()
    else:
        # Inform user if no orders are assigned to the chosen courier ID
        print(f'No orders found assigned to courier ID {courierId}')
        print()


# SQL Functions

def SaveChanges(products, couriers, orders, cursor, connection):
    # Read current state from the database
    cursor.execute('SELECT * FROM products')
    dbProducts = cursor.fetchall()

    cursor.execute('SELECT * FROM couriers')
    dbCouriers = cursor.fetchall()

    cursor.execute('SELECT * FROM orders')
    dbOrders = cursor.fetchall()

    # Convert database records to dictionaries for easy comparison
    dbProducts = {prod['product_id']: prod for prod in dbProducts}
    dbCouriers = {cour['courier_id']: cour for cour in dbCouriers}
    dbOrders = {ord['order_id']: ord for ord in dbOrders}

    # Process Products
    for product in products:
        prodID = product['product_id']
        if prodID not in dbProducts:
            # Create new product if it doesn't exist in the database
            cursor.execute('INSERT INTO products (product_id, product_name, product_price) VALUES (%s, %s, %s)',
                           (product['product_id'], product['product_name'], product['product_price']))
        else:
            # Update existing product if any details have changed
            if (dbProducts[prodID]['product_name'] != product['product_name'] or 
                dbProducts[prodID]['product_price'] != product['product_price']):
                cursor.execute('UPDATE products SET product_name=%s, product_price=%s WHERE product_id=%s',
                               (product['product_name'], product['product_price'], product['product_id']))
    
    # Delete products not in memory (i.e., they have been removed)
    memoryProductIds = {prod['product_id'] for prod in products}
    for prodID in dbProducts.keys():
        if prodID not in memoryProductIds:
            # Ensure no orders reference this product before deleting
            cursor.execute('DELETE FROM order_product_junction WHERE product_id=%s', (prodID,))
            cursor.execute('DELETE FROM products WHERE product_id=%s', (prodID,))

    # Process Couriers
    for courier in couriers:
        courID = courier['courier_id']
        if courID not in dbCouriers:
            # Create new courier if it doesn't exist in the database
            cursor.execute('INSERT INTO couriers (courier_id, courier_name, courier_phone) VALUES (%s, %s, %s)',
                           (courier['courier_id'], courier['courier_name'], courier['courier_phone']))
        else:
            # Update existing courier if any details have changed
            if (dbCouriers[courID]['courier_name'] != courier['courier_name'] or 
                dbCouriers[courID]['courier_phone'] != courier['courier_phone']):
                cursor.execute('UPDATE couriers SET courier_name=%s, courier_phone=%s WHERE courier_id=%s',
                               (courier['courier_name'], courier['courier_phone'], courier['courier_id']))
    
    # Delete couriers not in memory (i.e., they have been removed)
    memoryCourierIds = {cour['courier_id'] for cour in couriers}
    for courID in dbCouriers.keys():
        if courID not in memoryCourierIds:
            # Ensure no orders reference this courier before deleting
            cursor.execute('DELETE FROM order_courier_junction WHERE courier_id=%s', (courID,))
            cursor.execute('DELETE FROM couriers WHERE courier_id=%s', (courID,))

    # Process Orders
    for order in orders:
        ordID = order['order_id']
        if ordID not in dbOrders:
            # Create new order if it doesn't exist in the database
            cursor.execute('INSERT INTO orders (order_id, order_name, order_address, order_phone, order_status) VALUES (%s, %s, %s, %s, %s)',
                           (order['order_id'], order['order_name'], order['order_address'], order['order_phone'], order['order_status']))
            
            # Insert order-product junctions
            for productId in order['order_items']:
                cursor.execute('INSERT INTO order_product_junction (order_id, product_id) VALUES (%s, %s)', (ordID, productId))
            
            # Insert order-courier junctions
            cursor.execute('INSERT INTO order_courier_junction (order_id, courier_id) VALUES (%s, %s)', (ordID, order['order_courier']))

        else:
            # Update existing order if any details have changed
            if (dbOrders[ordID]['order_name'] != order['order_name'] or 
                dbOrders[ordID]['order_address'] != order['order_address'] or 
                dbOrders[ordID]['order_phone'] != order['order_phone'] or 
                dbOrders[ordID]['order_status'] != order['order_status']):
                cursor.execute('UPDATE orders SET order_name=%s, order_address=%s, order_phone=%s, order_status=%s WHERE order_id=%s',
                               (order['order_name'], order['order_address'], order['order_phone'], order['order_status'], order['order_id']))
            
            # Update order-product junctions (clear and re-insert)
            cursor.execute('DELETE FROM order_product_junction WHERE order_id=%s', (ordID,))
            for productId in order['order_items']:
                cursor.execute('INSERT INTO order_product_junction (order_id, product_id) VALUES (%s, %s)', (ordID, productId))
            
            # Update order-courier junctions (clear and re-insert)
            cursor.execute('DELETE FROM order_courier_junction WHERE order_id=%s', (ordID,))
            cursor.execute('INSERT INTO order_courier_junction (order_id, courier_id) VALUES (%s, %s)', (ordID, order['order_courier']))

    # Delete orders not in memory (i.e., they have been removed)
    memoryOrderIds = {ord['order_id'] for ord in orders}
    for ordID in dbOrders.keys():
        if ordID not in memoryOrderIds:
            # Delete order-product junctions
            cursor.execute('DELETE FROM order_product_junction WHERE order_id=%s', (ordID,))
            # Delete order-courier junctions
            cursor.execute('DELETE FROM order_courier_junction WHERE order_id=%s', (ordID,))
            # Delete the order itself
            cursor.execute('DELETE FROM orders WHERE order_id=%s', (ordID,))

    # Commit all changes to the database
    connection.commit()

    print("Changes saved to the database.")

