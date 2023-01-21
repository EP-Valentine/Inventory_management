# Shoe Class: takes product information regarding country, code, product, cost and quantity.
class Shoe:

    def __init__(self, country, code, product, cost, quantity):

        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity



    # Function to get cost of product.
    def get_cost(self):
        return self.cost
        
    # Function to get quantity of product.
    def get_quantity(self):
        return self.quantity
        
    # Function to display all product information in a user friendly manner.
    def __str__(self):

        print("┌────────────────────┐                       ") 
        print(f"│ PRODUCT:           │  {self.product}       ")
        print("├────────────────────┼───────────────────────")
        print(f"│ Product Code:      │  {self.code}          ")
        print("├────────────────────┼───────────────────────")
        print(f"│ Product Cost:      │  {self.cost}          ")
        print("├────────────────────┼───────────────────────")
        print(f"│ Product Quantity:  │  {self.quantity}      ")
        print("├────────────────────┼───────────────────────")
        print(f"│ Product Country:   │  {self.country}       ")
        print("└────────────────────┴───────────────────────")

       




# ====== FUNCTIONS ======

# Again(): Function to avoid repetitive code when asking user if they would like to repeat their previous actions.
# Takes 'text' as the question relevant to the task.
def Again(text):

    
    # Insert relevant question and ask user to input 'y' or 'n'.
    Again = input(f"{text} y/n: ")

    # Ensure input is valid.
    if Again != 'y' and Again != 'n':
        print("\nPlease enter 'y' or 'n'.")
        Again = input(f"{text} y/n: ")
    
    return Again



# Menu_Return(): Function to avoid repetitive code when asking user if they wish to return to menu. 
def Menu_Return():
    
    m_return = input("Return to menu? y/n: ")

    # Ensure user inputs correct 'y' or 'n' values.
    if m_return != 'y' and m_return != 'n':
        print("Please type 'y' or 'n'.")
        m_return = input("Return to menu? y/n: ")

    return m_return



# Read_shoes_data(): Function to take product information from inventory.txt and encapsulate each line of information into a Shoe object.
def read_shoes_data():

    # Empty shoe_list to store shoe objects:  Inside function to update each time an item is restocked or added.
    shoe_list = []

    # Empty data list to store shoe data from text file.
    data = []

    try:
        with open("inventory.txt", "r") as f:
            
            # For each line in f, remove '\n' and split by ',' to create product list. 
            # Nest each product list within the data list:  Ensuring to delete first line (data[0]) as to only use only relevant shoe data.
            for line in f:
                line = line.replace("\n", "")
                line = line.split(",")
                data.append(line)
            del data[0]

        # For each nested product in data, create a Shoe object with the information.
        # Country = data[i][0], Code = data[i][1], Product = data[i][2], Cost = data[i][3],  Quantity = data[i][4]
        for i, shoe in enumerate(data):
            shoe_obj = Shoe(data[i][0], data[i][1], data[i][2], float(data[i][3]), int(data[i][4]))
            shoe_list.append(shoe_obj)
        
     
    # If files does not exist except error and inform user. 
    except FileNotFoundError:
            print("Error: This file does not exist.")
    return shoe_list



# capture_shoes(): Function to enable user to add Shoe objects to shoe_list and inventory.txt.
def capture_shoes():
    
    # Get information regarding the country, code, product, cost and quantity of the product being added.
    product = input("Enter the name of the product: ")
    cost = input("Enter the price of the product (numbers only): ")
    code = input("Enter the product code: ")
    quantity = input("Enter the stock quantity of the product: ")
    country = input("Enter the country of the product: ")

    # Append this data as Shoe object to shoe_list
    shoe_list.append(Shoe(country, code, product, cost, quantity))

    # Append the data to inventory.txt to save product in inventory.
    with open("inventory.txt", "a") as f:
        f.write(f"\n{country},{code},{product},{cost},{quantity}")
    
    # Call read_shoes_data() to ensure shoe_list is updated with new information.
    read_shoes_data()

    # Inform user that the task have been complete.
    print("Product added to inventory.")

    

def view_all():
    
    # For each Shoe object in shoe_list, call .__str__() to display product information.
    for obj in shoe_list:
        obj.__str__()
 


