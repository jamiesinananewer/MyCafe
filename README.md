
## Welcome to MyCafe!

This program is intended for use by the employees of a cafe/restaurant so that they can add/modify/delete menu items, couriers, and orders that have been made by customers, and save any changes that they make. This is done by storing the orders, products and couriers in a MySQL database, extracting this information using python pymysql and creating a user interface that the employees can interact with to make their changes. Once changes are made, they are saved back into the database.

The SQL database has been normalized to allow orders to have multiple products attached to them, as well as having a courier attached to them, from separate tables. When saving the changes to the database, CRUD methodology is used to ensure that the data is saved in the most efficient way, by reading each row in each table and determining if they need to be updated or deleted, or if new rows need to be created.

Please read the following instructions as to how to set up the program and navigate it once you have it running. I hope you enjoy!

**- Jamie S-E, creator**





## Instructions for setting up MyCafe:

1. **Install Python:**
   - Download Python from python.org and follow the installation instructions.

2. **Install Required Python Packages:**
   - Open a terminal or command prompt.
   - Install the necessary Python packages using pip:
     ```sh
     pip install pymysql 
     pip install dotenv
     pip install os
     ```
     *n.b. these commands may be different depending on the operating system you use, make sure you are familiar with what these are.*

3. **Install Docker and MySQL:**
   - Download and install Docker Desktop from docker.com.
   - Ensure Docker is running on your system.
   - Pull the MySQL Docker image:
     ```sh
     docker pull mysql
     ```

4. **Set Up Adminer for Database Management:**
   - Pull the Adminer Docker image:
     ```sh
     docker pull adminer
     ```
   - Start Adminer using Docker:
     ```sh
     docker run -d -p 8080:8080 adminer
     ```
   - Adminer will be accessible at [http://localhost:8080](http://localhost:8080) in your web browser.

5. **Create the Database and Tables:**
   - Copy the contents of the `Cafe_Database.sql` file and execute it in Adminer:
     - Open your web browser and go to [http://localhost:8080](http://localhost:8080).
     - Log in to Adminer with the MySQL credentials (default username: `root`, password: `password`).
     - Click on "SQL Command" in the Adminer interface.
     - Paste the contents of `Cafe_Database.sql` into the SQL command box.
     - Click "Execute" to create the database and tables.

6. **Set Up Python Environment and Install Packages:**
   - Open a terminal or command prompt.
   - Navigate to the directory containing your project files.
   - Create a virtual environment (optional but recommended):
     ```sh
     python -m venv env
     ```
   - Activate the virtual environment:
     - On Windows:
       ```sh
       .\env\Scripts\activate
       ```
     - On macOS/Linux:
       ```sh
       source env/bin/activate
       ```
   - Install required packages:
     ```sh
     pip install pymysql
     pip install python-dotenv
     ```

7. **Populate the Database:**
   - Execute the `db_filler.py` script to populate the database:
     - Open a terminal or command prompt.
     - Navigate to the directory containing your project files.
     - Ensure your virtual environment (if used) is activated:
       - On Windows:
         ```sh
         .\env\Scripts\activate
         ```
       - On macOS/Linux:
         ```sh
         source env/bin/activate
         ```
     - Run the `db_filler.py` script:
       ```sh
       python db_filler.py
       ```

8. **Run the Program:**
   - Execute the `MyCafe.py` main program:
     - Open a terminal or command prompt.
     - Navigate to the directory containing your project files.
     - Ensure your virtual environment (if used) is activated:
       - On Windows:
         ```sh
         .\env\Scripts\activate
         ```
       - On macOS/Linux:
         ```sh
         source env/bin/activate
         ```
     - Run the main program:
       ```sh
       python MyCafe.py
       ```





## Below are instructions detailing each option in the UI:

### Managing Products:

#### View Current Products:
   - Choose option 1 from the main menu to see a list of existing products.

#### Add New Product:
   - Select option 2 and follow the prompts to enter the product name and price. The program will automatically assign an ID.

#### Update Existing Product:
   - To modify a product, select option 3, enter the product ID to update, and provide new details for the name and/or price.

#### Delete Product:
   - Choose option 4, enter the product ID you wish to delete, and confirm the deletion when prompted.

### Managing Couriers:

#### View Current Couriers:
   - Select option 1 in the main menu to display all current couriers.

#### Add New Courier:
   - Choose option 2 and follow the prompts to add a new courier by entering their name and phone number.

#### Update Existing Courier:
   - For updating a courier, select option 3, input the courier ID to modify, and provide new details for the name and/or phone number.

#### Delete Courier:
   - Select option 4, enter the courier ID you wish to delete, and confirm the deletion when prompted.

### Managing Orders:

#### View Current Orders:
   - Select option 1 in the main menu to see a list of all existing orders.

#### View Orders by Status:
   - Choose option 2 to filter orders based on status. Enter the status (e.g., "Preparing", "Ready for Collection") to view orders under that status.

#### View Orders by Courier:
   - Select option 3 to filter orders by a specific courier ID. Enter the courier ID to display orders assigned to that courier.

#### Add New Order:
   - To create a new order, select option 4, and follow the prompts to enter order details, select products, and assign a courier.

#### Update Order Status:
   - Choose option 5 to update the status of an existing order. Enter the order ID and select from available statuses (e.g., "Preparing", "Completed").

#### Update Existing Order:
   - Select option 6 to update existing orders. Enter the order ID to modify and update details such as name, address, items, and courier assignment.

#### Delete Order:
   - Choose option 7, enter the order ID to delete, and confirm the deletion when prompted.

###
