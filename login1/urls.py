from django import urls
from django.urls import include, path, re_path
from login1 import views


urlpatterns = [
    path("",views.base,name="base"),
    path("user_login/",views.user_login,name="user_login"),
    path("user_login1",views.user_login1),                             ##updated login view
    path("forgot",views.forgotpassword),
    path("signup",views.signup),
    path("user_login/getstu",views.get_all_stu),
    path("student_data",views.update_student),
    path("dashboard",views.student_dashboard),   #dashboard of student
    #path("book_issue",views.book_issue),
    #path('<int:key_id>/', views.myview, name='myname'),
    path('book_issue/<username>/',views.book_issue),
    path("view_new_books_added",views.view_new_books_added),                    #student dashboard card2 link
    path("view_allocated_books",views.view_allocated_books),                    #student dashboard card1 link
    path("stu_profile",views.stu_profile),
    path("admin_dashboard",views.admin_dashboard),   #admin dashboard
    path("admin_dashboard/student_management",views.student_management),
    path("admin_dashboard/librarian_management",views.librarian_management),
    path("admin_dashboard/student_management/addnew",views.addnew_student),
    path("admin_dashboard/student_management/addnew/add",views.insert_new_student),
    path("admin_dashboard/librarian_management/addnew",views.getnew_librarian),
    path("admin_dashboard/librarian_management/addnew/add",views.insert_new_librarian),
    path("librarian_dashboard",views.librarian_dashboard),    #lib dashboard
    path("lib_profile",views.lib_profile),
    path("lib_update",views.lib_update),
    path("books",views.books),               #view all the books related action in librarian.
    path("librarian_dashboard/addnew_book",views.addnew_book),
    path("librarian_dashboard/addnew_book/save",views.insert_new_book),
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
    #re_path(r'book_issue/',views.book_issue),
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