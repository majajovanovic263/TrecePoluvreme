from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import MinValueValidator, MaxValueValidator,MinLengthValidator

class Korisnik(AbstractUser):
    id = None
    username = models.CharField(db_column='KorIme', primary_key=True, max_length=20, validators=[UnicodeUsernameValidator()])
    password = models.CharField(db_column='Sifra', max_length=128)
    email = models.EmailField(db_column='Email', max_length=40)
    telefon = models.CharField(db_column='Telefon', max_length=10, blank=True, null=True)  # Field name made lowercase.
    mesto = models.ForeignKey('Mesto', models.DO_NOTHING, db_column='IDM',default="")  # Field name made lowercase.
    godiste = models.DecimalField(db_column='Godiste', max_digits=4, decimal_places=0,  default=2005)  # Field name made lowercase.
    admin = models.IntegerField(db_column='Admin', default=0)  # Field name made lowercase.
    ime = models.CharField(db_column='Ime', max_length=18,default="Korisnik")  # Field name made lowercase.
    prezime = models.CharField(db_column='Prezime', max_length=18, default="Bezimeni")  # Field name made lowercase.

    class Meta:
        db_table = 'korisnik'


class Igrac(Korisnik):
    pozicija = models.IntegerField(db_column='Pozicija',default=1, validators=[MinValueValidator(1),MaxValueValidator(4)])  # Field name made lowercase.
    termini = models.CharField(db_column='Termini', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    brojdresa = models.IntegerField(db_column='BrojDresa',default=13, validators=[MinValueValidator(1),MaxValueValidator(99)])  # Field name made lowercase.

    class Meta:
        db_table = 'igrac'


class Mesto(models.Model):
    mesto = models.CharField(db_column='IDM', primary_key=True, max_length=50)  # Field name made lowercase.

    class Meta:
        db_table = 'mesto'


class Pripada(models.Model):

    idt = models.ForeignKey('Tim', models.DO_NOTHING, db_column='IDT')  # Field name made lowercase.
    idk = models.ForeignKey(db_column='Username', max_length=20, to='Igrac', on_delete=models.CASCADE)  # Field name made lowercase.

    uplata = models.DecimalField(db_column='Uplata', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'pripada'
        unique_together = (('idt', 'idk'),)

class Pripada2(models.Model):

    idt = models.ForeignKey('Tim', models.DO_NOTHING, db_column='IDT')  # Field name made lowercase.
    idk = models.ForeignKey(db_column='Username', max_length=20, to='Igrac', on_delete=models.CASCADE)  # Field name made lowercase.

    uplata = models.DecimalField(db_column='Uplata', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'pripada2'
        unique_together = (('idt', 'idk'),)

class RacunTima(models.Model):

    idt = models.ForeignKey('Tim', models.DO_NOTHING, db_column='IDT', primary_key=True)  # Field name made lowercase.
    stanje = models.DecimalField(db_column='Stanje', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'racun_tima'


class Sala(models.Model):
    ids = models.AutoField(db_column='IDS', primary_key=True)  # Field name made lowercase.
    mesto = models.ForeignKey(Mesto, models.DO_NOTHING, db_column='IDM', blank=True, null=True)  # Field name made lowercase.
    slobodnitermini = models.CharField(db_column='SlobodniTermini', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    cenovnik = models.CharField(db_column='Cenovnik', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    idk = models.ForeignKey('Vlasnik', models.DO_NOTHING, db_column='Username')  # Field name made lowercase.
    adresa = models.CharField(db_column='Adresa', max_length=18, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'sala'



class Tim(models.Model):
    idt = models.AutoField(db_column='IDT', primary_key=True)  # Field name made lowercase.
    mesto = models.ForeignKey(Mesto, models.DO_NOTHING, db_column='IDM', blank=True, null=True)  # Field name made lowercase.
    maxclanova = models.IntegerField(db_column='MaxClanova', blank=True, null=True)  # Field name made lowercase.
    idk_c_field = models.ForeignKey(db_column='Username', max_length=20, to='Igrac', on_delete=models.CASCADE)  # Field name made lowercase. Field renamed because it ended with '_'.
    presektermina = models.CharField(db_column='PresekTermina', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    naziv = models.CharField(db_column='Naziv', max_length=50, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        db_table = 'tim'


class Vlasnik(Korisnik):
    stanjeracuna = models.DecimalField(db_column='StanjeRacuna', max_digits=15, decimal_places=2, blank=True, default=0)  # Field name made lowercase.

    class Meta:
        db_table = 'vlasnik'

class TerminUtakmice(models.Model):
    idtr = models.AutoField(db_column='IDTR', primary_key=True)  # Field name made lowercase.
    idt1 = models.ForeignKey(Tim, models.DO_NOTHING, db_column='IDT1', related_name='tim1')  # Field name made lowercase.
    idt2 = models.ForeignKey(Tim, models.DO_NOTHING, db_column='IDT2', related_name='tim2')  # Field name made lowercase.
    ids = models.ForeignKey(Sala, models.DO_NOTHING, db_column='IDS')  # Field name made lowercase.
    rezultat = models.CharField(db_column='Rezultat', max_length=11, blank=True, null=True)  # Field name made lowercase.
    cena = models.DecimalField(db_column='Cena', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    placen = models.IntegerField(db_column='Placen', blank=True, null=True)  # Field name made lowercase.
    vreme = models.TimeField(db_column='Vreme', blank=True, null=True)  # Field name made lowercase.
    datum = models.DateTimeField(db_column='Datum', blank=True, null=True)  # Field name made lowercase.
    dan = models.CharField(db_column='Dan', max_length=2, blank=True, null=True)
    class Meta:
        db_table = 'termin_utakmice'

class Poruke(models.Model):
    idp = models.AutoField(db_column='IDP', primary_key=True)
    idk1 = models.ForeignKey(Korisnik, models.DO_NOTHING, db_column='IDK1', related_name='user1')  # Field name made lowercase.
    idk2 = models.ForeignKey(Korisnik, models.DO_NOTHING, db_column='IDK2', related_name='user2')  # Field name made lowercase.
    idk3 = models.ForeignKey(Korisnik, models.DO_NOTHING, db_column='IDK3', related_name='user3')  # Field name made lowercase.
    ids = models.ForeignKey(Sala, models.DO_NOTHING, db_column='IDS')
    tip = models.IntegerField(db_column='tip', default=0)
    termin = models.CharField(db_column='termin', max_length=5, blank=True, null=True)
    class Meta:
        db_table = 'poruke'
class PorukeIgraca(models.Model):
    idp = models.AutoField(db_column='IDP', primary_key=True)
    idi1 = models.ForeignKey(Igrac, models.DO_NOTHING, db_column='IDI1', related_name='igrac1')  # Field name made lowercase.
    idi2 = models.ForeignKey(Igrac, models.DO_NOTHING, db_column='IDI2', related_name='igrac2')  # Field name made lowercase.
    idt1 = models.ForeignKey(Tim, models.DO_NOTHING, db_column='IDT1', default= "1",related_name='timP1')
    idt2 = models.ForeignKey(Tim, models.DO_NOTHING, db_column='IDT2', default="1",related_name='timP2')
    tip = models.IntegerField(db_column='tip', default=0)
    termin = models.CharField(db_column='termin',max_length=5, blank=True, null=True)

    class Meta:
        db_table = 'poruke_igraca'