# re_stock(): Enables user to see items of low stock and restock those items.
def re_stock():

    while True:
        
        # ===== FIND LOWEST QUANTITY: =====
        # Empty quantity list to store quantity values.
        quant_list = []
        
        # For each Shoe object in shoe_list, append the stock quantity to quant_list.
        for obj in shoe_list:
            quantity = obj.get_quantity()
            quant_list.append(quantity)
        
        # make a sorted copy of quant_list to find lowest stock quantity at index 'sorted_q[0]'.
        sorted_q = sorted(quant_list.copy())
        lowest_Shoe_index = quant_list.index(sorted_q[0])



        # ===== RESTOCKING PROCESS: =====
        # Print requested information to user.
        print(f"\n• The shoe with the lowest stock is {shoe_list[lowest_Shoe_index].product}. There are {shoe_list[lowest_Shoe_index].quantity} pairs left.")
    
        # Ask user if they would like to restock the product.
        restock = input("\n  Would you like to restock this product? y/n: ")

        # Ensure user input is correct.
        if restock != 'y' and restock != 'n':
            print("\n  Please choose 'y' or 'n'.")
            restock = input("\n  Would you like to restock this product? y/n: ")
        


        # If restock = yes, ask the quantity of the item they would like to restock.
        if restock == 'y':
            new_stock = int(input("\nHow many pairs would you like to restock?: "))

            # Add 'new_stock' quantity to the 'quantity' variable of the lowest stocked Shoe object.
            shoe_list[lowest_Shoe_index].quantity = (shoe_list[lowest_Shoe_index].quantity) + new_stock
        
            # Replace previously removed first (descriptor) line in text file for clarity.          
            line = "country,code,product,cost,quantity\n"

            # For each obj in shoe_list, create a string of all relevant data and append to 'line' variable:
            # separate by ',' and add '\n' at end to ensure proper file formatting when written to inventory.txt file.
            for i, obj in enumerate(shoe_list):
                line += f"{shoe_list[i].country},{shoe_list[i].code},{shoe_list[i].product},{shoe_list[i].cost},{shoe_list[i].quantity}\n"

            # Write the updated file data to inventory.txt and inform user the restock has been registered.            
            with open("inventory.txt", "w") as f:
                    f.write(line)
            print ("Restock Complete")

            
        # If restock = no, break to return to menu.
        if restock =='n':
            break
        


        # ===== REPEAT: ====

        # Call Again() with the text 'Perform another restock?' to ask user whether they wish to restock another item.
        again = Again("Perform another restock?")
        
        # If again = 'y':  call read_shoes_data() to update shoe_list and continue to perform another restock.
        if again == "y":
            read_shoes_data()
            continue

        # Otherwise, break to continue to menu.
        else:
            break 
           

# search_shoe(): Enables user to search product in inventory by either name or product code.        
def search_shoe():

    while True:

        # Ask user whether to search by name or by code.
        search = input("\nEnter '1' to search by product name, enter '2' to search by code: ")

        # Ensure user input is valid.
        if search != '1' and search != "2":
            print("Please enter '1' or '2'.")
            search = input("\nEnter '1' to search by product name, enter '2' to search by code: ")
        


        # ===== SEARCH BY NAME =====
        if search == "1":

            # Ask user to input the name of the shoe they are searching for.
            name = input("Enter the name of the product you are looking for: ")
            
            # Empty name list to store name values.
            name_list = []
            
            # For each Shoe object in shoe_list, append the name to name_list.
            for obj in shoe_list:
                name_list.append(obj.product)


            try:
                # Find the index of the Shoe object containing 'cname' in shoe_list (equivalent order to name_list).
                name_Shoe_index = name_list.index(name)
                
                # Display details of the requested shoe by calling .__str__() on the name_Shoe_index.
                shoe_list[name_Shoe_index].__str__()

            # If product searched does not exist, inform user.    
            except ValueError:
                print("This product is not registered in the inventory.")

        
        
        # ===== SEARCH BY CODE =====
        else:

            # Ask user to input the code of the shoe they are searching for.
            code = input("Enter the code of the shoe you are looking for: ")
            
            # Empty code list to store code values.
            code_list = []
            
            # For each Shoe object in shoe_list, append the stock quantity to code_list.
            for obj in shoe_list:
                shoe_code = obj.code
                code_list.append(shoe_code)


            try:
                # Find the index of the Shoe object containing 'code' in shoe_list (equivalent order to code_list).
                code_Shoe_index = code_list.index(code)
                
                # Display details of the requested shoe by calling .__str__() on the code_Shoe_index.
                shoe_list[code_Shoe_index].__str__()

            # If product searched does not exist, inform user.    
            except ValueError:
                print("This product is not registered in the inventory.")
        

        # ===== REPEAT =====

        # Call Again() function to ask user if they wish to search for another item.
        again = Again("Search for another item?")
       
        # If 'y', continue to search another item.
        if again == "y":
            continue

        # Otherwise, break to return to menu.
        else:
            break


