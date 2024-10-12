from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Usuario, Vino, Avatar, Cata

# class UsuarioFormulario(forms.Form):

#     nombre = forms.CharField()
#     apellido = forms.CharField()
#     email = forms.EmailField()

class UsuarioFormulario(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ('__all__')
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'placeholder': 'usuario...',
                    "class": "input-usuario-nombre"
                }
            )
        }

class VinosFormulario(forms.ModelForm):

    class Meta:
        model = Vino
        fields = ('__all__')

class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)

    def clean_password2(self):

        print(self.cleaned_data)

        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password2 != password1:
            raise forms.ValidationError("Las contraseñas no son iguales")
        
        else:
            return password2
        
class CataForm(forms.ModelForm):

    class Meta:

        model = Cata
        fields = ['fecha', 'vinos', 'tipo_de_cata', 'comentarios']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'vino': forms.CheckboxSelectMultiple(),
        }
        
class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields=('imagen',)

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Nombre')
    last_name = forms.CharField(max_length=30, required=True, help_text='Apellido')
    email = forms.EmailField(max_length=254, required=True, help_text='Correo electrónico')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
