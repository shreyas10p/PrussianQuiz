from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile 

class UserForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100,required=False)
    username = forms.CharField(max_length=100, required=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name','username' , 'email' ,'password1', 'password2')

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('phone_number','location','birth_date','profile_picture')

class UpdateUserForm(UserForm):
    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        
        self.fields.pop('password1')
        self.fields.pop('password2')
        