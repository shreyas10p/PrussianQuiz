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

class ProfileForm(forms.ModelForm):#ProfileForm([])
    birth_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    age = forms.CharField(label = 'age', disabled=True,required=False)
    class Meta:
        model = Profile
        fields = ('phone_number','location','birth_date','profile_picture','employer','job_title')
    
    def __init__(self, *args, **kwargs):
        profile = super(ProfileForm, self).__init__(*args, **kwargs)
        self.initial['age'] = kwargs['instance'].get_age()

    def save(self,image_id=None,commit=True):
        print("here")
        profile = super(ProfileForm, self).save(commit=False)
        profile.profile_picture = image_id
        if(commit):
            profile.save()
        return profile


class UpdateUserForm(UserForm):
    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        
        self.fields.pop('password1')
        self.fields.pop('password2')
        