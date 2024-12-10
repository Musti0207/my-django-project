from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomerRegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True, label="Ad")
    last_name = forms.CharField(required=True, label="Soyad")
    phone = forms.CharField(required=True, label="Telefon Numarası")
    address = forms.CharField(required=False, label="Adres")
    birthdate = forms.DateField(required=False, label="Doğum Tarihi", widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(
        required=False,
        label="Cinsiyet",
        choices=[('', 'Seçiniz'), ('male', 'Erkek'), ('female', 'Kadın'), ('other', 'Diğer')]
    )

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'phone', 'address', 'birthdate', 'gender']
