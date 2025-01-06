from django import forms
from django.contrib.auth.models import User
from dal import autocomplete
from .models import Book, Student
from . import models

class IssueBookForm(forms.Form):
    book_isbn = forms.ModelChoiceField(queryset=models.Book.objects.all(),  to_field_name="isbn", label="Book (Name and ISBN)")
    student_name = forms.ModelChoiceField(queryset=models.Student.objects.all(), to_field_name="user", label="Student Details")
    # days = forms.IntegerField(min_value=1, label="Number of Days")  # Add this field
    
    book_isbn.widget.attrs.update({'class': 'form-control'})
    student_name.widget.attrs.update({'class':'form-control'})
