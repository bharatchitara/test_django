from email import message
import json
import re
import time
import secrets
import string
import random
import django.contrib.auth
from pickle import NONE
from pydoc import describe, render_doc
from pyexpat.errors import messages
import random
from socket import AddressFamily
from typing_extensions import Self
from urllib import request
from urllib.request import Request
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from pymysql import NULL
from login1.forms import Studentupdate
from login1.models import book_history, books_history, librarian_data, tbl_Authentication
from login1.models import student_data,books_data
import datetime
from django.views.generic import TemplateView
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db.models import Avg,Max
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from datetime import date
import datetime
import dateutil
from dateutil.relativedelta import relativedelta



# Create your views here.
def base(request):
    return render(request, 'base.html')
     

my_username = ''   
 
def user_login(request):
    
    if request.method == 'POST':
        global my_username 
        username = request.POST.get('username')
        
        my_username = username
        
        password = request.POST.get('password')
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')    
        department = request.POST.get('dropdown_dept')
        #last_login = request.POST.get('last_login')  
        book1 = request.POST.get('book1')
        book2 = request.POST.get('book2')
        book3 = request.POST.get('book3')
        
        

        #role = request.POST.get('dropdown')
        #get_role = 0
        
        # if (role == 'student'):
        #     get_role = 1 
        # elif(role == 'lib'):
        #     get_role = 2 
        # elif(role == 'admin'):
        #     get_role = 3      
            
        
        
        valid_email_check = username
        
        flag_valid_email = 0
        
        try:
            validate_email(valid_email_check) 
        except ValidationError as e:
            print("bad email, details:", e)
        else:
            flag_valid_email = 1
            
        month_list = []
        month_list= calculate_month_name()
        #print(month_list)
        
        
        book_count_in_dict = month_count_calcualte()
        
        #for i in range(len(book_count_in_dict)):
        # if( book_count_in_dict.value == 1):
        #     print("aasdfj")
        # else:
        #     print('tyfosd')
                
        print(book_count_in_dict)
        
        # books_data = book_history.objects.values_list('stu_username','book1','book1_allocatedon').filter(stu_username = username)
        # print(books_data)   
        
        books_data = book_history.objects.filter(stu_username = username)
        #print(books_data[0].stu_username)   
        
         
            
        try:
            user = tbl_Authentication.loginauth_objects.get(username=username,password=password)
            
        
            
            if user is not NONE and user.role== 1 and user.is_active == 1 and flag_valid_email == 1:
                #print(username)
                name,age,gender,dropdown_dept,book1,book2,book3 = student_update(username)
                #print(book1)
                
                
                last_login_1 = datetime.datetime.now()
                
                update_time = tbl_Authentication.loginauth_objects.filter(username =username ).update(last_login = last_login_1)
                
            
                fetch_books_data = book_history.objects.all()
                
                get_books_count = book_history.objects.filter(stu_username = username).count()
                
                
                
                return render(request, 'student_dashboard.html',{'last_login':last_login_1,'books_count':get_books_count,'month_list':month_list,'final_book_count_list':book_count_in_dict,'books_data':books_data})
            
                return render(request, 'dashboard.html', 
                              {'username': username,'name':name,'age':age,'gender':gender,'department':dropdown_dept,'book1':book1,'book2':book2,'book3':book3,'fetch_books_data' : fetch_books_data})

            elif user is not NONE and user.role == 2 and user.is_active == 1 and flag_valid_email == 1 :
                lib_fetch_username,lib_name,lib_age,lib_gender = librarian_fetch_data(username)
                # print(lib_username)
                # print(lib_name)
                # print(lib_age)
                # print(lib_gender)
                
                return render(request, 'librarian.html',{'lib_username':lib_fetch_username,'lib_name':lib_name,'lib_age':lib_age,'lib_gender':lib_gender})

            
            elif user is not NONE and user.role == 3 and user.is_active  == 1 and flag_valid_email == 1 :
                fetch_student_data =  student_data.Studentdata_objects.all()
                
                
                #print(fetch_student_data)
                    
                    
                
                return render(request, 'admin.html',{'fetch_student_data':fetch_student_data})
        
            
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username,password))
    
                return redirect('/')
        except Exception as identifier:
            
            return redirect('/')
                
    else:
        return render(request, 'base.html')
    
    
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
    
    
def month_count_calcualte():
    
    month_list = []
    month_list= calculate_month_name()
    
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
    
    
 ## test view 

