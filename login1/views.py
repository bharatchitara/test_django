import datetime
import random
import re
import secrets
import string
from datetime import date
from importlib.resources import contents
from pickle import NONE

import pyrebase
from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.contrib.auth.hashers import check_password, make_password
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.db import transaction
from django.db.models import Max
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
##
from rest_framework.views import APIView

from login1.models import (book_history, books_data, librarian_data,
                           student_data, tbl_Authentication)

##  



# Create your views here.
def base(request):
    return render(request, 'base2.html')
     

my_username = ''   


class CustomException(Exception):
    def __init__(self, message="Error occured."):
        super().__init__(self.message)
        
 

# def user_login(request):
    
#     if request.method == 'POST':
#         global my_username 
#         username = request.POST.get('username')
        
#         my_username = username
        
#         password = request.POST.get('password')
#         name = request.POST.get('name')
#         age = request.POST.get('age')
#         gender = request.POST.get('gender')    
#         department = request.POST.get('dropdown_dept')
#         #last_login = request.POST.get('last_login')  
#         book1 = request.POST.get('book1')
#         book2 = request.POST.get('book2')
#         book3 = request.POST.get('book3')
        
        

        
        
#         valid_email_check = username
        
#         flag_valid_email = 0
        
#         try:
#             validate_email(valid_email_check) 
#         except ValidationError as e:
#             print("bad email, details:", e)
#         else:
#             flag_valid_email = 1
            
#         month_list = []
#         month_list,year_list= calculate_month_name()
#         #print(month_list)
        
        
#         book_count_in_dict = month_count_calcualte()
        
#         #for i in range(len(book_count_in_dict)):
#         # if( book_count_in_dict.value == 1):
#         #     print("aasdfj")
#         # else:
#         #     print('tyfosd')
                
#         #print(book_count_in_dict)
        
#         # books_data = book_history.objects.values_list('stu_username','book1','book1_allocatedon').filter(stu_username = username)
#         # print(books_data)   
        
#         books_data1 = book_history.objects.filter(stu_username = username)
#         #print(books_data[0].stu_username)   
        
#         #book_count_in_dict = month_count_calcualte()
    
#         student_count_in_dict  = student_count_by_month()
    
#         lib_count_in_dict = lib_count_by_month()
        
#         book_added_in_last6 = books_count_by_month()
        
#         print("books added ln121")
#         print(book_added_in_last6)
        
#         correct_user = 0
    
        
#         try:
#             is_active_user = tbl_Authentication.loginauth_objects.get(username= username)
#             user_exist = 1 
#         except:
#             user_exist = 0
            
#         if(user_exist == 1 ):
            
#             get_password = tbl_Authentication.loginauth_objects.get(username = username)
#             print(get_password.password)
            
#             check_password1 = check_password (password,get_password.password)
            
#             if (check_password1 == True):
#                 correct_user = 1 
                
         
            
#         try:
#             user = tbl_Authentication.loginauth_objects.get(username=username,password=password)
            
        
            
#             if user is not NONE and user.role== 1 and user.is_active == 1 and flag_valid_email == 1:
#                 #print(username)
#                 name,age,gender,dropdown_dept,book1,book2,book3 = student_update(username)
#                 #print(book1)
                
#                 user = username
#                 username1 = '"'+user+'"'
#                 query  = 'select *,last_login from login1_tbl_authentication where username = '+username1
                
#                 last_login = ''
                
#                 #print(query)
#                 for p in tbl_Authentication.loginauth_objects.raw(query):
#                     last_login = p.last_login
            
#                 fetch_books_data = book_history.objects.all()
                
#                 get_books_count = book_history.objects.filter(stu_username = username).count()
                
                
#                 one_months_past = date.today() + relativedelta(months=-1)
#                 #print(one_months_past)
                
#                 new_books_added = books_data.objects.filter(added_on__gte = one_months_past).count()
                
#                 print("book count"+new_books_added)
                
                
#                 return render(request, 'student_dashboard.html',{'u_name':username,'last_login':last_login,'books_count':get_books_count,'month_list':month_list,'final_book_count_list':book_count_in_dict,'books_data':books_data1})
            
                

#             elif user is not NONE and user.role == 2 and user.is_active == 1 and flag_valid_email == 1 :
                
#                 lib_fetch_username,lib_name,lib_age,lib_gender = librarian_fetch_data(username)
                
#                 last_login,new_books_added,book_less_than_10copies = librarian_data_for_dashboard(username)
                
                
#                 books_history = book_history.objects.all()
                
#                 print(last_login,new_books_added,book_less_than_10copies)
                
#                 return render(request,'librarian_dashboard.html',{'u_name':username,'books_history':books_history,'lib_username':lib_fetch_username,'lib_name':lib_name,'lib_age':lib_age,'lib_gender':lib_gender,'last_login':last_login,'new_books_added':new_books_added,'book_less_than_10copies':book_less_than_10copies,'book_added_in_last6':book_added_in_last6,'month_list':month_list})
                
#                 #return render(request, 'librarian.html',{'lib_username':lib_fetch_username,'lib_name':lib_name,'lib_age':lib_age,'lib_gender':lib_gender})

            
#             elif user is not NONE and user.role == 3 and user.is_active  == 1 and flag_valid_email == 1 :
#                 fetch_student_data =  student_data.Studentdata_objects.all()
                
                
                
#                 user = 'admin@spanidea.com'
#                 username1 = '"'+user+'"'
#                 query  = 'select *,last_login from login1_tbl_authentication where username = '+username1
                
#                 last_login = ''
                
#                 #print(query)
#                 for p in tbl_Authentication.loginauth_objects.raw(query):
#                     last_login = p.last_login
                
                
#                 one_months_past = date.today() + relativedelta(months=-1)
#                 print(one_months_past)
                
#                 new_students_added = tbl_Authentication.loginauth_objects.filter(role = 1,created_on__gte= one_months_past ).count()
#                 print(new_students_added)
                
#                 new_lib_added = tbl_Authentication.loginauth_objects.filter(role = 2, created_on__gte= one_months_past ).count()
#                 print(new_lib_added)
                
                
#                 allusers = tbl_Authentication.loginauth_objects.filter(role__lt = 3 )
                
                
#                 return render(request, 'admin_dashboard.html',{'last_login':last_login,'allusers':allusers,"new_students_added":new_students_added,"new_lib_added":new_lib_added,'u_name':username,'month_list':month_list,'student_count':student_count_in_dict,'lib_count':lib_count_in_dict})

#                 #return render(request, 'admin.html',{'fetch_student_data':fetch_student_data})
        
            
#             else:
#                 print("Someone tried to login and failed.")
#                 print("They used username: {} and password: {}".format(username,password))
    
#                 return redirect('/')
#         except Exception as identifier:
            
