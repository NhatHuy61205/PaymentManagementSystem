import mysql.connector as conn 
import time
from login import Usern, Userp
import drinks

start_time = time.time()
# a: user 
# b: password
# c: xác định quyền truy cập
def main_menu(a,b,c):
    mycon = conn.connect(host="127.0.0.1", user="huyy", password="Huybui1206",database="cafe_payment_system")
    login = 0 
    
# Kiểm tra thông tin đăng nhập
    while login!=1:
        cursor = mycon.cursor()
        cursor.execute(f"select * from accounts where username = '{a}' and passwd = '{b}' ")
        data = cursor.fetchone()   
        if data == None:
            print("Wrong Credentials!!!")
            break
        else:
            if data[0]==1:
                while c!=1:    #Menu cho Quản trị viên 
                    print("    Successfully Logged In. \n"
                          "    You are Administrator :)")
                    c=1
                print("Select your choice: \n"
                      "     1 -> Add New Drinks \n" +
                      "     2 -> Update New Drinks Information \n" +
                      "     3 -> Remove Drinks \n" +
                      "     4 -> See Drink Details \n" +
                      "     5 -> View All Drinks \n" + 
                      "     6 -> View A Bill \n" +
                      "     7 -> View Bill By Date \n "+
                      "     8 -> Revenue Statistics \n" +
                      "     9 -> Add New User \n" +
                      "     10 -> Update User Information \n" +
                      "     11 -> Remove User \n" +
                      "     12 -> View All Users \n" +
                      "     13 -> View User Details" +
                      "     14 -> Exit")
                ch = int(input("Enter your choice from (1 to 14): "))
                if ch ==1:
                    drinks.Add_drink()
                elif ch==2:
                    drinks.Update_drink()
                elif ch==3:
                    drinks.Delete_drink()
                elif ch==4:
                    drinks.View_details()
                elif ch==5:
                    drinks.View_all()
                elif ch==14:
                    end_time = time.time()
                    print("Successfully Logged Out. Your active time was ", end_time - start_time, "seconds")
                    exit(0)
                else: 
                    print("Wrong Input")
                login = 1
                again = input("Go Back to Main Menu? (y -> Yes, n -> No and Logout) ")
                    # Goi lam menu
                if again in ['y', 'yes', 'Y', 'YES']:
                    main_menu(a, b, c)
                else:
                    end_time = time.time()
                    print("Process Successfully Done. Logged Out")
                    print("Your active time was ", end_time - start_time, "seconds")
                    exit(0)
            else:
                print("     Successfully Logged In.")
                print("    1-> Order \n" +
                      "    2-> Cancel an Order \n" +
                      "    3-> Add Drinks \n" +
                      "    4-> View Bill \n" +
                      "    5-> Payment \n" +
                      "    6-> Exit")
                ch2 = int(input("Enter your choice from (1 to 6): "))
                if ch2==1:
                    # goi ham orders.
                elif ch2 == 6:
                    end_time = time.time()
                    print("Successfully Logged Out. Your active time was ", end_time - start_time, "seconds")
                    exit(0)
                else:
                    print("Wrong Input.")
                login = 1
                do_again = input("Go Back to Main Menu? (y -> Yes, n -> No and Logout) ")
                if do_again in ['y', 'yes', 'Y', 'YES']:
                    main_menu(a, b, c)
                else:
                    end_time = time.time()
                    print("Process Successfully Done. Logged Out")
                    print("Your active time was ", end_time - start_time, "seconds")
                    exit(0)
    log_ag = str(input("Enter login details again? (y -> Yes, n -> No and exit): "))
    if log_ag == 'y' or log_ag == 'Y':
        user_id = Usern()
        user_pass = Userp()
        main_menu(user_id, user_pass, c)
    else:
        end_time = time.time()
        print("Successfully Logged Out. Your active time was ", end_time - start_time, "seconds")
        exit(0)
                
            
            
                        
                    
                    
                
        
    