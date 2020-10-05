import os
import datetime
def get_all_files():
    for(root,directories,files)in os.walk(path):
        for file in files:
            print(file)
def get_files_with_extension():
    extension=input("enter a extension:")
    for(root,directories,files)in os.walk(path):
        for file in files:
            if file.endswith(extension):
                print(file)
def get_files_modifed_yesterday():
    start_date=today_date-datetime.timedelta(days=1)
    end_date=today_date
    
    get_files_by_date(start_date,end_date)
def get_files_by_date(start_date,end_date):
    for(root,directories,files)in os.walk(path):
        for i in files:
            file=os.path.join(root,i)
            created_date=get_created_date(file)
            if check_range(created_date,start_date,end_date):
                print(i,"---",created_date)
def check_range(created_date,start_date,end_date):
    if created_date>=start_date and end_date>=created_date:
        return True
    else:
        return False
def get_created_date(file):
    return datetime.date.fromtimestamp(os.path.getctime(file))
def files_between_date():
    try:
        start_date = convert_to_date(input("Enter the start date (yyyy-mm-dd): "))
        end_date = convert_to_date(input("Enter the end date (yyyy-mm-dd): "))
        get_files_by_date(start_date, end_date)
    except:
        print("Invalid Date\"TRY AGAIN\"")
def convert_to_date(x):
    year,month,day=map(int,x.split('-'))
    return datetime.date(year,month,day)
def search_with_date_and_ex():
    try:
        start_date = convert_to_date(input("Enter the start date (yyyy-mm-dd): "))
        end_date = convert_to_date(input("Enter the end date (yyyy-mm-dd): "))
    except:
        print("Invalid Date\"TRY AGAIN\"")
    extension=input("enter a extension:")
    for(root,directories,files)in os.walk(path):
        for i in files:
            file=os.path.join(root,i)
            created_date=get_created_date(file)
            if check_range(created_date,start_date,end_date)and i.endswith(extension):
                print(i,"---",created_date)
    
    
print("IAM MR.FINDER")    
options={1:get_all_files,2:get_files_with_extension,3:get_files_modifed_yesterday,4:files_between_date,5:search_with_date_and_ex}
today_date=datetime.date.today()
while True:
    print("what would you like to search?")
    print("1.All files\n2.find Files with extension\n3.files which are modifed yesterday\n4.find files between a range of days\n5.find files with extension and date \n0.Exit")
    user_input=int(input("Enter your command\n>>>"))
    if user_input==0:
        print("Thank You And Comeback")
        break
    elif user_input in options:
        path=input("Enter The File Path:").strip('"\'')
        options[user_input]()
    else:
        print("Invalid Input\"TRY AGAIN\"\n\n")
        
