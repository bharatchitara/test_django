from django import urls
from django.urls import include, path, re_path
from login1 import views
 
urlpatterns = [
    path("",views.base,name="base"),
    path("user_login/",views.user_login,name="user_login"),
    path("forgot",views.forgotpassword),
    
    path("signup",views.signup),
    
    path("user_login/getstu",views.get_all_stu),
    #path('user_login/',views.user_login,name="user_login"),
    
    path("student_data",views.update_student),
    path("book_issue",views.book_issue),
    
   ####
   
 
    #path("user_login/",views.student_update),
   
    
    #path("user_login/update_librarian_data/",views.UpdateLibrariandata),
    re_path(r'update_librarian_data/',views.UpdateLibrariandata),

    path("user_login/books_data/",views.Updatebooksdata),
    re_path(r'add_books/new', views.newbooks),
    re_path(r'add_books/',views.addbooks),
    #path("user_login/student_action/",views.student_action),
    #path("user_login/admin/add_new_student/",views.addnew_student),
    
    path("user_login/admin/add_new_librarian/",views.addnew_librarian),
    path("user_login/admin/add_new_librarian/new_librarian/",views.insert_new_librarian),
    re_path(r'new/',views.insert_new_student),
    
    
    #path("user_login/admin/add_new_librarian/",views.addnew_librarian),
    path("user_login/update_librarian_data/add_books",views.addbooks),
    path("user_login/update_librarian_data/add_books/new", views.newbooks),
   # path("user_login/#",views.get_all_stu),
    
    
    path("user_login/update_librarian_data/books_data/", views.Updatebooksdata),
    re_path(r'admin/add_new_student/',views.addnew_student),
    re_path(r'student_action/',views.student_action),
    re_path(r'new_book_get/',views.book_allotment),
    re_path(r'book_issue/',views.book_issue),
    
    re_path(r'student_data/',views.update_student, name = "student_data_update"),
    re_path(r'test_user/',views.test_user),
    
    re_path(r'test_user1/',views.test_user1),
    re_path(r'test_user2',views.test_user2),
    re_path(r'check_email_exist',views.check_email_exist),
    re_path(r'new_signup',views.new_signup),
    
    re_path(r'test_book_allocate/',views.test_book_allocate),
    
    path('test/',views.students),
    
    re_path(r'get_all_librarians',views.get_all_librarians),
    
    
    
   
     
]