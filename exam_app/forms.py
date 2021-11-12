from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


CAT_CHOICES = {
    ('RPG', 'RPG'),
    ("FPS", "FPS"),
    ("TPS", "TPS"),
    ("Horror", "Horror"),
    ("Platformer", "Platformer"),

}


class AuctionAddForm(forms.Form):
    name = forms.CharField(label="name")
    end_date = forms.DateField(label="end_date")
    product_desc = forms.CharField(label="product-desc")
    product_cat = forms.ChoiceField(label="product-cat", choices=CAT_CHOICES)


class AddUserForm(forms.Form):
    login = forms.CharField(max_length=16, label='login')
    username = forms.CharField(label='username')
    password = forms.CharField(max_length=128, widget=forms.PasswordInput, label='password')
    password2 = forms.CharField(max_length=128, widget=forms.PasswordInput)

    def clean_login(self):
        login = self.cleaned_data['login']
        if User.objects.filter(username=login).exists():
            raise ValidationError('taki username istnieje')
        return login

    def clean(self):
        cd = super().clean()
        password = cd['password']
        password2 = cd['password2']
        if password != password2:
            raise ValidationError('hasło nietakiesame')


class LoginForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    def clean(self):
        cd = super().clean()
        username = cd['username']
        password = cd['password']

        user = authenticate(username=username, password=password)
        if user:
            self.user = user
        else:
            raise ValidationError('Podaj poprawne dane')

class UserListForm(forms.Form):
    login = forms.CharField(label='login')
    username = forms.CharField(label='username')
    password = forms.CharField(label='password', widget=forms.PasswordInput)