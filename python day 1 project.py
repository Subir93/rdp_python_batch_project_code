
"""
import pymysql
conn_obj=pymysql.connect(host="localhost", user="root", password="Rbei@2014")
cur_obj=conn_obj.cursor() #to execute the sql queries

try:

    dbms=cur_obj.execute("show databases")
except:
    conn_obj.rollback()

for x in cur_obj:
    print(x)

conn_obj.close()
"""

#Database connection details
"""
import mysql.connector #connector is class inside a module named mysql

conn_obj=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rbei@2014",
    database="python_project_curd")
cur_obj=conn_obj.cursor()
"""
import pymysql

conn_obj=pymysql.connect(host="localhost", user="root", password="Rbei@2014",database="python_project_curd")
cur_obj=conn_obj.cursor() #to execute the sql queries

#Define function data_entry_sql
def data_entry_sql(user_name,user_address,user_phone,user_id,user_password):

# Build the query with user-provided name using LIKE operator
    sql = "INSERT INTO cust_details (cust_name, cust_address, cust_phon_no, cust_user_id, cust_password) VALUES (%s, %s, %s, %s, %s)"
    data = (user_name,user_address,user_phone,user_id,user_password)

    try:
        cur_obj.execute(sql, data)
        print("customer ENTRY SUCCESSFUL.")
        conn_obj.commit()
    except pymysql.connect.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()

#Define function data_retrieve
def data_retrieve(user_id):
# Build the query with user-provided name using LIKE operator
#select * from students_details WHERE Roll_no=1;
    query = f"select * from cust_details WHERE cust_user_id=\'{user_id}\'"
    print(query)
    try:
        cur_obj.execute(query)
        result = cur_obj.fetchone()
        conn_obj.commit()
    except pymysql.connect.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()

#print(result)
    return result

def new_cust_registration(user_id):
    user_name = input("Enter your full name: ")
    user_address = input("Enter your address: ")
    user_phone = input("Enter your phone : ")
    user_password = input("Enter your password: ")
    # print("User not found in database")
    data_entry_sql(user_name, user_address, user_phone, user_id, user_password)

def login_check(details_from_database):
    user_password = input("Enter your password: ")
    if user_password == details_from_database[-1]:
        #print("access granted")
        return 1
    else:
        #print("access denied")
        return 0

def audit_table_entry(cust_id, cust_name):

# Build the query with user-provided name using LIKE operator
    sql = "INSERT INTO audit_table (cust_id, cust_name) VALUES (%s, %s)"
    data = (cust_id, cust_name)

    try:
        cur_obj.execute(sql, data)
        print("customer ENTRY SUCCESSFUL.")
        conn_obj.commit()
    except pymysql.connect.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()
def login_entry(cust_id, cust_name,logout_time=None):
    sql = "INSERT INTO audit_table (cust_id, cust_name,logout_time) VALUES (%s, %s, %s)"
    data = (cust_id, cust_name, logout_time)

    try:
        cur_obj.execute(sql, data)
        print("You have successfully loged in")
        conn_obj.commit()
    except pymysql.connect.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()
def logout_entry(cust_id, cust_name,login_time=None):
    sql = "INSERT INTO audit_table (cust_id, cust_name,login_time) VALUES (%s, %s, %s)"
    data = (cust_id, cust_name, login_time)

    try:
        cur_obj.execute(sql, data)
        #print("You have successfully loged out.")
        conn_obj.commit()
    except pymysql.connect.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()

user_id=input("Enter user username: ")
details_from_database=data_retrieve(user_id)
#print(details_from_database[-2])
print(details_from_database)

if details_from_database:
    print("User found in database")
    result_from_login_check=login_check(details_from_database)
    if result_from_login_check:
        #login time should be recorded
        login_entry(details_from_database[-2],details_from_database[1])
        print("Access granted")
        cust_choice=input("Do you want to logout? Y/N")
        if cust_choice=='Y' or cust_choice=='y':
            logout_entry(details_from_database[-2],details_from_database[1])
            print("You have successfully loged out")

else:
    new_cust_registration(user_id)

conn_obj.close()