def students(request):
    
    #name = request.POST.get('name')
    
    student_data1 = student_data.Studentdata_objects.get(username= "bharatc@spanidea.com")
    print(student_data1.department)
      
    return render(request,'new_test.html',{'student_data1' : student_data1})           
    
    
def calculate_month_name():
    
    month_name = []
    for i in range(0,6):
        months = date.today() + relativedelta(months=-i)
        #print(months)
        currentMonthName = months.strftime("%B")
        #print(currentMonthName)
        month_name.append(currentMonthName)
        
    return month_name
    
    
def update_student(request):
    
    username = request.POST.get('username1')
    name = request.POST.get('name')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    #print(gender)
    
    
    gender_upd = ''
    if(gender == 'Male'):
        gender_upd = 'M'
    else:
        gender_upd = 'F'
        
    department = request.POST.get('dropdown_dept')
    #print(department)
    
    dept_upd = 0 
    if(department == 'science'):
        dept_upd = 1
    elif(department == 'arts'):
        dept_upd = 2
    elif(department == 'commerce'):
        dept_upd = 3
    elif(department == 'all'):
        dept_upd = 4
        
        
    #last_login = request.POST.get('time')
    book1 = request.POST.get('book1')
    book2 = request.POST.get('book2')
    book3 = request.POST.get('book3')
    
    #print(username)
    
    obj = student_data(username = username, name = name , age = age , gender = gender_upd, department = dept_upd )
    
    try:
        Update_qry = student_data.Studentdata_objects.filter(username = username).update( name = name , age = age , gender = gender_upd, department = dept_upd)
        
        
        st_name,st_age,st_gender,st_dropdown_dept,st_book1,st_book2,st_book3 = student_update(username)
        
        print(st_book1)
        
        fetch_books_data = book_history.objects.all()
        
        return render(request,'dashboard.html',{'update_student_query_pass': True , 'username': username ,'name':st_name ,'age':st_age,'gender':st_gender,'department':st_dropdown_dept ,'book1':st_book1,'book2':st_book2,'book3':st_book3,'fetch_books_data':fetch_books_data })
        
        
    except:
        #unameby_local = request.GET['uname_local']
        
        st_name,st_age,st_gender,st_dropdown_dept,st_book1,st_book2,st_book3 = student_update(my_username)
        
        fetch_books_data = book_history.objects.all()
        
        return render(request,'dashboard.html',{'update_student_query_fail': True, 'username': my_username ,'name':st_name ,'age':st_age,'gender':st_gender,'department':st_dropdown_dept ,'book1':st_book1,'book2':st_book2,'book3':st_book3,'fetch_books_data':fetch_books_data })
  
    
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
        
    except Exception as identifier:
        flag_getlib_data = 0
        print(flag_getlib_data)
        
   # print(librarian_fetch_data.query())
   # flag_getlib_data = 1
   




