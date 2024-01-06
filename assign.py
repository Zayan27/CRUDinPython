import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

client = pymongo.MongoClient(os.getenv('CONNECTION_MONGO'))

db= client.get_database('Employeedata')

collection = db.employees

def add_employee():
    e_id = input(" enter id : "+"\n")
    e_name = input(" enter name : "+"\n")
    dept = input(" enter department : "+"\n")
    sal = input(" enter salary : "+"\n")
    record = {
        "_id" : e_id,
        "name" : e_name,
        "department" : dept,
        "salary" : sal
    }
    collection.insert_one(record)
    print('employee id '+e_id+' details inserted');

def display():
    result = collection.find()
    for i in result:
        print(i);

def update_employee():
    u_id = input("Enter employee id you wanted to update: ")
    query = {'_id': {'$eq': u_id}}
    present_data = collection.find_one(query)
    
    if present_data:
        key = input('Enter key you wanted to update: ')
        value = input('Enter value you wanted to update: ')
        new_data = {'$set': {key: value}}
        collection.update_one({'_id': u_id}, new_data)
        print(collection.find_one(query))
    else:
        print(f"No employee found with id {u_id}");



def delete_employee():
    e_id = input('enter ID you wanted to delete : ')
    query = {'_id':e_id}
    collection.delete_one(query)
    print('employee '+e_id+' is deleted');




while True:
    print("1 : Add Employee")
    print("2 : Update Employee")
    print("3 : Delete Employee")
    print("4 : Display Employee")
    print("5 : Exit")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        add_employee()
    elif ch == 2:
        update_employee()
    elif ch == 3:
        delete_employee()
    elif ch == 4:
        display()
    else:
        break;