# value_per_item(): Displays information regarding total stock value of all items in inventory.
def value_per_item():

    # Calculate total value of ALL stock.
    total = 0
    for obj in shoe_list:
        total += obj.cost*obj.quantity
        
    # Display total value and value title in table head.    
    print( "┌───────────────────┐") 
    print(f"│ TOTAL VALUE:      │   £{total}")
    print( "├───────────────────┴───────────────")
 
    # For each subsequent item, display the item and its total value in separate table sections.
    for obj in shoe_list:
        print(f"│ {obj.product}: £{obj.cost*obj.quantity}")
        print( "├───────────────────────────────────")
        
   
# highest_qty(): Displays the highest stock quantity product to user.
def highest_qty():
    
    # Empty quantity list to store quantity values.
    quant_list = []
    
    # For each Shoe object in shoe_list, append the stock quantity to quant_list.
    for obj in shoe_list:
        quantity = obj.get_quantity()
        quant_list.append(quantity)      

    # Make a descending sorted copy of quant_list to find highest stock quantity at 'sorted_q[0]'.
    sorted_q = sorted(quant_list.copy(),reverse=True)     
    highest_Shoe_index = quant_list.index(sorted_q[0])

    # Display the information regarding the highest quantity product to user.
    print(f"The shoe with the highest stock is {shoe_list[highest_Shoe_index].product}. There are {shoe_list[highest_Shoe_index].quantity} pairs for sale")



# ===== MENU =====

while True: 

    # Renew/update shoe_list data by by calling read_shoes_data().
    shoe_list = read_shoes_data()

    
    # Display menu to user and ask user to input the action they would like to perform.
    print("\nMENU:  Please select one of the following options:")
    print("──────────────────────────────────────────────────")
    print("► a   - Add Product\n► va  - View All \n► r   - Restock \n► s   - Search Product\n► sv  - View Stock Values\n► h   - View Highest Quantity Item \n► e   - Exit")
    print("──────────────────────────────────────────────────")
    choice = input("Selection: ").lower()
    


    if choice == "a":

        while True:

            # Call capture_shoes() to encapsulate user inputted product information into a Shoe object.
            capture_shoes()

            # ===== REPEAT =====

            # Call Again() with the text 'Add another product to inventory?' to ask user if they wish to add another product to inventory.
            again = Again("Add another product to inventory?")
            
            if again == "y":
                continue
            else:
                break
        


    elif choice == "va":
                
        # If user chooses 'va'. call view_all() function to display all product information.
        view_all()

        # Call Menu_Return() to ask user if they wish to return to menu.
        menu_return = Menu_Return()
        if menu_return == "n":
            print("\nClosing inventory. Goodbye!")
            exit()


        
        



    elif choice == "r":
        
        # Call re_stock() to access restocking process.
        re_stock()
        


    elif choice == "s":
        
        # Call search_shoe() to enable user to search for product by name or by product code.
        search_shoe()



    elif choice == "sv":

        # Call value_per_item() to display total monetary values for all products stocked.
        value_per_item()
        

        # Call Menu_Return() to ask user if they wish to return to menu.
        menu_return = Menu_Return()
        if menu_return == "n":
            print("\nClosing inventory. Goodbye!")
            exit()
        


    elif choice == "h":

        # Call highest_qty() to display the product with the highest quantity stock value to the user.
        highest_qty()


        # Call Menu_Return() to ask user if they wish to return to menu.
        menu_return = Menu_Return()
        if menu_return == "n":
            print("\nClosing inventory. Goodbye!")
            exit()


    # If user chooses to exit, display goodbye message and exit program.
    elif choice == "e":
        print("\nClosing inventory. Goodbye!")
        exit()

    # If user inputs an invalid menu option, inform them and return to menu options.
    else:
        print("\nOops! Something went wrong. Please Try again.")  