def UpdateLibrariandata(request):
    
    
    print(request.GET.get('username'))
    
    get_lib_username = request.POST.get('lib_username1')    
    get_lib_name = request.POST.get('lib_name')
    get_lib_age = request.POST.get('lib_age') 
    get_lib_gender = request.POST.get('lib_gender')
    
    str_lib_gender = ''
    
    if get_lib_gender == 'Male':
        str_lib_gender = 'F'
    else:
        str_lib_gender = 'M'
        
    #lib_fetch_username,lib_name,lib_age,lib_gender = librarian_fetch_data(get_lib_username)
    
    try:
        update_librarian_data = librarian_data.objects.filter(lib_username = get_lib_username).update(lib_name = get_lib_name,lib_age= get_lib_age,lib_gender= str_lib_gender)
        
        lib_fetch_username,lib_name,lib_age,lib_gender = librarian_fetch_data(my_username)
        
        return render(request,"librarian.html",{'update_librarian_query_pass': True , 'lib_username':lib_fetch_username,'lib_name':lib_name,'lib_age':lib_age,'lib_gender':lib_gender})

    
    except:
        
        
        #print("my username is:" +my_username)
        
        lib_fetch_username,lib_name,lib_age,lib_gender = librarian_fetch_data(my_username)
        return render(request,"librarian.html",{'update_librarian_query_pass': True , 'lib_username':lib_fetch_username,'lib_name':lib_name,'lib_age':lib_age,'lib_gender':lib_gender})
    



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
            except:
                flag_book_add = 0 
                
            
            return render(request,'add_book.html',{'flag_book_add':flag_book_add,'test_data': 1})
            

        except Exception as e:
            return HttpResponse('Book not added, Some Error occured!')
                      
       
    except:
        
        return HttpResponse('data')
    
    
    
def student_action(request):
    
    if 'block' in request.POST:
        
        
        block_user = tbl_Authentication.loginauth_objects.filter()
        fetch_student_data =  student_data.Studentdata_objects.all()
        
                
        return render(request, 'admin.html',{'update_student_block_unblock_pass': True  ,'fetch_student_data':fetch_student_data})
    
    
def book_allotment(request):
    if 'issue' in request.POST:
        
        data= request.POST.get('getbookid')
        print(data)
        
        fetch_books_data = books_data.objects.all()
        
        return render(request,'book_issue.html',{'update_allotment_pass': True , 'fetch_book_data': fetch_books_data})
    
    
    
def addnew_student(request):
    num = random.randrange(100000, 999999)
    print(num)
    
    return render(request,"addnew_student.html" , {'num': num}) 

def insert_new_student(request):
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
    
    add_new_student = tbl_Authentication(username = st_username, password = st_password, is_active = st_active, role =st_role  )
    
    try:
        add_new_student.save()
        add_into_st_table =  student_data(username = st_username,name = st_name, age = st_age,gender = gender, department = dept )
        
        add_into_st_table.save()
        
        
        return render(request,'addnew_student.html',{'student_insertion_pass':True})
    
    except:
        return render(request,'addnew_student.html',{'student_insertion_fail':True})
    
    
    return render(request,'add_new_student.html')
    
    


def addnew_librarian(request):
    num = random.randrange(100000, 999999)
    print(num)
    
    return render(request,"addnew_librarian.html", {'num': num})    

def insert_new_librarian(request):
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
    
    add_new_librarian = tbl_Authentication(username = st_username, password = st_password, is_active = st_active, role =st_role  )
    
    try:
        add_new_librarian.save()
        add_into_lib_table =  librarian_data(lib_username = st_username,lib_name = st_name, lib_age = st_age,lib_gender = gender )
        #print(add_into_lib_table)
        add_into_lib_table.save()
        
        
        return render(request,'addnew_librarian.html',{'lib_insertion_pass':True})
    
    except:
        return render(request,'addnew_librarian.html',{'lib_insertion_fail':True})
    
    


 
def book_issue(request):
    
    
    fetch_book_data = books_data.objects.all()
    
    #print(fetch_book_data)
    
    return render(request,"book_issue.html", {'fetch_book_data': fetch_book_data})



def test_user(request):
    result = request.GET.get('getuname')
    print(result)
    
    
    try:
        fetch_student_data = tbl_Authentication.loginauth_objects.get(username = result)
        print(fetch_student_data.is_active)
        if(fetch_student_data.is_active == 1 ):
            unblock_user = tbl_Authentication.loginauth_objects.filter(username = result).update(is_active = 0)
    
        else:
            x = ''
    
    except:
        return HttpResponse("admin -> view name: test_user")
    
    data= {}
    return JsonResponse(data)