#             return redirect('/')
                
#     else:
#         return render(request, 'base.html')
    

def valid_email_check(username):
    #valid_email_check = username
    user = username
        
    flag_valid_email = 0
    
    try:
        validate_email(user) 
        flag_valid_email = 1
    except CustomException:
        print("incorrect email used")
        flag_valid_email = 0
    return flag_valid_email
        

def user_login1(request):
    
    if request.method == 'POST':
        global my_username
        username = request.POST.get('username')        #get username from base.html
        
        my_username = username                         #create a copy of username to global var
        
        password = request.POST.get('password')        #get passwrd from base.html
        
        is_valid_email = valid_email_check(username)    #checking is valid email 
        
        month_list = [] 
        month_list,year_list= calculate_month_name()                #gets last 6 months name
        
        book_count_in_dict = month_count_calcualte()         #books count by month
        
        #print(book_count_in_dict)
        
        books_data1 = book_history.objects.filter(stu_username = username)
        
        student_count_in_dict  = student_count_by_month()        #students count by month
    
        lib_count_in_dict = lib_count_by_month()                #lib count by month
        
        book_added_in_last6 = books_count_by_month()            #books added in last 6 month count
        
        print("books added ln121")
        print(book_added_in_last6)
        
        correct_user = 0
        user_exist = 0
        
        try:
            is_active_user = tbl_Authentication.loginauth_objects.get(username= username)          #to check if user exist
            user_exist = 1
        except CustomException:
            user_exist = 0 
            
        
        if (user_exist == 1 ):
            get_password = tbl_Authentication.loginauth_objects.get(username = username)              #to fetch hash password of existing user
            print(get_password.password)
            
            check_hash_password = check_password(password,get_password.password)                     #match password with hash
            if (check_hash_password == True):
                correct_user = 1 
        
        if(correct_user == 1 ):
            print("correct user")
            
            try:
                user = tbl_Authentication.loginauth_objects.get(username = username)                           #get rest of the info. of the existing user.
                
            except CustomException:
                return render(request,'base2.html',{'failed_login':True})
                
            if( user is not NONE and user.role == 1 and user.is_active ==1 and is_valid_email == 1):
                
                name,age,gender,dropdown_dept,book1,book2,book3 = student_update(username)
                
                print(user.last_login)
                last_login  = user.last_login
            
                fetch_books_data = book_history.objects.all()
                
                get_books_count = book_history.objects.filter(stu_username = username,submit_status = 0).count()
                
                    
                one_months_past = date.today() + relativedelta(months=-1)
                new_books_added = books_data.objects.filter(added_on__gte = one_months_past).count()
                print(new_books_added)
                

                return render(request, 'student_dashboard.html',{'u_name':username,'last_login':last_login,'books_count':get_books_count,'month_list':month_list,'final_book_count_list':book_count_in_dict,'books_data':books_data1,'new_books_added':new_books_added})
            
            
            ######lib login #####
            elif(user is not NONE and user.role == 2 and user.is_active == 1 and is_valid_email == 1):
                
                lib_fetch_username,lib_name,lib_age,lib_gender = librarian_fetch_data(username)
            
                last_login,new_books_added,book_less_than_10copies = librarian_data_for_dashboard(username)
                
                books_history = book_history.objects.all()
                
                print(last_login,new_books_added,book_less_than_10copies)
                
                return render(request,'librarian_dashboard.html',{'u_name':username,'books_history':books_history,'lib_username':lib_fetch_username,'lib_name':lib_name,'lib_age':lib_age,'lib_gender':lib_gender,'last_login':last_login,'new_books_added':new_books_added,'book_less_than_10copies':book_less_than_10copies,'book_added_in_last6':book_added_in_last6,'month_list':month_list})

            
            ########## admin login ##################
            elif(user is not NONE and user.role == 3 and user.is_active  == 1 and is_valid_email == 1):
            
                fetch_student_data =  student_data.Studentdata_objects.all()
                last_login  = user.last_login
                
                
                one_months_past = date.today() + relativedelta(months=-1)
                print(one_months_past)
        
                new_students_added = tbl_Authentication.loginauth_objects.filter(role = 1,created_on__gte= one_months_past ).count()
                print(new_students_added)
            
                new_lib_added = tbl_Authentication.loginauth_objects.filter(role = 2, created_on__gte= one_months_past ).count()
                print(new_lib_added)
                
            
                allusers = tbl_Authentication.loginauth_objects.filter(role__lt = 3 )
                
                return render(request, 'admin_dashboard.html',{'last_login':last_login,'allusers':allusers,"new_students_added":new_students_added,"new_lib_added":new_lib_added,'u_name':username,'month_list':month_list,'student_count':student_count_in_dict,'lib_count':lib_count_in_dict,'year_list':year_list})
            
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username,password))
                
                return render(request,'base2.html',{'failed_login':True})
            

        else:
            return render(request,'base2.html',{'failed_login':True})
        


def stu_profile(request,username):
    global my_username
    
    my_username = username
    
    st_name,st_age,st_gender,st_dept,book1,book2,book3=student_update(my_username)
    
    return render(request, 'dashboard.html',
                              {'u_name': my_username,'name':st_name,'age':st_age,'gender':st_gender,'department':st_dept,'book1':book1,'book2':book2,'book3':book3})
    


def lib_profile(request,username):
    
    global my_username
    my_username = username
    
    lib_fetch_username,lib_name,lib_age,lib_gender = librarian_fetch_data(my_username)
    
    
    lib_data = {
            "lib_fetch_username": lib_fetch_username,
            "lib_name": lib_name,
            "lib_age":lib_age,
            "lib_gender": lib_gender
            
    }
    
    
    return render(request,'lib_profile.html',{'lib_data':lib_data})
    #return render(request,'lib_profile.html',{'lib_fetch_username':lib_fetch_username,'lib_name':lib_name,'lib_age':lib_age,'lib_gender':lib_gender})


def librarian_data_for_dashboard(username):
    
    user = username
    
    username1 = '"'+user+'"'
    query  = 'select *,last_login from login1_tbl_authentication where username = '+username1
    
    last_login = ''
    
    for p in tbl_Authentication.loginauth_objects.raw(query):
        last_login = p.last_login
    
    
    one_months_past = date.today() + relativedelta(months=-1)
    #print(one_months_past)
    
    new_books_added = books_data.objects.filter(added_on__gte= one_months_past ).count()
    #print(new_books_added)
    
    
    book_less_than_10copies = books_data.objects.filter(total_count__lte = 10).count()
    #print(book_less_than_10copies)
    
    #month_list = []
    #month_list,year_list= calculate_month_name()
    
    #books_count_in_dict = books_count_by_month()
    
    
    ###################
    #print(books_count_in_dict)
    
    
    #return last_login,new_books_added,book_less_than_10copies,books_count_in_dict
    return last_login,new_books_added,book_less_than_10copies
         
    
    
    
    
