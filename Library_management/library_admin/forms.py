from pyexpat import model
from django import forms
from django.contrib.auth.models import User

class AdminRegisterForm(forms.ModelForm):
    # user_name = forms.CharField()
    # first_name = forms.CharField()
    # last_name = forms.CharField()
    # email = forms.EmailField()
    # password = forms.PasswordInput()
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
                'username' : forms.TextInput(
                    attrs={'class' : 'form-control w-50 m-auto'}
                ),
                'first_name' : forms.TextInput(
                    attrs={'class' : 'form-control w-50 m-auto'}
                ),
                'last_name' : forms.TextInput(
                    attrs={'class' : 'form-control w-50 m-auto'}
                ),
                'email' : forms.EmailInput(
                    attrs={'class' : 'form-control w-50 m-auto'}
                ),
                'password' : forms.PasswordInput(
                    attrs={'class' : 'form-control w-50 m-auto'}
                ),
            }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class AdminLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username' : forms.TextInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'password' : forms.PasswordInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            )
        }