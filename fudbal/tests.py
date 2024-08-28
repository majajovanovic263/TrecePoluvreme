from multiprocessing.connection import Client

from django.test import TestCase
from .models import *
# Create your tests here.

def create_user(u,p,e,t,m,g,i,pr,poz,br):
    # return Igrac.objects.create(username=u,password=p,email=e,telefon=t,mesto=m,godiste=g,admin=a,ime=i,prezime=pr,pozicija=poz,brojdresa=br)
    igrac = Igrac(username=u)
    igrac.set_password(p)
    igrac.email = e
    igrac.telefon = t
    igrac.mesto = m
    igrac.godiste= g
    igrac.ime = i
    igrac.prezime = pr
    igrac.pozicija = poz
    igrac.brojdresa = br
    igrac.save()
    return igrac

def create_vlasnik(u,p,e,t,m,g,i,pr):
    # return Igrac.objects.create(username=u,password=p,email=e,telefon=t,mesto=m,godiste=g,admin=a,ime=i,prezime=pr,pozicija=poz,brojdresa=br)
    vlasnik = Vlasnik(username=u)
    vlasnik.set_password(p)
    vlasnik.email = e
    vlasnik.telefon = t
    vlasnik.mesto = m
    vlasnik.godiste= g
    vlasnik.ime = i
    vlasnik.prezime = pr
    vlasnik.save()
    return vlasnik

def create_mesto(m):
    mest = Mesto(m)
    mest.save()
    return mest

def create_sala(a,c,v,m):
    s = Sala()
    s.mesto = m
    s.idk = v
    s.cenovnik = c
    s.adresa = a
    s.save()
    return s

def create_tim(i,b,m,n):
    tim = Tim()
    tim.mesto = m
    tim.idk_c_field = i
    tim.maxclanova = b
    tim.naziv = n
    tim.save()
    return tim