def student_update(username):
        
    username1 = username
    
    #print(username1)
    
        
    student_data1 = student_data.Studentdata_objects.get(username = username1)
    
    
    student_name = student_data1.name
    #print(student_name)
    student_age = student_data1.age
    #print(student_age)
    student_gender= student_data1.gender
    
    # print(current_time)
    #print(student_gender)
    student_department = student_data1.department
    #print(student_department)
    book1 =  student_data1.book1
    book2 =  student_data1.book2
    book3 =  student_data1.book3
    
    #print(student_department)
    #student_name = 'test'
    return(student_name,student_age,student_gender,student_department,book1,book2,book3)
    


def student_management(request,username):
    global my_username
    my_username = username
    username = my_username
    fetch_student_data =  student_data.Studentdata_objects.all()
    return render(request,'admin2.html',{'u_name':username,'fetch_student_data':fetch_student_data})  



def librarian_management(request,username):
    global my_username
    my_username = username
    username = my_username
    fetch_librarian_data =  librarian_data.objects.all()
    return render(request,'get_all_librarians.html',{'u_name':username,"fetch_librarian_data": fetch_librarian_data})



def getnew_librarian(request,username):
    global my_username
    my_username = username
    username = my_username
    return render(request,'addnew_librarian.html',{'u_name':username})
    
    
def month_count_calcualte():
    
    month_list = []
    month_list,year_list= calculate_month_name()
    
    month_num = []
    month_count = []
    
    dict= {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[]}
    
    #print(month_list)
    
    book_count_by_month = []
        
    six_months_past = date.today() + relativedelta(months=-6)
        #print(months)
        
    getdate = book_history.objects.values_list('book1_allocatedon',flat =True).filter(stu_username = my_username,book1_allocatedon__gte = six_months_past )
        #print(getdate)
        
    for i in range(len(getdate)):
        print(getdate[i])
        MonthName = getdate[i].strftime("%B")
        year = getdate[i].strftime("%Y")
        print(MonthName)
        
            
        for j in range(len(month_list)):
            if(str(month_list[j]) == MonthName):
                    #print(j)
                    
                user = '"'+my_username+'"'
                query = 'select id, EXTRACT(MONTH FROM book1_allocatedon) as "extract",count(*) as "count" from login1_book_history where stu_username = '+ user +' and book1_allocatedon >= CURDATE()- interval 180 day group by EXTRACT(MONTH FROM book1_allocatedon)'
                
                #print(query)
                
                for p in book_history.objects.raw(query):
                        
                    #print(p.extract,p.count)
                    #dict['3'].append(p.count)
                    month_num.append(p.extract)
                    month_count.append(p.count) 
                    
                    continue
                #print(month_num)
        break
    #print("this data")
    
    #dict[month_num].append(month_count)
    
    for i in range(len(month_num)):
        #print(month_num[i])
        #print(month_count[i])
        dict[month_num[i]].append(month_count[i])
        
        
    month_numbers = []
    for i in range(0,6):
        months = date.today() + relativedelta(months=-i)
        #print(months)
        currentMonthName = months.strftime("%m")
        #print(currentMonthName)
        month_numbers.append(currentMonthName)
        
        
    print(month_numbers)
    
    # for i in range(1,len(dict)+1):
    #         if(dict[i] == int(month_numbers[i])):
    #             print("hell yah")
            
    final_book_count_list = []
    
    for i in range(len(month_numbers)):
        for key,value in dict.items():
            if(int(month_numbers[i]) == key):
                final_book_count_list.append(value)
    
        
    return(final_book_count_list)                
    


def student_count_by_month():
    
    
    month_list = []
    month_list,year_list= calculate_month_name()
    
    month_num = []
    month_count = []
    
    dict= {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[]}
    
    #print(month_list)
    
    book_count_by_month = []
        
    six_months_past = date.today() + relativedelta(months=-6)
    
    getdate = tbl_Authentication.loginauth_objects.values_list('created_on',flat =True).filter(role = 1,created_on__gte = six_months_past )
   
    print(getdate.query)

    for i in range(len(getdate)):
        #print(getdate[i])
        MonthName = getdate[i].strftime("%B")
        print(MonthName)
        
        for j in range(len(month_list)):
            if(str(month_list[j]) == MonthName):
                    #print(j)
                    
                query = 'select *, EXTRACT(MONTH FROM created_on) as "extract",count(*) as "count" from login1_tbl_authentication where role = 1 and created_on >= CURDATE()- interval 180 day group by EXTRACT(MONTH FROM created_on)'
                
                print(query)
                
                for p in tbl_Authentication.loginauth_objects.raw(query):
                        
                    #print(p.extract,p.count)
                    #dict['3'].append(p.count)
                    month_num.append(p.extract)
                    month_count.append(p.count) 
                    
                    continue
                #print(month_num)
        break
    #print("this data")
    
    #dict[month_num].append(month_count)
    
    
    for i in range(len(month_num)):
        #print(month_num[i])
        
        #print(month_count[i])
        dict[month_num[i]].append(month_count[i])
        
    month_numbers = []
    for i in range(0,6):
        months = date.today() + relativedelta(months=-i)
        #print(months)
        currentMonthName = months.strftime("%m")
        #print(currentMonthName)
        month_numbers.append(currentMonthName)
        
        
    print(month_numbers)
    
    # for i in range(1,len(dict)+1):
    #         if(dict[i] == int(month_numbers[i])):
    #             print("hell yah")
            
    final_book_count_list = []
    
    for i in range(len(month_numbers)):
        for key,value in dict.items():
            if(int(month_numbers[i]) == key):
                final_book_count_list.append(value)
    
        
    return(final_book_count_list)                
    