def test_user1(request):
    result = request.GET.get('getuname')
    print(result)
    
    
    try:
        fetch_student_data = tbl_Authentication.loginauth_objects.get(username = result)
        print(fetch_student_data.is_active)
        if(fetch_student_data.is_active == 0 ):
            unblock_user = tbl_Authentication.loginauth_objects.filter(username = result).update(is_active = 1)
    
        else:
            y = ''
    
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
            except:
                update_book = student_data.Studentdata_objects.filter(username = unameby_local).update(book1= book_to_be_allot)
                print(update_book)
                
                
                
        elif(check_books_status.book2 == ''):
            print("book2 is empty")
            fetch_book= books_data.objects.get(book_id = result)
        
            book_to_be_allot = fetch_book.book_name
            try:
                update_book= student_data.Studentdata_objects.filter(username = my_username).update(book2= book_to_be_allot)
                print(update_book)
            except:
                update_book= student_data.Studentdata_objects.filter(username = unameby_local).update(book2= book_to_be_allot)
                print(update_book)
                
        
        elif(check_books_status.book3 == ''):
            print("book3 is empty")
            fetch_book= books_data.objects.get(book_id = result)
        
            book_to_be_allot = fetch_book.book_name
            try:
                update_student_with_book= student_data.Studentdata_objects.filter(username = my_username).update(book3= book_to_be_allot)
                print(update_student_with_book)
            except:
                update_student_with_book= student_data.Studentdata_objects.filter(username = unameby_local).update(book3= book_to_be_allot)
                print(update_student_with_book)
    else:
        print("The student have already 3 books issued.")
        flag_for_books_check  = 1 
        
    
    
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
    
    
    # lower = "abcdefghijklmnopqrstuvwxyz"
    # upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # numbers = "0123456789"
    # symbols = "!@#$%*"


    # string = lower + upper + numbers + symbols
    # password = "".join(random.sample(string, 8))

    # return password

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
    
    email_from = settings.EMAIL_HOST_USER
    
    try:
        emailexist = tbl_Authentication.loginauth_objects.get(username = getemail)
        email_flag_pass = 1 
        
    except:
        email_flag_pass = 0 
        
    trigger_email = 0
    
    new_passwd = password_generate()
    
    check_passwd = re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$!%*?&])[A-Za-z\d@#$!%*?&]{8,}$",new_passwd)
    
    
    st_name,age,gender,dropdown_dept,book1,book2,book3 = student_update(getemail)
    
    send_message = 'Hello '+st_name+',\n\nWe have received your request to reset your password. Please find below the new password.\nNew password: '+new_passwd+'\n\nRegards,\nadmin\nLMS version 1.0'
    print(send_message)
    
    if(email_flag_pass == 1):
        send_mail(
            'LMS: Reset password',
            send_message,
            email_from,
            [getemail,],
            fail_silently=False,
                )
        
        change_password = tbl_Authentication.loginauth_objects.filter(username = getemail).update(password = new_passwd)
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
    
    new_signup = tbl_Authentication(username = getemail, password = getpasswd, is_active = 1, role = new_role )
    try:
        new_signup.save()
        
        flag_signup = 1 
    except:
        flag_signup = 0 
        print('failed signup')
        
    
    if(flag_signup == 1 ):
        if(new_role == 1):
            student_add = student_data(username = getemail, name = getname)
            try:
                student_add.save()
                flag_success_signup = 1
            except:
                print("student add is failed")
                flag_success_signup = 0
            
        elif(new_role == 2):
            librarian_add = librarian_data(lib_username = getemail, lib_name = getname)
            
            try:
                librarian_add.save()
                flag_success_signup = 2
            except:
                print("librarian add is failed")
                flag_success_signup = 0
    
    
    
    
    
    data= {"flag_success_signup":flag_success_signup}
    # if(flag_success_signup > 0 ):
    #     return render(request,'success_signup.html',{'flag': 1 } )
    # else:
    #     return render(request,'success_signup.html',{'flag': 0 })
    
    #print(flag_success_signup)
    return JsonResponse(data)