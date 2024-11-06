import mysql.connector as conn 
import time


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
                #     ## Gọi hàm thêm nước vd: drinks.Add_drink()
                # elif ch ==2:
                #     ## Gọi hàm cập nhật 
                # elif ch==3:
                #     ## Goi ham xoa nuoc
                # ....
                    elif ch==14:
                        end_time = time.time()
                        print("Successfully Logged Out. Your active time was ", end_time - start_time, "seconds")
                        exit(0)
                    else:
                        
                        
                    
                    
                
        
    