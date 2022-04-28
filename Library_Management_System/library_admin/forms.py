from asyncio.windows_events import NULL
from django import forms
from django.contrib.auth.models import User
from library_admin.models import Book, Issued_Book

class AdminRegisterform(forms.ModelForm):

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control w-50 m-auto'}))

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
            ),
        }


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'description', 'quantity', 'category']
        widgets = {
            'name' : forms.TextInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'description' : forms.Textarea(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'quantity' : forms.TextInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'category' : forms.Select(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
        }


class Issue_Book_Form(forms.ModelForm):
    class Meta:
        model = Issued_Book
        fields = ['username', 'email', 'address', 'book', 'issued_date', 'return_date', 'charge_per_day']
        widgets = {
            'username' : forms.TextInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'email' : forms.EmailInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'address' : forms.Textarea(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'book' : forms.Select(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),        
            'issued_date' : forms.DateInput(
                format=('%d-%m-%Y'),
                attrs={'class' : 'form-control w-50 m-auto',
                'type' : 'date'}
            ),
            'charge_per_day' : forms.TextInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        qun = Book.objects.get(name=user.book)
        if commit:
            if qun.quantity>0:
                x = qun.quantity - 1
                Book.objects.filter(name=user.book).update(quantity=x)
                user.save()
        return user


class Issue_Book_Edit_Form(forms.ModelForm):
    class Meta:
        model = Issued_Book
        fields = ['username', 'email', 'address', 'book', 'issued_date', 'return_date', 'charge_per_day']
        widgets = {
            'username' : forms.TextInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'email' : forms.EmailInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'address' : forms.Textarea(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'book' : forms.Select(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),        
            'issued_date' : forms.DateInput(
                attrs={'class' : 'form-control w-50 m-auto',
                'type' : 'date'}
            ),
            'return_date' : forms.DateInput(
                attrs={'class' : 'form-control w-50 m-auto',
                'type' : 'date'}
            ),
            'charge_per_day' : forms.TextInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
        }

    def clean(self):
        cleaned_data = super(Issue_Book_Edit_Form, self).clean()
        date = cleaned_data.get('issued_date')
        re_book = cleaned_data.get("return_date")
        if re_book != None:
            days = re_book.day - date.day
        # if days < 0:
        #     raise forms.ValidationError("Enter valid return date.")
        return super().clean()

    def save(self, commit=True):
        user = super().save(commit=False)
        qun = Book.objects.get(name=user.book)
        if commit:
            if user.return_date != None:
                x = qun.quantity + 1
                Book.objects.filter(name=user.book).update(quantity=x)
            else:
                pass
            user.save()
        return user