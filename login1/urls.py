from django.urls import path, re_path

from login1 import views

urlpatterns = [
    path("",views.base,name="base"),
    #path("user_login/",views.user_login,name="user_login"),
    path("user_login1",views.user_login1),                                                                              ##updated login view
    path("forgot",views.forgotpassword),
    path("signup",views.signup),
    path("user_login/getstu",views.get_all_stu),
    path("student_data/<username>",views.update_student,name= 'student_data'),
    path("dashboard/<username>",views.student_dashboard,name = 'dashboard'),                                            #Dashboard of student
    path("book_issue/<username>",views.book_issue, name = 'book_issue'),                                                #book issue in student login
    path("view_new_books_added/<username>",views.view_new_books_added,name= 'view_new_books_added'),                    #student dashboard card2 link
    path("view_allocated_books/<username>",views.view_allocated_books,name= 'view_allocated_books'),                    #student dashboard card1 link
    path("stu_profile/<username>",views.stu_profile,name = 'stu_profile'),                                              #student profile edit/update
    path("admin_dashboard/<username>",views.admin_dashboard,name = 'admin_dashboard'),                                  #admin dashboard
    path("admin_dashboard/student_management/<username>",views.student_management,name = 'student_management'),         #admin stu management sidenav
    path("admin_dashboard/librarian_management/<username>",views.librarian_management,name = 'librarian_management'),   #admin lib management sidenav
    path("admin_dashboard/student_management/addnew/<username>",views.addnew_student,name = 'addnew_student'),          #admin new stu button 
    path("admin_dashboard/student_management/addnew/add/<username>",views.insert_new_student,name= 'insert_new_student'),    #admin new stu add button 
    path("admin_dashboard/librarian_management/addnew/<username>",views.getnew_librarian,name= 'getnew_librarian'),     #admin new lib button 
    path("admin_dashboard/librarian_management/addnew/add/<username>",views.insert_new_librarian,name= 'insert_new_librarian'),  #admin new lib add button
    path("librarian_dashboard/<username>",views.librarian_dashboard,name= 'librarian_dashboard'),                       #lib dashboard
    path("lib_profile/<username>",views.lib_profile,name= 'lib_profile'),                                               #lib profile update/edit
    path("lib_update/<username>",views.lib_update,name='lib_update'),                                                   #lib profile update button link/refresh the same page
    path("books/<username>",views.books,name= 'books'),                                                                 #view all the books related action in librarian.
    path("librarian_dashboard/addnew_book/<username>",views.addnew_book,name='addnew_book'),                            #add new book form display in lib login
    path("librarian_dashboard/addnew_book/save/<username>",views.insert_new_book,name = 'addnew_book_save'),            #save the new book in lib login
    path("logout",views.logout),
    path("dev",views.dev),
    
    #####################    older links ########################
     #path("user_login/",views.student_update),
    #path("user_login/update_librarian_data/",views.UpdateLibrariandata),
    #re_path(r'update_librarian_data/',views.UpdateLibrariandata),
    path("user_login/books_data/",views.Updatebooksdata),
    re_path(r'add_books/new', views.newbooks),
    re_path(r'add_books/',views.addbooks),
    #path("user_login/student_action/",views.student_action),
    #path("user_login/admin/add_new_student/",views.addnew_student),
    path("user_login/admin/add_new_librarian/",views.addnew_librarian),
    path("user_login/admin/add_new_librarian/new_librarian/",views.insert_new_librarian),
    ################# older links
    re_path(r'new/',views.insert_new_student),
    #path("user_login/admin/add_new_librarian/",views.addnew_librarian),
    path("user_login/update_librarian_data/add_books",views.addbooks),
    path("user_login/update_librarian_data/add_books/new", views.newbooks),
   # path("user_login/#",views.get_all_stu),
    path("user_login/update_librarian_data/books_data/", views.Updatebooksdata),
    re_path(r'admin/add_new_student/',views.addnew_student),
    re_path(r'student_action/',views.student_action),
    re_path(r'new_book_get/',views.book_allotment),
    re_path(r'student_data/',views.update_student, name = "student_data_update"),
    re_path(r'test_user/',views.test_user),
    re_path(r'test_user1/',views.test_user1),
    re_path(r'fetch_book_data/',views.fetch_book_data),
    re_path(r'submit_book/',views.submit_book),
    re_path(r'test_user2',views.test_user2),
    re_path(r'check_email_exist',views.check_email_exist),
    re_path(r'new_signup',views.new_signup),
    re_path(r'test_book_allocate/',views.test_book_allocate),
    #path(r'^test/(?P<username>\w+)/$',views.students),              #for test

    path('test/',views.students),

    re_path(r'get_all_librarians',views.get_all_librarians),
    path("test_page",views.test_page),
]
