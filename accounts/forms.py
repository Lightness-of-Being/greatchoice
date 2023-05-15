from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        required=True,
        label='아이디',
        widget=forms.TextInput(
            attrs={
                'id': "floating_username",
                'class': 'block w-full py-2.5 px-0 text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 focus:outline-none focus:border-blue-600 peer',
                'placeholder': " "
        })
    )

    password = forms.CharField(
        required=True,
        label='비밀번호',
        widget=forms.TextInput(
            attrs={
                'type': 'password',
                'id': "floating_password",
                'class': 'block w-full py-2.5 px-0 text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 focus:outline-none focus:border-blue-600 peer',
                'placeholder': " "
        })
    )


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        label='아이디',
        widget=forms.TextInput(
            attrs={
                'id': "floating_username",
                'class': 'block w-full py-2.5 px-0 text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 focus:outline-none focus:border-blue-600 peer',
                'placeholder': " "
        })
    )
    password1 = forms.CharField(
        required=True,
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'id': "floating_password",
                'class': 'block w-full py-2.5 px-0 text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 focus:outline-none focus:border-blue-600 peer',
                'placeholder': " "
        })
    )
    password2 = forms.CharField(
        required=True,
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'id': "floating_repeat_password",
                'class': 'block w-full py-2.5 px-0 text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 focus:outline-none focus:border-blue-600 peer',
                'placeholder': " "
        })
    )
    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ('username', 'password', 'password_confirm',)