class RegistrationTest(TestCase):

    def test_create_igrac(self):
        create_user("Denis","Qwer4321!","denis@gmail.com", 0o631234422, create_mesto("Beograd"), 2000,"Denis","Kovačević",2,3)
        us = Igrac.objects.get(username="Denis")
        self.assertEquals(us.email,"denis@gmail.com")
    def test_create_vlasnik(self):
        create_vlasnik("Zoki","Qwer4321!","zoki@gmail.com", 0o631234422, create_mesto("Beograd"), 2000,"Nikola","Ristic")
        us = Vlasnik.objects.get(username="Zoki")
        self.assertEquals(us.email,"zoki@gmail.com")
    def test_create_sala(self):
        create_sala("Jurija Gagarina 9",4500,create_vlasnik("Zoki","Qwer4321!","zoki@gmail.com", 0o631234422, create_mesto("Beograd"), 2000,"Nikola","Ristic"),create_mesto("Beograd"))
        us = Sala.objects.get(adresa="Jurija Gagarina 9")
        self.assertEquals(us.idk, Vlasnik.objects.get(username="Zoki"))
    def test_create_tim(self):
        create_tim(create_user("Denis","Qwer4321!","denis@gmail.com", 0o631234422, create_mesto("Beograd"), 2000,"Denis","Kovačević",2,3),10, create_mesto("Beograd"), "N8")
        us = Tim.objects.get(naziv="N8")
        self.assertEquals(us.idk_c_field, Igrac.objects.get(username="Denis"))

    def test_create_igrac_group(self):
        klijent = Client()
        mestoTest = create_mesto("Beograd")
        response = klijent.post("/registration_req/", data={
            'username': 'Denis1',
            'password1': 'Qwer4321!',
            'password2': 'Qwer4321!',
            'email': 'denis1@gmail.com',
            'ime': 'Denis',
            'prezime': 'Kovačević',
            'telefon': '0o631234423',
            'godiste': '2000',
            'mesto': mestoTest,
            'pozicija': '2',
            'brojdresa': '3'
        })
        self.assertTrue(response.url == "/pocetna_stranica_igraca/")
    def test_create_vlasnik_group(self):
        klijent = Client()
        mestoTest = create_mesto("Beograd")
        response = klijent.post("/registrationV_req/", data={
            'username': 'Zoki1',
            'password1': 'Qwer4321!',
            'password2': 'Qwer4321!',
            'email': 'zoki1@gmail.com',
            'ime': 'Nikola',
            'prezime': 'Ristić',
            'telefon': '0o631234423',
            'godiste': '2000',
            'mesto': mestoTest,
        })
        self.assertTrue(response.url == "/pocetna_stranica_vlasnika_prostora/")
    def test_create_sala_group(self):
        klijent = Client()
        mestoTest = create_mesto("Beograd")
        vlasnikTest = create_vlasnik("Zoki2", "Qwer4321!", "zoki2@gmail.com", 0o631234422, mestoTest, 2000, "Nikola", "Ristic")
        response = klijent.post("/sala_req/", data={
            'idk': vlasnikTest,
            'mesto': mestoTest,
            'adresa': 'Jurija Gagarina 9',
            'cenovnik': '4500'
        })
        self.assertTrue(response.url == "/pocetna_stranica_vlasnika_prostora/")
    def test_create_tim_group(self):
        mestoTest = create_mesto("Beograd")
        kapitenTest = create_user("Denis2","Qwer4321!","denis2@gmail.com", 0o631234422, mestoTest, 2000,"Denis", "Kovačević",2,3)
        response = self.client.post("/team_req/", data={
            'idk_c_field': kapitenTest,
            'mesto': mestoTest,
            'maxclanova': '10',
            'maziv': 'N8'
        })
        self.assertTrue(response.url == "/pocetna_stranica_igraca/")
    def test_login(self):
        mestoTest = create_mesto("Beograd")
        korisnikTest = create_user("Denis3","Qwer4321!","denis3@gmail.com", 0o631234422, mestoTest, 2000,"Denis", "Kovačević",2,3)
        response = self.client.post("/pocetna_stranica/", data={
            'username': 'Denis3',
            'password': 'Qwer4321!'
        })
        self.assertEqual(response.status_code, 200)
    def test_profile_changeAll(self):
        mestoTest = create_mesto("Beograd")
        korisnikTest = create_user("Denis4", "Qwer4321!", "denis4@gmail.com", 0o631234422, mestoTest, 2000, "Denis", "Kovačević", 2, 3)
        response = self.client.post("/profil/", data={
            'password': 'Qwer4321!',
            'email': 'denis10@gmail.com',
            'username': 'Denis4'
        })
        self.assertEqual(response.status_code, 200)
    def test_profile_changeAllButName(self):
        mestoTest = create_mesto("Beograd")
        korisnikTest = create_user("Denis5", "Qwer4321!", "denis5@gmail.com", 0o631234422, mestoTest, 2000, "Denis", "Kovačević", 2, 3)
        response = self.client.post("/profil/", data={
            'password': 'Qwer4321!',
            'email': 'denis10@gmail.com',
            'username': 'Denis4',
            'ime': 'Denis'
        })
        self.assertEqual(response.status_code, 200)
    def test_profile_changeAllButGodiste(self):
        mestoTest = create_mesto("Beograd")
        korisnikTest = create_user("Denis4", "Qwer4321!", "denis10@gmail.com", 0o631234422, mestoTest, 2000, "Denis", "Kovačević", 2, 3)
        response = self.client.post("/profil/", data={
            'password': 'Qwer4321!',
            'email': 'denis10@gmail.com',
            'username': 'Denis4',
            'godiste': '2000'
        })
        self.assertEqual(response.status_code, 200)
    def test_profile_changeAllButPrezime(self):
        mestoTest = create_mesto("Beograd")
        korisnikTest = create_user("Denis4", "Qwer4321!", "denis10@gmail.com", 0o631234422, mestoTest, 2000, "Denis", "Kovačević", 2, 3)
        response = self.client.post("/profil/", data={
            'password': 'Qwer4321!',
            'email': 'denis10@gmail.com',
            'username': 'Denis4',
            'prezime': 'Kovačević'
        })
        self.assertEqual(response.status_code, 200)
    def test_profile_changeAllButTelefon(self):
        mestoTest = create_mesto("Beograd")
        korisnikTest = create_user("Denis4", "Qwer4321!", "denis10@gmail.com", 0o631234422, mestoTest, 2000, "Denis", "Kovačević", 2, 3)
        response = self.client.post("/profil/", data={
            'password': 'Qwer4321!',
            'email': 'denis10@gmail.com',
            'username': 'Denis4',
            'telefon': '0o631234422'
        })
        self.assertEqual(response.status_code, 200)
    def test_profile_changeMesto(self):
        mestoTest = create_mesto("Beograd")
        mestoChange = create_mesto("Novi Sad")
        korisnikTest = create_user("Denis4", "Qwer4321!", "denis10@gmail.com", 0o631234422, mestoTest, 2000, "Denis", "Kovačević", 2, 3)
        response = self.client.post("/profil/", data={
            'password': 'Qwer4321!',
            'email': 'denis10@gmail.com',
            'username': 'Denis4',
            'mesto': mestoChange
        })
        self.assertEqual(response.status_code, 200)