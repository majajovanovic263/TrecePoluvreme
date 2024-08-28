from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm,PasswordResetForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.forms import *
from .models import *



class LoginForm(AuthenticationForm):
    username = UsernameField(widget = TextInput())
    password = CharField(widget= PasswordInput())


class RegisterForm(UserCreationForm):

    class Meta:
        model = Igrac
        fields = ['username', 'password1', 'password2', 'email','ime','prezime', 'telefon', 'godiste','mesto','pozicija','brojdresa']


class VlasnikRegForm(UserCreationForm):
    class Meta:
        model = Vlasnik
        fields = ['username','password1', 'password2', 'email','ime','prezime','telefon', 'godiste', 'mesto']
        #promeniti mesto.object

class ZaboravljenaLozinkaForm(PasswordResetForm):
    class Meta:
        model = Korisnik
        fields = ['email']

class ProfilForm(ModelForm):
    email = CharField(widget= EmailInput())
    password = CharField(widget= PasswordInput())
    class Meta:
        model = Korisnik
        fields = ['ime', 'prezime', 'telefon','mesto']
        # exclude = ['username']


class TeamRegForm(ModelForm):
    class Meta:
        model = Tim
        fields = ['mesto', 'maxclanova', 'naziv']

class SalaRegForma(ModelForm):
    class Meta:
        model = Sala
        fields=['mesto','adresa', 'cenovnik']

class ProslediForma(Form):
    skriveno = CharField(widget=HiddenInput(), required=False)
class ProslediForma2(Form):
    skriveno2 = CharField(widget=HiddenInput(), required=False)
class ProslediForma3(Form):
    skriveno3 = CharField(widget=HiddenInput(), required=False)
class ProslediForma4(Form):
    skriveno4 = CharField(widget=HiddenInput(), required=False)

class ProslediForma5(Form):
    skriveno5 = CharField(widget=HiddenInput(), required=False)
class ProslediForma6(Form):
    skriveno6 = CharField(widget=HiddenInput(), required=False)
class ProslediForma7(Form):
    skriveno7 = CharField(widget=HiddenInput(), required=False)
class ProslediForma8(Form):
    skriveno8 = CharField(widget=HiddenInput(), required=False)

class ProslediForma9(Form):
    skriveno9 = CharField(widget=HiddenInput(), required=False)

class ProslediForma10(Form):
    vidljivo10 = CharField(widget = TextInput(), required=False)
    skriveno10 = CharField(widget=HiddenInput(), required=False)