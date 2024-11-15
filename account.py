import mysql.connector as conn2
from time import sleep
from tabulate import tabulate

# Dang ky
def Sign_up():
    mycon2 = conn2.connect(host="127.0.0.1", user="huyy", password="Huybui1206",database="cafe_payment_system")
    cursor = mycon2.cursor(buffered=True)
    while True:
        clear_screen()
        print("=== SIGN UP USER ===")
        input_username = input("    Create Username (Login ID): ").lower()
        cursor.execute(f"SELECT * FROM account WHERE username = '{input_username}'")
        data = cursor.fetchone()
        
        if data==None:
            input_pass = input("    Create Password: ").lower()
            role = 'user'
            cursor.execute(
            f"INSERT INTO account (username, password, role) VALUES ('{input_username}', '{input_pass}', '{role}')"
        )
            mycon2.commit()
            print(f"Account '{input_username}' created successfully")
            break
        else:
            print(f"The username '{input_username}' is already taken. Please choose a different username.")
        
    mycon2.close()
    return 

# Them User 
def Add_user(admin_user):
    mycon2 = conn2.connect(host="127.0.0.1", user="huyy", password="Huybui1206",database="cafe_payment_system")
    cursor = mycon2.cursor(buffered=True)
    
    cursor.execute(f"SELECT role FROM account WHERE username = '{admin_user}'")
    admin_data = cursor.fetchone()
    if admin_data and admin_data[2]== 'admin':
        while True:
            clear_screen()
            print("=== SIGN UP USER (ADMIN) ===")
            input_username = input("    Create Username (Login ID): ").lower()
            cursor.execute(f"SELECT * FROM account WHERE username = '{input_username}'")
            data = cursor.fetchone()
            if data is None:
                break
            else:
                print(f"The username '{input_username}' is already taken. Please choose a different username.")
        
        input_pass = input("    Create Password: ").lower()
        while True:
            clear_screen()
            print("=== SIGN UP USER (ADMIN) ===")
            print(f"Creating account for {input_username}")
            print("Select role for the new account:")
            print("1. User")
            print("2. Admin")
            choice = input("Enter the number corresponding to the role: ").strip()
            if choice == '1':
                role = 'user'
                break
            elif choice == '2':
                role = 'admin'
                break
            else:
                print("Invalid choice. Please select '1' for user or '2' for admin.")
                
        cursor.execute(
             f"INSERT INTO account (username, password, role) VALUES ('{input_username}', '{input_pass}', '{role}')"
        )
        mycon2.commit()
        print(f"Account '{input_username}' created successfully")
    else:
        print("Access denied. Only admins have the right to create new accounts")
        
    mycon2.close()
    return

# Xoa User
def Del_user(current_user):
    mycon2 = conn2.connect(host="127.0.0.1", user="huyy", password="Huybui1206",database="cafe_payment_system")
    cursor = mycon2.cursor(buffered=True)
    while True:
        clear_screen()
        print("=== DELETE USER ===")
        input_username = input("    Enter the account you want to delete (or type 'exit' to quit): ").lower()
        cursor.execute(f"SELECT * FROM account WHERE username = '{input_username}'")
        data = cursor.fetchone()
        
        if input_username == 'exit':
            print("Exiting delete function.")
            break
        
        if input_username == current_user:
            print("You cannot delete your own account!")
            break
        
        if data is None:
            print(f"No account found with username '{input_username}'.")
            retry = input("Would you like to try again? (yes/no): ").lower()
            if retry != 'yes':
                print("Exiting the delete process.")
                break
        else:
            print(f"Found account with username '{input_username}':")
            print(f"Username: {data[0]}, Role: {data[2]}")
            confirm = input("Are you sure you want to delete this account? (yes/no): ").lower()
            if confirm == 'yes':
                cursor.execute(f"DELETE FROM account WHERE username = '{input_username}'")
                mycon2.commit
                print(f"Account '{input_username}' has been deleted successfully.")
                break
            else:
                print("Account deletion canceled.")
                break
    mycon2.close()
    return
                
# Doi mat khau 
def Change_pass(user_change):
    mycon2 = conn2.connect(host="127.0.0.1", user="huyy", password="Huybui1206",database="cafe_payment_system")
    cursor = mycon2.cursor(buffered=True)
    
    dem=0
    while dem <3:
        clear_screen()
        print("=== CHANGE PASSWORD ===")
        print(f"Change password for account: '{user_change}'")
        
        old_pass = input(f"     Enter old password: ").lower()
        cursor.execute(f"SELECT * FROM account WHERE username = '{user_change}' AND password = '{old_pass}'")
        data= cursor.fetchone()
        
        if data:
            new_pass = input("      Enter new password: ").lower()
            cursor.execute(f"UPDATE account SET password = '{new_pass}' WHERE username = '{user_change}'")
            mycon2.commit()
            print("Password updated successfully.")
            break
        else:
            dem+=1
            if dem < 3:
                print(f"Incorrect password. You have {3 - dem} attempts left.") 
            else:
                print("You have exceeded the maximum number of attempts. Exiting...")
                break
    mycon2.close()
    return
    
# Xem tat ca user
def View_all():
    mycon2 = conn2.connect(host="127.0.0.1", user="huyy", password="Huybui1206",database="cafe_payment_system")
    cursor = mycon2.cursor(buffered=True)
    cursor.execute("SELECT username, password, role FROM account")
    data = cursor.fetchall()
    if not data:
        print("No account found in the database")
        return
    header = ["Username", "Password", "Role"]
    
    table = tabulate(data, headers=header,tablefmt="fancy_grid",stralign='center', colalign=("center", "center", "center"))
    print(table)
    mycon2.close()
    return

    

        
    

def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

    
        
                
        
    
    
    
        