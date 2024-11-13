import mysql.connector as conn2
from time import sleep

# Dang ky
def Sign_up():
    mycon2 = conn2.connect(host="127.0.0.1", user="huyy", password="Huybui1206",database="cafe_payment_system")
    cursor = mycon2.cursor(buffered=True)
    while True:
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
    if admin_data and admin_data[0]== 'admin':
        while True:
            input_username = input("    Create Username (Login ID): ").lower()
            cursor.execute(f"SELECT * FROM account WHERE username = '{input_username}'")
            data = cursor.fetchone()
            if data is None:
                break
            else:
                print(f"The username '{input_username}' is already taken. Please choose a different username.")
        
        input_pass = input("    Create Password: ").lower()
        while True:
            role = input("  Enter roles for the new account (user/admin): ").lower()
            if role in ['user', 'admin']:
                break
            else:
                print("Invalid role. Please select 'user' or 'admin'.")
                
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

# Doi mat khau 

# Xem tat ca user



    
        
                
        
    
    
    
        