def lib_count_by_month():
    
    
    month_list = []
    month_list,year_list= calculate_month_name()
    
    month_num = []
    month_count = []
    
    dict= {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[]}
    
    #print(month_list)
    
    book_count_by_month = []
        
    six_months_past = date.today() + relativedelta(months=-6)
    
    getdate = tbl_Authentication.loginauth_objects.values_list('created_on',flat =True).filter(role = 2,created_on__gte = six_months_past )
   
    print(getdate.query)

    for i in range(len(getdate)):
        #print(getdate[i])
        MonthName = getdate[i].strftime("%B")
        print(MonthName)
        
        for j in range(len(month_list)):
            if(str(month_list[j]) == MonthName):
                    #print(j)
                    
                query = 'select *, EXTRACT(MONTH FROM created_on) as "extract",count(*) as "count" from login1_tbl_authentication where role = 2 and created_on >= CURDATE()- interval 180 day group by EXTRACT(MONTH FROM created_on)'
                
                print(query)
                
                for p in tbl_Authentication.loginauth_objects.raw(query):
                        
                    #print(p.extract,p.count)
                    #dict['3'].append(p.count)
                    month_num.append(p.extract)
                    month_count.append(p.count) 
                    
                    continue
                #print(month_num)
        break
    #print("this data")
    
    #dict[month_num].append(month_count)
    
    
    for i in range(len(month_num)):
        #print(month_num[i])
        #print(month_count[i])
        dict[month_num[i]].append(month_count[i])
        
        
    month_numbers = []
    for i in range(0,6):
        months = date.today() + relativedelta(months=-i)
        #print(months)
        currentMonthName = months.strftime("%m")
        #print(currentMonthName)
        month_numbers.append(currentMonthName)
        
        
    print(month_numbers)
    
    # for i in range(1,len(dict)+1):
    #         if(dict[i] == int(month_numbers[i])):
    #             print("hell yah")
            
    final_lib_count_list = []
    
    for i in range(len(month_numbers)):
        for key,value in dict.items():
            if(int(month_numbers[i]) == key):
                final_lib_count_list.append(value)
    
        
    return(final_lib_count_list)                


  
def books_count_by_month():
    
    month_list = []
    month_list,year_list= calculate_month_name()
    
    month_num = []
    month_count = []
    
    dict= {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[]}
    
    #print(month_list)
    
    book_count_by_month = []
        
    six_months_past = date.today() + relativedelta(months=-6)
    
    getdate = books_data.objects.values_list('added_on',flat =True).filter(added_on__gte = six_months_past )
   
    print(getdate.query)

    for i in range(len(getdate)):
        #print(getdate[i])
        MonthName = getdate[i].strftime("%B")
        print(MonthName)
        
        for j in range(len(month_list)):
            if(str(month_list[j]) == MonthName):
                    #print(j)
                    
                query = 'select *, EXTRACT(MONTH FROM added_on) as "extract",count(*) as "count" from login1_books_data where added_on >= CURDATE()- interval 180 day group by EXTRACT(MONTH FROM added_on)'
                
                print(query)
                
                for p in books_data.objects.raw(query):
                        
                    #print(p.extract,p.count)
                    #dict['3'].append(p.count)
                    month_num.append(p.extract)
                    month_count.append(p.count) 
                    
                    continue
                #print(month_num)
        break
    #print("this data")
    
    #dict[month_num].append(month_count)
    
    
    for i in range(len(month_num)):
        #print(month_num[i])
        #print(month_count[i])
        dict[month_num[i]].append(month_count[i])
        
        
    month_numbers = []
    for i in range(0,6):
        months = date.today() + relativedelta(months=-i)
        #print(months)
        currentMonthName = months.strftime("%m")
        #print(currentMonthName)
        month_numbers.append(currentMonthName)
        
        
    print(month_numbers)
    
            
    final_book_count_list = []
    
    for i in range(len(month_numbers)):
        for key,value in dict.items():
            if(int(month_numbers[i]) == key):
                final_book_count_list.append(value)
    
        
    return(final_book_count_list)                




def student_dashboard(request,username):
    
    global my_username 
    my_username = username
    #print(my_username)
    
    name,age,gender,dropdown_dept,book1,book2,book3 = student_update(my_username)
    
    books_data1 = book_history.objects.filter(stu_username = my_username)
                
    month_list = []
    month_list,year_list= calculate_month_name()
        
        
    book_count_in_dict = month_count_calcualte()
    print(book_count_in_dict)
                    
    user = my_username
    username1 = '"'+user+'"'
    query  = 'select *,last_login from login1_tbl_authentication where username = '+username1
    
    last_login = ''
    
    #print(query)
    for p in tbl_Authentication.loginauth_objects.raw(query):
        last_login = p.last_login


    fetch_books_data = book_history.objects.all()
    
    get_books_count = book_history.objects.filter(stu_username = my_username,submit_status = 0).count()

    one_months_past = date.today() + relativedelta(months=-1)
    new_books_added = books_data.objects.filter(added_on__gte = one_months_past).count()
    print(new_books_added)
    
    
    return render(request, 'student_dashboard.html',{'u_name': my_username,'last_login':last_login,'books_count':get_books_count,'month_list':month_list,'final_book_count_list':book_count_in_dict,'books_data':books_data1,'new_books_added':new_books_added})
            


def admin_dashboard(request,username):
    
    global my_username
    my_username = username
    
    month_list = []
    month_list,year_list= calculate_month_name()

    #book_count_in_dict = month_count_calcualte()
    
    student_count_in_dict  = student_count_by_month()
    
    lib_count_in_dict = lib_count_by_month()
    
    
    
    user = 'admin@spanidea.com'
    username = '"'+user+'"'
    query  = 'select *,last_login from login1_tbl_authentication where username = '+username
    
    last_login = ''
    
    #print(query)
    for p in tbl_Authentication.loginauth_objects.raw(query):
        last_login = p.last_login
    
    
    one_months_past = date.today() + relativedelta(months=-1)
    print(one_months_past)
    
    new_students_added = tbl_Authentication.loginauth_objects.filter(role = 1,created_on__gte= one_months_past ).count()
    print(new_students_added)
    
    new_lib_added = tbl_Authentication.loginauth_objects.filter(role = 2, created_on__gte= one_months_past ).count()
    print(new_lib_added)
    
    
    allusers = tbl_Authentication.loginauth_objects.filter(role__lt = 3 )
    
    return render(request, 'admin_dashboard.html',{'last_login':last_login,'allusers':allusers, "new_students_added":new_students_added,"new_lib_added":new_lib_added,'u_name':my_username,'month_list':month_list,'student_count':student_count_in_dict,'lib_count':lib_count_in_dict,'year_list':year_list})




def librarian_dashboard(request,username):
    
    global my_username
    my_username = username
    
    month_list = []
    month_list,year_list= calculate_month_name()

    last_login,new_books_added,book_less_than_10copies = librarian_data_for_dashboard(my_username)
    
    book_added_in_last6 = books_count_by_month()
    
    books_history = book_history.objects.all()
    
    print(last_login,new_books_added,book_less_than_10copies)
    
    return render(request,'librarian_dashboard.html',{'u_name':my_username,'books_history':books_history,'last_login':last_login,'new_books_added':new_books_added,'book_less_than_10copies':book_less_than_10copies,'book_added_in_last6':book_added_in_last6,'month_list':month_list})
                



def students(request):
    
    #name = request.POST.get('name')
    
    
    print(request.GET.get('username'))
    
    student_data1 = student_data.Studentdata_objects.get(username= "bharatchitara99@gmail.com")
    print(student_data1.department)
      
    return render(request,'new_test.html',{'student_data1' : student_data1})           
    
    
