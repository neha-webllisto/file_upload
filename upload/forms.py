from django import forms

class Student_form(forms.Form):
	firstname = forms.CharField(max_length=20, label='Enter First Name')
	lastname = forms.CharField(max_length=20, label='Enter Last Name')
	file = forms.FileField()