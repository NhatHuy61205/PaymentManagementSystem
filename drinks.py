import mysql.connector as conn1
from tabulate import tabulate
import string

# Them nuoc
def Add_drink():
    mycon1 = conn1.connect(host="127.0.0.1", user="huyy", password="Huybui1206",database="cafe_payment_system")
    cursor = mycon1.cursor(buffered=True)
    #so luong nuoc can them
    add_drinks = int(input("Enter number of drinks you want to add: "))
    for drink in range(add_drinks):
        try:
            drink_id = input("  Enter the drink ID: ").lower()
            drink_name = input("    Enter the drink name: ").lower()
            ingredient = input("    Enter the ingredient: ").lower()
            volume = input("    Enter the volume: ").lower()
            temperature = input("  Enter the temperature: ").lower()
            price = input(" Enter the price: ").lower()
            additives = input("     Enter the additives (if any): ").lower()
            preparation = input("   Enter the preparation (if any): ").lower()
            description = input("   Enter the description: ").lower()
    # truy van sql
            cursor.execute(
                f"INSERT INTO drinks (ID, name, ingredient, volume, temperature, price, additives, "
                f" preparation, description) VALUES('{drink_id}', '{drink_name}', '{ingredient}', '{volume}', "
                f" '{temperature}', '{price}', '{additives}', '{preparation}', '{description}')"
    )
    #xac nhan thay doi
            mycon1.commit()
            print("Successfully add the drink.")
        except:
            print("WRONG DATA GIVEN.")
            Add_drink()
    mycon1.close()
    return 

# View All
def View_all():
    mycon1 = conn1.connect(host="127.0.0.1", user="huyy", password="Huybui1206",database="cafe_payment_system")
    cursor = mycon1.cursor(buffered=True)
    cursor.execute("SELECT ID, name, price, volume, temperature FROM drinks")
    drinks = cursor.fetchall()
    
    if not drinks:
        print("No drinks found in the database.")
        return
    hearder = ["ID", "Name", "Price", "Volume", "Temperature"]
    table = tabulate(drinks, hearder=hearder, tablefmt="fancy_grid",stralign='center', colalign=("center", "center", "center"))
    
    print(table)
    mycon1.close()
    return
    
# View Detail
def View_details():
    mycon1 = conn1.connect(host="127.0.0.1", user="huyy", password="Huybui1206", database="cafe_payment_system")
    cursor = mycon1.cursor(buffered=True)
    drink_id = input("Enter the drink ID you want to view details for: ").lower()
    cursor.execute(f"SELECT * FROM drinks WHERE ID = '{drink_id}'")
    drink = cursor.fetchone()
    if not drink:
        print(f"No drink found with ID: {drink_id}")
        return
    
    # In thông tin chi tiết theo dạng dọc
    print(f"Details of drink ID {drink_id}:")
    print(f"ID        : {drink[0]}")
    print(f"Name      : {drink[1]}")
    print(f"Ingredient: {drink[2]}")
    print(f"Volume    : {drink[3]}")
    print(f"Temperature: {drink[4]}")
    print(f"Price     : {drink[5]}")
    print(f"Additives : {drink[6]}")
    print(f"Preparation: {drink[7]}")
    print(f"Description: {drink[8]}")
    
    mycon1.close()
    return
    
# Cap Nhat Drink
def Update_drink():
    mycon1 = conn1.connect(host="127.0.0.1", user="huyy", password="Huybui1206",database="cafe_payment_system")
    cursor = mycon1.cursor(buffered=True)
    drink_id = input("Enter the drink ID you want to update for: ").lower()
    cursor.execute(f"SELECT * FROM drinks WHERE ID = '{drink_id}'")
    drink =cursor.fetchone()
    if not drink:
        print(f"No drink found with ID: {drink_id}")
        mycon1.close()
        return
# In chi tiet 
    print(f"Details of drink ID {drink_id}:")
    print(f"Ingredient  : {drink[2]}")
    print(f"Volume      : {drink[3]}")
    print(f"Temperature : {drink[4]}")
    print(f"Price       : {drink[5]}")
    print(f"Additives   : {drink[6]}")
    print(f"Preparation : {drink[7]}")
    print(f"Description : {drink[8]}")
    
    while True:
        clear_screen()
        print("\nWhich detail would you like to update?")
        print("1. Ingredient")
        print("2. Volume")
        print("3. Temperature")
        print("4. Price")
        print("5. Additives")
        print("6. Preparation")
        print("7. Description")
        ch = input("Enter the number of the detail you want to update: ")
        if ch =='1':
            new_value =  input("Enter the new ingredient: ")
            cursor.execute(f"UPDATE drinks SET ingredient = '{new_value}' WHERE ID = '{drink_id}'")
        elif ch=='2':
            new_value = input("Enter the new volume: ")
            cursor.execute(f"UPDATE drinks SET volume = '{new_value}' WHERE ID = '{drink_id}'")
        elif ch=='3':
            new_value = input("Enter the new temperature: ")
            cursor.execute(f"UPDATE drinks SET temperature = '{new_value}' WHERE ID = '{drink_id}'")
        elif ch=='4':
            new_value = input("Enter the new price: ")
            cursor.execute(f"UPDATE drinks SET price = '{new_value}' WHERE ID = '{drink_id}'")
        elif ch=='5':
            new_value = input("Enter the new additives: ")
            cursor.execute(f"UPDATE drinks SET additives = '{new_value}' WHERE ID = '{drink_id}'")
        elif ch=='6':
            new_value = input("Enter the new preparation method: ")
            cursor.execute(f"UPDATE drinks SET preparation = '{new_value}' WHERE ID = '{drink_id}'")
        elif ch=='7':
            new_value = input("Enter the new description: ")
            cursor.execute(f"UPDATE drinks SET description = '{new_value}' WHERE ID = '{drink_id}'")
        else:
            print("Invalid choice! Please try again.")
            continue
        
        mycon1.commit()
        print("Successfully updated the drink detail.")
        continue_update = input("Do you want to update another detail? (yes/no): ").lower()
        if continue_update != 'yes':
            break
        
    mycon1.close()
    return 
        
# Xoa Drink
def Delete_drink():
    mycon1 = conn1.connect(host="127.0.0.1", user="huyy", password="Huybui1206", database="cafe_payment_system")
    cursor = mycon1.cursor(buffered=True)
    drink_id = input("Enter the drink ID you want to view details for: ").lower()
    cursor.execute(f"SELECT * FROM drinks WHERE ID = '{drink_id}'")
    drink = cursor.fetchone()
    if not drink:
        print(f"No drink found with ID: {drink_id}")
        return
    
    cursor.execute(f"DELETE FROM drinks WHERE ID = '{drink_id}'")
    mycon1.commit()
    print(f"Drink with ID {drink_id} has been successfully deleted.")
    mycon1.close()
    return


def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
        
    
    
    
    
    
    