def calculate_month_name():
    
    month_name = []
    year_list = []
    for i in range(0,6):
        months = date.today() + relativedelta(months=-i)
        #print(months)
        currentMonthName = months.strftime("%B")
        year = months.strftime("%Y")
        #print(currentMonthName)
        month_name.append(currentMonthName)
        year_list.append(year)
        
    return month_name,year_list
    

    
def update_student(request,username):
    
    global my_username
    my_username = username
    
    username = request.POST.get('username1')
    
    print(username)
    name = request.POST.get('name')
    print(name)
    age = request.POST.get('age')
    print(age)
    gender = request.POST.get('gender')
    print(gender)
    
    
    gender_upd = ''
    if(gender == 'Male'):
        gender_upd = 'M'
    else:
        gender_upd = 'F'
        
    department = request.POST.get('dropdown_dept')
    print(department)
    
    dept_upd = 0 
    if(department == 'science'):
        dept_upd = 1
    elif(department == 'arts'):
        dept_upd = 2
    elif(department == 'commerce'):
        dept_upd = 3
    elif(department == 'all'):
        dept_upd = 4
        
    
    #print(username)
    
    obj = student_data(username = username, name = name , age = age , gender = gender_upd, department = dept_upd )
    
    try:
        Update_qry = student_data.Studentdata_objects.filter(username = username).update( name = name , age = age , gender = gender_upd, department = dept_upd)
        
        
        st_name,st_age,st_gender,st_dropdown_dept,st_book1,st_book2,st_book3 = student_update(username)
        
        print(st_book1)
        
        #fetch_books_data = book_history.objects.all()
        
        return render(request,'dashboard.html',{'update_student_query_pass': True , 'u_name': username ,'name':st_name ,'age':st_age,'gender':st_gender,'department':st_dropdown_dept  })
        
        
    except CustomException:
        #unameby_local = request.GET['uname_local']
        
        st_name,st_age,st_gender,st_dropdown_dept,st_book1,st_book2,st_book3 = student_update(my_username)
        
        #fetch_books_data = book_history.objects.all()
        
        return render(request,'dashboard.html',{'update_student_query_fail': True, 'u_name': my_username ,'name':st_name ,'age':st_age,'gender':st_gender,'department':st_dropdown_dept })
  
    
def librarian_fetch_data(username):
    username1 = username
    #print(username1)
    flag_getlib_data = 0
    
    
    try:
        librarian_fetch_data = librarian_data.objects.get(lib_username = username1)
        
        lib_fetch_username = librarian_fetch_data.lib_username
        lib_name = librarian_fetch_data.lib_name
        lib_age = librarian_fetch_data.lib_age
        lib_gender = librarian_fetch_data.lib_gender
        
        flag_getlib_data = 1
        print(flag_getlib_data)
        
        return(lib_fetch_username,lib_name,lib_age,lib_gender)
        
    except CustomException:
        flag_getlib_data = 0
        print(flag_getlib_data)
        
   # print(librarian_fetch_data.query())
   # flag_getlib_data = 1
   





def lib_update(request):
    
    
    print(request.GET.get('username'))
    
    get_lib_username = request.POST.get('username1')   
    

    get_lib_name = request.POST.get('name')
    get_lib_age = request.POST.get('age') 
    get_lib_gender = request.POST.get('gender')
    
    print(get_lib_username,get_lib_name,get_lib_age,get_lib_gender) 
    
    str_lib_gender = ''
    
    if get_lib_gender == 'Male':
        str_lib_gender = 'M'
    else:
        str_lib_gender = 'F'
        
    #lib_fetch_username,lib_name,lib_age,lib_gender = librarian_fetch_data(get_lib_username)
    
    try:
        update_librarian_data = librarian_data.objects.filter(lib_username = get_lib_username).update(lib_name = get_lib_name,lib_age= get_lib_age,lib_gender= str_lib_gender)
        
        lib_fetch_username,lib_name,lib_age,lib_gender = librarian_fetch_data(get_lib_username)
        
        return render(request,"lib_profile.html",{'update_librarian_query_pass': True , 'lib_fetch_username':lib_fetch_username,'lib_name':lib_name,'lib_age':lib_age,'lib_gender':lib_gender})

    
    except CustomException:
        
        
        lib_fetch_username,lib_name,lib_age,lib_gender = librarian_fetch_data(get_lib_username)
        
        return render(request,"lib_profile.html",{'update_librarian_query_fail': True , 'lib_fetch_username':lib_fetch_username,'lib_name':lib_name,'lib_age':lib_age,'lib_gender':lib_gender})
    




def Updatebooksdata(request):
    return render(request,"book_data.html")


def addbooks(request):
    
    flag_book_add = 1
 
    return render(request,"add_book.html",{'flag_book_add':flag_book_add})

    
# class UpdateLibrariandata(TemplateView):  # new
    
#     template_name = "update_librarian.html"
    
    

# class Updatebooksdata(TemplateView):  # new
#     template_name = "book_data.html"



def newbooks(request):
    input_book_name = request.POST.get('new_book_name')
    
    print(input_book_name)
    input_book_author = request.POST.get('new_book_author')
    input_book_description  = request.POST.get('description')
    input_book_department  = request.POST.get('dropdown_dept')
    
    department_val = 0 
    if input_book_department == 'science':
        department_val = 1
    elif input_book_department == 'arts':
        department_val = 2
    elif input_book_department == 'commerce':
        department_val = 3
    elif input_book_department == 'all':
        department_val = 4
    
    total_book_count = request.POST.get('books_count')
    input_book_location  = request.POST.get('location')
    
    try:
        fetch_max_book_id = books_data.objects.latest('book_id')
        
        ##fetch max book id based on department wise (if department is : science then department_val is - 1 and max_book_id is - 1XXX)
        max_book_id =  books_data.objects.filter(department = department_val).aggregate(Max('book_id'))
        max_book_id = max_book_id.get('book_id__max') + 1
        
        print(max_book_id)
        print(input_book_name)
        print(input_book_author)
        print(total_book_count)
        print(input_book_description)
        print(input_book_department)
        print(input_book_location)
        
        
        try:
            add_new_book  = books_data(book_name = input_book_name, book_id = max_book_id,book_author = input_book_author, 
                                                  total_count = total_book_count, description = input_book_description, department = department_val,
                                                  location = input_book_location)      
            
            flag_book_add = 0 
            try:
                add_new_book.save()
                flag_book_add= 1 
                print(flag_book_add)
            except CustomException:
                flag_book_add = 0 
                
            
            return render(request,'add_book.html',{'flag_book_add':flag_book_add,'test_data': 1})
            

        except CustomException:
            return HttpResponse('Book not added, Some Error occured!')
                      
       
    except  CustomException:
        
        return HttpResponse('data')
    
    

    
