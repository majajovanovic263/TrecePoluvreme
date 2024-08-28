from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('test.html', test, name='test.html'),

    # path('pocetna_stranica_igraca.html', igrac, name = 'pocetna_stranica_igraca.html'),
    # path('pocetna_stranica_vlasnika_prostora.html', vlasnik, name='pocetna_stranica_vlasnika_prostora.html'),

    path('registracija_igraca.html', registracijaIgrac, name='registracija_igraca.html'),
    path('registracija_vlasnika_prostora.html', registracijaVlasnik, name='registracija_vlasnika_prostora.html'),
    path('pocetna_stranica.html', template, name='pocetna_stranica.html'),
    path('zaboravljena_lozinka.html', zaboravljena, name='zaboravljena_lozinka.html'),
    path('profil.html', profil, name='profil.html'),
    path('login_req', login_req, name='login_req'),
    path('logout_req', logout_req, name='logout_req'),
    path('registration_req', registration_req, name='registration_req'),
    path('forgotpass_req', forgotpass_req, name='forgotpass_req'),
    path('profilchange_req', profilchange_req, name='profilchange_req'),
    path('team_req', team_req, name='team_req'),
    path('pocetna_stranica_igraca.html', timre, name='pocetna_stranica_igraca.html'),
    path('sala_req', sala_req, name='sala_req'),
    path('pocetna_stranica_vlasnika_prostora.html', salre, name='pocetna_stranica_vlasnika_prostora.html'),
    path('registrationV_req', registrationV_req, name='registrationV_req'),
    path('timovi_traze_igraca.html', timfin, name='timovi_traze_igraca.html'),
    path('sendter', sendter, name='sendter'),
    path('presek', presek, name='presek'),
    path('salaTermini', salaTermini, name='salaTermini'),
    path('rival', rival, name='rival'),
    path('solo', solo, name='solo'),
    path('sendSal', sendSal, name='sendSal'),
    path('soloZakazan', soloZakazan, name='soloZakazan'),
    path('accepted1', accepted1, name='accepted1'),
    path('accepted2', accepted2, name='accepted2'),
    path('denied', denied, name='denied'),
    path('reqToJoin', reqToJoin, name='reqToJoin'),
    path('organizujMec', organizujMec, name='organizujMec'),
    path('duoZakazan', duoZakazan, name='duoZakazan'),
    path('noted', noted, name='noted'),
    path('noted2', noted2, name='noted2'),
    path('uplatiTimu', uplatiTimu, name='uplatiTimu'),
    path('uplatiSalu', uplatiSalu, name='uplatiSalu'),
    path('newPlayer', newPlayer, name='newPlayer'),
]
