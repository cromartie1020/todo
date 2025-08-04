from .models import TodoItem
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm   
from django.contrib.auth.models import User


class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['title', 'description', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'title': 'Todo Title',
            'description': 'Description (optional)',
            'completed': 'Mark as Completed',
        }
        help_texts = {
            'title': 'Enter the title of your todo item.',
            'description': 'You can add a description if needed.',
        }
        error_messages = {
            'title': {
                'required': 'This field is required.',
                'max_length': 'Title cannot exceed 200 characters.',
            },
        }
        
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'username': 'Username',         
                    
        }
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'})) 

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
        labels = {
            'old_password': 'Old Password',
            'new_password1': 'New Password',
            'new_password2': 'Confirm New Password',
        }
        help_texts = {
            'old_password': 'Enter your current password.',
            'new_password1': 'Enter a new password.',
            'new_password2': 'Re-enter the new password for confirmation.',
        }
        error_messages = {
            'old_password': {
                'required': 'This field is required.',
            },
            'new_password1': {
                'required': 'This field is required.',
                'min_length': 'Password must be at least 8 characters long.',
            },
            'new_password2': {
                'required': 'This field is required.',
                'password_mismatch': 'The two password fields didn’t match.',
            },
        }
        widgets = {
            'old_password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'new_password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'new_password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        error_messages = {      
            'old_password': {
                'required': 'This field is required.',
            },
            'new_password1': {
                'required': 'This field is required.',
                'min_length': 'Password must be at least 8 characters long.',
            },
            'new_password2': {
                'required': 'This field is required.',
                'password_mismatch': 'The two password fields didn’t match.',
            },
        }
        help_texts = {
            'old_password': 'Enter your current password.',
            'new_password1': 'Enter a new password.',
            'new_password2': 'Re-enter the new password for confirmation.',
        }
        labels = {
            'old_password': 'Old Password',
            'new_password1': 'New Password',
            'new_password2': 'Confirm New Password',
        }         