def student_action(request):
    
    if 'block' in request.POST:
        
        
        block_user = tbl_Authentication.loginauth_objects.filter()
        fetch_student_data =  student_data.Studentdata_objects.all()
        
                
        return render(request, 'admin.html',{'update_student_block_unblock_pass': True  ,'fetch_student_data':fetch_student_data})
    

    
def book_allotment(request):
    
    username = my_username
    print(username)
    if 'issue' in request.POST:
        
        data= request.POST.get('getbookid')
        print(data)
        
        fetch_books_data = books_data.objects.all()
        
        return render(request,'book_issue.html',{'u_name':username,'update_allotment_pass': True , 'fetch_book_data': fetch_books_data})
    
    

    
def addnew_student(request,username):
    # num = random.randrange(100000, 999999)
    # print(num)
    global my_username
    my_username = username
    username = my_username
    return render(request,"addnew_student_up.html",{'u_name':username} ) 



def insert_new_student(request):
    
    admin_username = my_username
    
    st_username = request.POST.get('username1')   
    print(st_username)
    
    st_password  = request.POST.get('password')
    #print(st_password)
    
    st_name = request.POST.get('name')  
    print(st_name)
    st_age =  request.POST.get('age')
    print(st_age)
    st_gender  =  request.POST.get('gender')
    print(st_gender)
    
    gender = ''
    if st_gender == 'Male':
        gender = 'M'
    else:
        gender = 'F'
    
    dept = ''
    
    st_dept = request.POST.get('dropdown_dept')
    print(st_dept)
    
    if st_dept == 'science':
        dept = 1
    elif st_dept == 'arts':
        dept  = 2
    elif st_dept == 'commerce':
        dept = 3
    elif st_dept == 'all':
        dept= 4
    
    print(dept)
    
    st_active  = 1
    st_role = 1 
    
    new_passwd = password_generate()
    
    hashed = make_password(new_passwd)
    
    #print(new_passwd)
    
    add_new_student = tbl_Authentication(username = st_username, password = hashed, is_active = st_active, role =st_role  )
    
    try:
        add_new_student.save()
        add_into_st_table =  student_data(username = st_username,name = st_name, age = st_age,gender = gender, department = dept )
        
        add_into_st_table.save()
        
        
        return render(request,'user_addition_page.html',{'u_name':admin_username,'student_insertion_pass':True})
    
    except CustomException:
        return render(request,'user_addition_page.html',{'u_name':admin_username,'student_insertion_fail':True})
    
    
    return render(request,'add_new_student.html')
    
    



def addnew_librarian(request):
    num = random.randrange(100000, 999999)
    print(num)
    
    return render(request,"addnew_librarian.html", {'num': num})    



def insert_new_librarian(request,username):
    global my_username
    my_username = username
    admin_username = my_username
    
    st_username = request.POST.get('username1')   
    print(st_username)
    
    st_password = request.POST.get('password')
    print(st_password)
    st_name = request.POST.get('name')  
    st_age =  request.POST.get('age')
    st_gender  =  request.POST.get('gender')
    print(st_gender)
    
    gender = ''
    if st_gender == 'Male':
        gender = 'M'
    else:
        gender = 'F'
    
    dept = ''
    
    
    new_passwd = password_generate()
    hashed = make_password(new_passwd)
    
    st_dept = request.POST.get('dropdown_dept')
    print(st_dept)
    
    if st_dept == 'science':
        dept = 1
    elif st_dept == 'arts':
        dept  = 2
    elif st_dept == 'commerce':
        dept = 3
    elif st_dept == 'all':
        dept= 4
    
    print(dept)
    
    st_active  = 1
    st_role = 2
    
    add_new_librarian = tbl_Authentication(username = st_username, password = hashed, is_active = st_active, role =st_role  )
    
    try:
        add_new_librarian.save()
        add_into_lib_table =  librarian_data(lib_username = st_username,lib_name = st_name, lib_age = st_age,lib_gender = gender )
        #print(add_into_lib_table)
        add_into_lib_table.save()
        
        
        return render(request,'user_addition_page.html',{'u_name':admin_username,'lib_insertion_pass':True})
    
    except CustomException:
        return render(request,'user_addition_page.html',{'u_name':admin_username,'lib_insertion_fail':True})
    
    


 
def book_issue(request,username):
    
    #username = my_username
    print(username)
    fetch_book_data = books_data.objects.all()
    
    #print(request.GET.get('username'))
    
    #print(fetch_book_data)
    
    
    return render(request,"book_issue.html", {'u_name':username,'fetch_book_data': fetch_book_data})



def view_new_books_added(request,username):
    
    my_username = username
    #username = my_username
    print(my_username)
    
    one_months_past = date.today() + relativedelta(months=-1)
    
    #fetch_book_data = books_data.objects.values_list('book_id','book_name','book_author','total_count','description','department','location').filter(added_on__gte = one_months_past)
    
    fetch_book_data = books_data.objects.filter(added_on__gte = one_months_past).all()
    
    return render(request,"book_issue.html", {'u_name':my_username,'fetch_book_data': fetch_book_data})



def view_allocated_books(request,username):
    
    my_username = username
    print(my_username)
    
    one_months_past = date.today() + relativedelta(months=-1)
    
    fetch_book_data = book_history.objects.filter(stu_username = my_username,submit_status = 0).all()
    
    return render(request,"view_allocated_books.html", {'u_name':my_username,'fetch_book_data': fetch_book_data})



def test_user(request):
    result = request.GET.get('getuname')
    print(result)
    
    
    try:
        fetch_student_data = tbl_Authentication.loginauth_objects.get(username = result)
        print(fetch_student_data.is_active)
        if(fetch_student_data.is_active == 1 ):
            unblock_user = tbl_Authentication.loginauth_objects.filter(username = result).update(is_active = 0)
    
    
    except:
        return HttpResponse("admin -> view name: test_user")
    
    data= {}
    return JsonResponse(data)


def fetch_book_data(request):
    bookid = request.GET.get('getbookid')
    bookname = request.GET.get('getbookname')
    bookauthor = request.GET.get('getbookauthor')
    total_count1 = request.GET.get('getbooktotalcount')
    bookdesc = request.GET.get('getbookdesc')
    booklocation = request.GET.get('getbooklocation')
    
    success_book_data = 0
    
    current_time = datetime.datetime.now()
    
    
    print(bookid,bookname,bookauthor,total_count1,bookdesc,booklocation )
    
    try:
        books_data.objects.filter(book_id = bookid).update(book_name = bookname, book_author= bookauthor,total_count = total_count1, description = bookdesc, location = booklocation,last_changed = current_time )
        success_book_data = 1        
    except:
        success_book_data = 0
    
    data= {"success_book_data":success_book_data}
    return JsonResponse(data)


