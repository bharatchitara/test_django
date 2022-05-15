
from django import forms
from .models import student_data

class Studentupdate(forms.ModelForm):
    class meta:
        model = student_data
        fields = ['username', 'name', 'age', 'gender' ,'department' ,'Last_login_time' ,'book1' , 'book2', 'book3']
    
    