def test_user1(request):
    result = request.GET.get('getuname')
    print(result)
    
    
    try:
        fetch_student_data = tbl_Authentication.loginauth_objects.get(username = result)
        print(fetch_student_data.is_active)
        if(fetch_student_data.is_active == 0 ):
            unblock_user = tbl_Authentication.loginauth_objects.filter(username = result).update(is_active = 1)
    
    
    except:
        return HttpResponse("admin -> view name: test_user")
    
    data= {}
    return JsonResponse(data)

def test_user2(request):
    result = request.GET.get('getuname')
    print(result)
    flag_st_del = 0
    
    try:
        
        delete_student_from_login= tbl_Authentication.loginauth_objects.get(username = result)
        delete_student_from_login.delete()
        
        delete_student_from_stu = student_data.Studentdata_objects.get(username = result)
        delete_student_from_stu.delete()
            
        
    except:
        flag_st_del = 1 
    
    data= {"flag_stu_del": flag_st_del}
    return JsonResponse(data)
        
        
def submit_book(request):
    global my_username
    my_username = request.GET['getusername']
    print(my_username)
    book_name = request.GET['getbookname']
    print(book_name)
    
    current_time = datetime.datetime.now()
    
    flag_book1 = 0 
    flag_book2 = 0 
    flag_book3 = 0 
    update_submit_time = 0 
    update_student_data = 0
    flag_success = 0
    
    
    try:
        find_book_no1 = student_data.Studentdata_objects.get(username = my_username,book1 = book_name )
        flag_book1 = 1
    except:
        flag_book1 = 0
        
    try:
        find_book_no2 = student_data.Studentdata_objects.get(username = my_username,book2 = book_name )
        flag_book2 =  1 
    except:
        flag_book2 = 0
    
    try:
        find_book_no3 = student_data.Studentdata_objects.get(username = my_username,book3 = book_name )
        flag_book3 =1 
    except:
        flag_book3 = 0
        
    print(flag_book1,flag_book2,flag_book3)
            
    with transaction.atomic():
        update_submit_time = book_history.objects.filter(stu_username = my_username,book1 = book_name).update(book1_submiton = current_time,submit_status = 1)
        
        if(flag_book1 ==1 ):
            update_student_data = student_data.Studentdata_objects.filter(username = my_username).update(book1= '')
            flag_success = 1 
        elif(flag_book2 ==1):
            update_student_data = student_data.Studentdata_objects.filter(username = my_username).update(book2= '')
            flag_success = 1 
        elif(flag_book3 == 1):
            update_student_data= student_data.Studentdata_objects.filter(username = my_username).update(book3= '')
            flag_success = 1 
            
    print(update_submit_time,update_student_data)
    
    
    
    
    data= {"flag_stu_del": flag_success}
    return JsonResponse(data)
    


def test_book_allocate(request):
    
    flag_for_books_check = 0
    
    result = request.GET['getbookid']
    
    unameby_local = request.GET['uname_local']
    print(unameby_local)
   # print("result is")
    print("result is" + result)
    
    print(my_username)
    
    try:
        check_books_status  = student_data.Studentdata_objects.get(username = my_username)     ##fetch username from global variable
    except:
        check_books_status  = student_data.Studentdata_objects.get(username = unameby_local)   ##fetch username from local storage 
        

    flag_for_book1 = 0
    flag_for_book2 = 0
    flag_for_book3 = 0
    
    book_to_be_allot = ''
    
    print(check_books_status.book1)
    print(check_books_status.book2)
    print(check_books_status.book3)
    
    if (check_books_status.book1 == '' or check_books_status.book2 == '' or check_books_status.book3 == ''):
        print("all empty")
        
        
        if(check_books_status.book1 == ''):
            print("book1 is empty")
            fetch_book= books_data.objects.get(book_id = result)
            print(fetch_book)
        
            book_to_be_allot = fetch_book.book_name
            print(book_to_be_allot)
            
            try:
                update_book = student_data.Studentdata_objects.filter(username = my_username).update(book1= book_to_be_allot)
                print(update_book)
                flag_for_book1 = 1
                
                
            except:
                update_book = student_data.Studentdata_objects.filter(username = unameby_local).update(book1= book_to_be_allot)
                print(update_book)
                flag_for_book1 = 1
                
                
                
        elif(check_books_status.book2 == ''):
            print("book2 is empty")
            fetch_book= books_data.objects.get(book_id = result)
        
            book_to_be_allot = fetch_book.book_name
            try:
                update_book= student_data.Studentdata_objects.filter(username = my_username).update(book2= book_to_be_allot)
                print(update_book)
                flag_for_book2 = 1
            except:
                update_book= student_data.Studentdata_objects.filter(username = unameby_local).update(book2= book_to_be_allot)
                print(update_book)
                flag_for_book2 = 1
                
        
        elif(check_books_status.book3 == ''):
            print("book3 is empty")
            fetch_book= books_data.objects.get(book_id = result)
        
            book_to_be_allot = fetch_book.book_name
            try:
                update_student_with_book= student_data.Studentdata_objects.filter(username = my_username).update(book3= book_to_be_allot)
                print(update_student_with_book)
                flag_for_book3 = 1
                
            except:
                update_student_with_book= student_data.Studentdata_objects.filter(username = unameby_local).update(book3= book_to_be_allot)
                print(update_student_with_book)
                flag_for_book3 = 1
    else:
        print("The student have already 3 books issued.")
        flag_for_books_check  = 1 
        
    
    if(flag_for_book1 ==1 or flag_for_book2 == 1 or flag_for_book3 == 1 ):
        
        time = datetime.datetime.now()
        
        try:
            new_book_history = book_history(stu_username = my_username,book1 = book_to_be_allot, book1_allocatedon = time) 
            save_book_history = new_book_history.save()
        except:
            new_book_history = book_history(stu_username = unameby_local,book1 = book_to_be_allot, book1_allocatedon = time) 
            save_book_history = new_book_history.save()
        
    
    
    data= {"flag": flag_for_books_check}
    return JsonResponse(data)


def get_all_librarians(request):
    return HttpResponse('librarian data')



def get_all_stu(request):
    
    fetch_student_data =  student_data.Studentdata_objects.all()
                
    return render(request, 'admin.html',{'fetch_student_data':fetch_student_data})


        
def forgotpassword(request):
    
    return render(request,'forgot_passwd.html')


def password_generate():
    

    symbols = ['!','@','#','$','%','*'] # Can add more
    
    password = ""
    
    for i in range(8):
        password += secrets.choice(string.ascii_lowercase)
    password += secrets.choice(string.ascii_uppercase)
    password += secrets.choice(string.digits)
    password += secrets.choice(symbols)
    return password


def check_email_exist(request):
    
    getemail = request.GET['getemail']
    print(getemail)
    
    email_flag_pass = 0
    emailexist = ''
    
    email_from = settings.EMAIL_HOST_USER
    
    try:
        emailexist = tbl_Authentication.loginauth_objects.get(username = getemail)
        email_flag_pass = 1 
        
    except CustomException:
        email_flag_pass = 0 
        
    trigger_email = 0
    
    new_passwd = password_generate()
    
    st_name = ''
    
    hashed = make_password(new_passwd)    #hashing of new password
    
    check_passwd = re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$!%*?&])[A-Za-z\d@#$!%*?&]{8,}$",new_passwd)
    
    if (emailexist.role == 1 ):
        st_name,age,gender,dropdown_dept,book1,book2,book3 = student_update(getemail)
        
    elif(emailexist.role == 2 ):
        lib_fetch_username,lib_name,lib_age,lib_gender = librarian_fetch_data(getemail)
        st_name = lib_name
        
    
    elif(emailexist.role == 3 ):
        st_name = 'Admin'
        
    
    send_message = 'Hello '+st_name+',\n\nWe have received your request to reset your password. Please find below the new password.\nNew password: '+new_passwd+'\n\nRegards,\nadmin\nLMS version 1.0'
    print(send_message)
    
    if(email_flag_pass == 1):
        send_mail(
            'LMS version1.0: Reset password',
            send_message,
            email_from,
            [getemail,],
            fail_silently=False,
                )
        
        change_password = tbl_Authentication.loginauth_objects.filter(username = getemail).update(password = hashed)
        trigger_email = 1
    #trigger_email = 1 
    data= {'email_flag': email_flag_pass, 'trigger_email': trigger_email}
    return JsonResponse(data)


def signup(request):
    return render(request,'signup.html')


def new_signup(request):
    
    getemail  = request.GET['sendemail']
    getname = request.GET['sendname']
    getpasswd = request.GET['sendpasswd']
    getrole = request.GET['sendrole']
    
    print("email is:"+getemail+" name is: " +getname+"passwd is: "+getpasswd+ "role is: "+getrole)
    
    new_role = 0
    
    if (getrole == 'student'):
        new_role = 1
    elif(getrole == 'lib'):
        new_role = 2
    
    flag_signup = 0
    flag_success_signup = 0
    
    hashed = make_password(getpasswd)
    
    new_signup = tbl_Authentication(username = getemail, password = hashed, is_active = 1, role = new_role )
    try:
        new_signup.save()
        
        flag_signup = 1 
    except CustomException:
        flag_signup = 0 
        print('failed signup')
        
    
    if(flag_signup == 1 ):
        if(new_role == 1):
            student_add = student_data(username = getemail, name = getname)
            try:
                student_add.save()
                flag_success_signup = 1
            except CustomException:
                print("student add is failed")
                flag_success_signup = 0
            
        elif(new_role == 2):
            librarian_add = librarian_data(lib_username = getemail, lib_name = getname)
            
            try:
                librarian_add.save()
                flag_success_signup = 2
            except CustomException:
                print("librarian add is failed")
                flag_success_signup = 0
    
    
    
    
    
    data= {"flag_success_signup":flag_success_signup}
    # if(flag_success_signup > 0 ):
    #     return render(request,'success_signup.html',{'flag': 1 } )
    # else:
    #     return render(request,'success_signup.html',{'flag': 0 })
    
    #print(flag_success_signup)
    return JsonResponse(data)


def logout(request):
    username1 = my_username
    
    time = datetime.datetime.now()
    
    update_last_login = tbl_Authentication.loginauth_objects.filter(username = username1).update(last_login = time)
    
    return render(request,'logout.html')

def dev(request):
    return render(request,'devinfo.html')


def test_page(request):
    
    data = {
        "success": True,
        "name": "Vaibhav",
        "age": 20,
        "hobbies": ["Coding", "Art", "Gaming", "Cricket", "Piano"]
    }
    
    
    #user = tbl_Authentication.loginauth_objects.get(username = 'test_user1@gmail.com',password = 'pbkdf2_sha256$180000$El9OJDUbAm1c$ADe6qGrECUQY5V4ZWcW2Wup67UndwTmNYa+PFSiiEXs=')
    #print(user.password)
    
    
    

    #return HttpResponse(json.dumps(data), content_type = "application/json")

    #return response({'Success': True})
    return render(request,'base2.html',{'data':data})




def books(request,username):
    global my_username
    my_username = username
    
    user = my_username
    all_books_data = books_data.objects.all()
    return render(request,'allbook_data.html',{'all_books_data':all_books_data,'u_name':user})



def addnew_book(request,username):
    global my_username
    my_username = username
    
    user = my_username
    
    
    return render(request,'addnew_book_up.html',{'u_name':user})


def insert_new_book(request,username):
    global my_username
    my_username = username
    
    
    input_book_name = request.POST.get('bookname1')
    input_book_author = request.POST.get('author')
    input_count = request.POST.get('copies')
    input_book_description  = request.POST.get('desc')
    input_book_department  = request.POST.get('department')
    
    department_val = 0 
    if input_book_department == 'science':
        department_val = 1
    elif input_book_department == 'arts':
        department_val = 2
    elif input_book_department == 'commerce':
        department_val = 3
    elif input_book_department == 'all':
        department_val = 4
    
    input_book_location  = request.POST.get('location')
    
    
    #fetch_max_book_id = books_data.objects.latest('book_id')
    
    ##fetch max book id based on department wise (if department is : science then department_val is - 1 and max_book_id is - 1XXX)
    max_book_id =  books_data.objects.filter(department = department_val).aggregate(Max('book_id'))
    max_book_id = max_book_id.get('book_id__max') + 1
    
    print(max_book_id)
    print(input_book_name)
    print(input_book_author)
    print(input_count)
    print(input_book_description)
    print(input_book_department)
    print(input_book_location)
    
    book_is_exist = 0
    
    flag_book_add = 0 
    
    cuurent_time = datetime.datetime.now()
    
    try: 
        find_book_exist = books_data.objects.get(book_name = input_book_name)
        book_is_exist = 1
    except CustomException:
        book_is_exist = 0
        
    
    if(book_is_exist == 1):
        print('books already existing...exiting now. Can''t be added again.')
        return render(request,'addnew_book_up.html',{'flag_exist':1,'u_name':my_username})
    
    
    add_new_book  = books_data(book_name = input_book_name, book_id = max_book_id, book_author = input_book_author, 
                                            total_count = input_count, description = input_book_description, department = department_val,
                                            location = input_book_location,added_on =cuurent_time, last_changed = cuurent_time )      
    

    try:
        add_new_book.save()
        flag_book_add= 1 
        print(flag_book_add)
        
    except CustomException:
        flag_book_add = 0 
        
    
    return render(request,'addnew_book_up.html',{'flag_book_add':flag_book_add,'u_name':my_username})
    

    