from django.contrib.auth.decorators import login_required
from django.db.models.query_utils import Q
from django.shortcuts import render, redirect
from django.http import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.template import loader
from django.contrib import messages

from fudbal.forms import *
from django.contrib.auth.hashers import *


def test(request):
    return render(request, 'test.html')


def test2(request):
    return render(request, 'test2.html')

#funkcija koja ucitava stranicu igraca sa njegovim infom i salje podatke u slucaju ptavljenja novog tima
def timre(request):
    template = loader.get_template('pocetna_stranica_igraca.html')
    igr = Igrac.objects.get(username=request.user.get_username())
    poz = igr.pozicija
    if (poz == 1):
        pozTekst = "Golman"
    if (poz == 2):
        pozTekst = "Odbrana"
    if (poz == 3):
        pozTekst = "Vezni"
    if (poz == 4):
        pozTekst = "Napadač"
    t = list(Tim.objects.all().filter(idk_c_field=request.user.username))
    p = list(Pripada2.objects.all().filter(idk=request.user.username))
    timovi = []
    kapTim = []
    br = 0
    for tim in t:
        timovi.append(tim)
    for moj in p:
        kapTim.append(moj.idt)
    kal = igr.termini
    porukeIgraca = PorukeIgraca.objects.all().filter(idi1=igr)
    porukeIgraca2 = PorukeIgraca.objects.all().filter(idi2=igr)
    porukeSale = Poruke.objects.all().filter(idk3=igr)
    tekme = TerminUtakmice.objects.all().exclude(~Q(idt1__in=[o.idt for o in kapTim]),
                                                 ~Q(idt2__in=[o.idt for o in kapTim]))

    context = {
        'hiddenforma': ProslediForma(),
        'hiddenforma2': ProslediForma2(),
        'timici': timovi,
        'mojTim': kapTim,
        'tekmice': tekme,
        'kalendar': kal,
        'broj': igr.brojdresa,
        'poza': pozTekst,
        "forma": TeamRegForm(),
        'poslate': porukeIgraca,
        'primljene': porukeIgraca2,
        'odSale': porukeSale,
        'hiddenforma7': ProslediForma7(),
        'hiddenforma8': ProslediForma8(),
        'hiddenforma9': ProslediForma9(),

    }
    return render(request, 'pocetna_stranica_igraca.html', context)


#funkcija koja ucitava stranicu vlasnika sa njegovim infom i salje podatke u slucaju ptavljenja novog prostora
def salre(request):
    q = list(Sala.objects.all().filter(idk=request.user.username))
    que = []
    for e in q:
        que.append(e)
    context = {
        'que': que,
        "forma": SalaRegForma(),
        "hiddenforma4": ProslediForma4()
    }
    return render(request, 'pocetna_stranica_vlasnika_prostora.html', context)


#funkcija koja sluzi da igtac pretrauje timove kojma ne pripada
def timfin(request):
    tf = list(Pripada2.objects.all().filter(idk=request.user.username))
    find = []
    for f in tf:
        find.append(f.idt)
    timS = Tim.objects.all().exclude(idt__in=[o.idt for o in find])

    context = {
        'timS': timS,
        "forma": ProslediForma()
    }
    return render(request, 'timovi_traze_igraca.html', context)

#funkcija za promenu profila
def profil(request):
    context = {
        "forma": ProfilForm()
    }
    return render(request, 'profil.html', context)


# def igrac (request):
#     return render(request, 'pocetna_stranica_igraca.html')
# def vlasnik (request):
#
#     return render(request, 'pocetna_stranica_vlasnika_prostora.html')

#funkcija za registraciju igraca
def registracijaIgrac(request):
    context = {
        "forma": RegisterForm()
    }
    return render(request, 'registracija_igraca.html', context)


#funkcija za registraciju vlasnika
def registracijaVlasnik(request):
    context = {
        "forma": VlasnikRegForm()
    }
    return render(request, 'registracija_vlasnika_prostora.html', context)




#funkcija za generisanje login forme
def template(request):
    context = {
        "forma": LoginForm()
    }
    return render(request, 'pocetna_stranica.html', context)


#funkcija za generisanje forme za povracaj lozinke u slucaju zaboravljene iste
def zaboravljena(request):
    context = {
        "forma": ZaboravljenaLozinkaForm()
    }
    return render(request, 'zaboravljena_lozinka.html', context)

#funkcija za validaciju login forme sa generisanom login formom i django bekend procesima validacije
def login_req(request):
    form = LoginForm(request=request, data=request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            try:
                igracI = Igrac.objects.get(username=request.user.get_username())
                if (username == igracI.username):
                    return redirect('pocetna_stranica_igraca.html')
            except Exception:
                igracI = Vlasnik.objects.get(username=request.user.get_username())
                if (username == igracI.username):
                    return redirect('pocetna_stranica_vlasnika_prostora.html')
            return redirect('pocetna_stranica_igraca.html')

    return render(request, 'pocetna_stranica.html')

#funkcija za promenu profila i validnost promenjenih podataka
@login_required(login_url='login')
def profilchange_req(request: HttpRequest):
    form = ProfilForm(data=request.POST or None)
    if form.is_valid():
        user = request.user
        novoIme = form.cleaned_data['ime']
        novoPrezime = form.cleaned_data['prezime']
        novoTel = form.cleaned_data['telefon']
        novoEm = form.cleaned_data['email']
        novoMes = form.cleaned_data['mesto']
        novoPass = form.cleaned_data['password']
        if novoIme != None:
            user.ime = novoIme
        if novoPrezime != None:
            user.prezime = novoPrezime
        if novoTel != None:
            user.telefon = novoTel
        if novoEm != None:
            user.email = novoEm
        if novoMes != None:
            user.mesto = novoMes
        if novoPass != None:
            user.password = make_password(novoPass)
        user.save()
        return redirect('pocetna_stranica.html')
    return render(request, 'profil.html')

#logout funkcija
def logout_req(request):
    logout(request)
    return redirect('pocetna_stranica.html')

#request za registraciju igraca
def registration_req(request: HttpRequest):
    form = RegisterForm(data=request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('pocetna_stranica_igraca.html')

    return render(request, 'registracija_igraca.html')

#request za registraciju vlasnika
def registrationV_req(request: HttpRequest):
    form = VlasnikRegForm(data=request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('pocetna_stranica.html')

    return render(request, 'registracija_vlasnika_prostora.html')

#uictavamke forme zaboravljene sifre
def forgotpass_req(request: HttpRequest):
    form = ZaboravljenaLozinkaForm(data=request.POST or None)
    if form.is_valid():
        return redirect('pocetna_stranica.html')

    return render(request, 'registracija_igraca.html')

#validacija forme za pravljenje tima
@login_required(login_url='login')
def team_req(request: HttpRequest):
    form = TeamRegForm(data=request.POST or None)
    if form.is_valid():
        tim = Tim()
        tim.idk_c_field = Igrac.objects.get(username=request.user.get_username())
        timMesto = form.cleaned_data['mesto']
        timMax = form.cleaned_data['maxclanova']
        timNaziv = form.cleaned_data['naziv']
        if (timNaziv != None) and (timMax != None) and (timMesto != None):
            tim.naziv = timNaziv
            tim.maxclanova = timMax
            tim.mesto = timMesto
            tim.save()

            racunce = RacunTima()
            racunce.idt = tim
            racunce.stanje = 0
            racunce.save()

            pripad = Pripada2()
            pripad.idt = tim
            pripad.idk = tim.idk_c_field
            pripad.uplata = 0
            pripad.save()

        return redirect('pocetna_stranica_igraca.html')

    return redirect('pocetna_stranica_igraca.html')

#validacija forme za pravljenje sale
@login_required(login_url='login')
def sala_req(request: HttpRequest):
    form = SalaRegForma(data=request.POST or None)
    if form.is_valid():
        sala = Sala()
        sala.idk = Vlasnik.objects.get(username=request.user.get_username())
        salaMesto = form.cleaned_data['mesto']
        salaAdr = form.cleaned_data['adresa']
        salaCena = form.cleaned_data['cenovnik']

        if (salaAdr != None) and (salaMesto != None) and (salaCena != None):
            sala.adresa = salaAdr
            sala.mesto = salaMesto
            sala.cenovnik = salaCena
            sala.save()
        return redirect('pocetna_stranica_vlasnika_prostora.html')

    return render(request, 'pocetna_stranica_vlasnika_prostora.html')

#upis termina u kalendar igraca
@login_required(login_url='login')
def sendter(request):
    forma = ProslediForma(data=request.POST or None)
    if forma.is_valid():
        stringic = forma.cleaned_data['skriveno']
        igrac1 = Igrac.objects.get(username=request.user.get_username())
        igrac1.termini = stringic + " "
        igrac1.save()
        return redirect('pocetna_stranica_igraca.html')

    return redirect('pocetna_stranica_igraca.html')

#presek termina igraca unutar tima
@login_required(login_url='login')
def presek(request):
    forma = ProslediForma2(data=request.POST or None)
    if forma.is_valid():
        stringic2 = forma.cleaned_data['skriveno2']
        timKapitena = Tim.objects.all().filter(idt=stringic2)
        kapitenTima = timKapitena.values_list().get()
        kap = kapitenTima[3]
        t = kapitenTima[5]
        s = kapitenTima[0]
        tk = Tim.objects.get(idt=stringic2)
        igracKapiten = Igrac.objects.all().filter(username=kap).values_list().get()
        li = list(Pripada2.objects.all().filter(idt=stringic2))
        p = []
        r = []
        for l in li:
            p.append(l.idk)
        for x in p:
            r.append(x.termini)

        tekme = TerminUtakmice.objects.all().exclude(~Q(idt1=tk), ~Q(idt2=tk))

        context = {
            'hiddenforma3': ProslediForma3(),
            'hiddenforma2': ProslediForma2(),
            'forma10':ProslediForma10(),
            'igr': igracKapiten[19],
            'red': r,
            'timC': t,
            'idTC': s,
            'racun': RacunTima.objects.get(idt=tk),
            'tekme': tekme,
            'timOb': tk,
        }
        return render(request, 'kalendar.html', context)
    return render(request, 'pocetna_stranica_igraca.html')

#termini sala
@login_required(login_url='login')
def salaTermini(request):
    forma = ProslediForma4(data=request.POST or None)
    if forma.is_valid():
        stringic4 = forma.cleaned_data['skriveno4']
        salaVlasnika = Sala.objects.get(ids=int(stringic4))
        context = {
            'v': salaVlasnika,
            'hiddenforma5': ProslediForma5(),
            'termini': salaVlasnika.slobodnitermini
        }
        return render(request, 'sale_termini.html', context)
    return render(request, 'pocetna_stranica_vlasnika_prostora.html')

#pamcenje termina sala nakon promene
@login_required(login_url='login')
def sendSal(request):
    forma = ProslediForma5(data=request.POST or None)
    if forma.is_valid():
        stringic5 = forma.cleaned_data['skriveno5']
        listica = stringic5.split(", ")
        salaTerminiPisiId = listica[0]
        listica.pop(0)
        salaTerminiPisi = listica
        salaPis = Sala.objects.get(ids=int(salaTerminiPisiId))
        p = ""
        for s in salaTerminiPisi:
            p = p + s + ", "
        p = p[:-2] + " "
        salaPis.slobodnitermini = p
        salaPis.save()
        context = {
            'v': Sala.objects.get(ids=int(salaTerminiPisiId)),
            'hiddenforma5': ProslediForma5(),
            'termini': p
        }
        return render(request, 'sale_termini.html', context)
    return render(request, 'pocetna_stranica_vlasnika_prostora.html')

#poziv na trening
@login_required(login_url='login')
def solo(request):
    forma = ProslediForma3(data=request.POST or None)
    if forma.is_valid():
        stringic3 = forma.cleaned_data['skriveno3']
        lista1 = stringic3.split(", ")
        idTIma = int(lista1[0])
        lista1.pop(0)
        idPolja = lista1[0]
        lista1.pop(0)
        termince = "";
        for f in lista1:
            termince = termince + f + ", "
        timUpis = Tim.objects.get(idt=idTIma)
        timUpis.presektermina = termince
        timUpis.save()
        sale = Sala.objects.all().values_list()
        listaSala = []
        for s in sale:
            provere = s[2]
            if (provere != None):
                terminiSale = s[2].split(", ")
                for ts in terminiSale:
                    if (ts == idPolja):
                        listaSala.append(s)
                        break
        # dobijamo listu svih sala sa trazemi, terminom, nastavak posle dorucka :)
        sst = []
        for ls in listaSala:
            ss = Sala.objects.get(ids=ls[0])
            sst.append(ss)
        # nisam glup, idemoooo!
        context = {
            'terminPolje': idPolja,
            'tim': timUpis,
            'saleSaTerminom': sst,
            'hiddenforma6': ProslediForma6(),
        }
        return render(request, 'test.html', context)
    return render(request, 'kalendar.html')

#poziv na utakmicu sa protivnicima slicnog kvaliteta
@login_required(login_url='login')
def rival(request):
    forma = ProslediForma3(data=request.POST or None)
    if forma.is_valid():
        stringic3 = forma.cleaned_data['skriveno3']
        lista1 = stringic3.split(", ")
        idTIma = int(lista1[0])
        lista1.pop(0)
        idPolja = lista1[0]
        timUpis = Tim.objects.get(idt=idTIma)

        protivnici = Tim.objects.all().exclude(idt=idTIma).values_list()
        listaProtvnika = []
        for prot in protivnici:
            provere = prot[4]
            if (provere != None):
                terminiProtivnika = prot[4].split(", ")
                for tp in terminiProtivnika:
                    if (tp == idPolja):
                        listaProtvnika.append(prot)
                        break
        # dobijamo listu svih sala sa trazemi, terminom, nastavak posle dorucka :)
        sst = []
        for lp in listaProtvnika:
            ss = Tim.objects.get(idt=lp[0])
            sst.append(ss)
        # nisam glup, idemoooo!
        context = {
            'terminPolje': idPolja,
            'tim': timUpis,
            'rivali': sst,
            'hiddenforma': ProslediForma3(),

        }
        return render(request, 'rival.html', context)
    return render(request, 'kalendar.html')

#ponude sala u zakazivanju treninga
@login_required(login_url='login')
def soloZakazan(request):
    forma = ProslediForma6(data=request.POST or None)
    if forma.is_valid():
        stringic6 = forma.cleaned_data['skriveno6']
        lista1 = stringic6.split(", ")
        tim1 = Tim.objects.get(idt=lista1[1])
        sala1 = Sala.objects.get(ids=lista1[0])
        daumIvreme = lista1[2].split(":")
        if (int(daumIvreme[1]) < 10):
            daumIvreme[1] = "0" + daumIvreme[1]
        listaObrisi = sala1.slobodnitermini.split(", ")
        stringNeObrisanih = ""
        listaObrisi.pop()

        # brise termin za sale
        for lo in listaObrisi:
            if (lo == lista1[2]):
                continue
            else:
                stringNeObrisanih = stringNeObrisanih + lo + ", "
        sala1.slobodnitermini = stringNeObrisanih;
        sala1.save()

        # brise termin za tim
        listaObrisi = tim1.presektermina.split(", ")
        stringNeObrisanih = ""
        listaObrisi.pop()

        # brise termin za tim
        for lo in listaObrisi:
            if (lo == lista1[2]):
                continue
            else:
                stringNeObrisanih = stringNeObrisanih + lo + ", "
        tim1.presektermina = stringNeObrisanih
        tim1.save()

        # brise termine za igrace iz tima
        prip = Pripada2.objects.all().filter(idt=tim1).values_list()
        igraciSvi = []
        for p in prip:
            igraciSvi.append(p[2])
        fudbaleri = []
        for iS in igraciSvi:
            fudbaleri.append(Igrac.objects.get(username=iS))
        for f in fudbaleri:
            listaTerm = f.termini.split(", ")
            listaTerm.pop()
            sTerm = ""
            for luton in listaTerm:
                if (luton == lista1[2]):
                    continue
                else:
                    sTerm = sTerm + luton + ", "
            f.termini = sTerm
            f.save()
        daumIvreme[1] = daumIvreme[1] + ":00:00"
        tekma = TerminUtakmice()
        tekma.idt1 = tim1
        tekma.idt2 = tim1
        tekma.ids = sala1
        tekma.cena = sala1.cenovnik
        tekma.vreme = daumIvreme[1]
        tekma.placen = 0
        tekma.save()
        return redirect('pocetna_stranica_igraca.html')
    return redirect('pocetna_stranica_igraca.html')


@login_required(login_url='login')
def accepted1(request):
    forma = ProslediForma7(data=request.POST or None)
    if forma.is_valid():
        stringonja7 = forma.cleaned_data['skriveno7']
        intS = int(stringonja7)
        poruka = PorukeIgraca.objects.get(idp=intS)
        userUlazi = poruka.idi2
        timUlaz = poruka.idt1
        pripadaTU = Pripada2()
        pripadaTU.uplata = 0
        pripadaTU.idt = timUlaz
        pripadaTU.idk = userUlazi
        pripadaTU.save()
        poruka.delete()
        return redirect('pocetna_stranica_igraca.html')
    return redirect('pocetna_stranica_igraca.html')

#odbijena poruka
@login_required(login_url='login')
def denied(request):
    forma = ProslediForma8(data=request.POST or None)
    if forma.is_valid():
        stringonja8 = forma.cleaned_data['skriveno8']
        intS = int(stringonja8)
        poruka = PorukeIgraca.objects.get(idp=intS)
        poruka.delete()
        return redirect('pocetna_stranica_igraca.html')
    return redirect('pocetna_stranica_igraca.html')

#prihvacena poruka tipa 2(utakmica)
@login_required(login_url='login')
def accepted2(request):
    forma = ProslediForma7(data=request.POST or None)
    if forma.is_valid():
        stringonja7 = forma.cleaned_data['skriveno7']
        intS = int(stringonja7)
        poruka = PorukeIgraca.objects.get(idp=intS)
        izazivac = poruka.idi1
        izazivacTim = poruka.idt1
        protivnik = poruka.idi2
        protivnik = poruka.idt2
        terminTekme = poruka.termin

        sale = Sala.objects.all().values_list()
        listaSala = []
        for s in sale:
            provere = s[2]
            if (provere != None):
                terminiSale = s[2].split(", ")
                for ts in terminiSale:
                    if (ts == terminTekme):
                        listaSala.append(s)
                        break
        # dobijamo listu svih sala sa trazemi, terminom, nastavak posle vecere :):)
        sst = []
        for ls in listaSala:
            ss = Sala.objects.get(ids=ls[0])
            sst.append(ss)
        # nisam glup, idemoooo! Ovde sam cak i brzi i bolji B)
        context = {
            'poruka': poruka,
            'saleSaTerminom': sst,
            'hiddenforma6': ProslediForma6(),
        }

        # pripadaTU.save()
        # poruka.delete()

        return render(request, 'test2.html', context)
    return render(request, 'pocetna_stranica_igraca.html')

#prihvacena poruka tipa 1(poziv u tim)

@login_required(login_url='login')
def reqToJoin(request):
    forma = ProslediForma(data=request.POST or None)
    if forma.is_valid():
        stringonja = forma.cleaned_data['skriveno']
        s = stringonja.split(", ")
        timID = int(s[0])
        userID = s[1]
        poruka = PorukeIgraca()
        timUpis = Tim.objects.get(idt=timID)
        userUpis = Igrac.objects.get(username=userID)
        poruka.idi1 = timUpis.idk_c_field
        poruka.idi2 = userUpis
        poruka.idt1 = timUpis
        poruka.tip = 3
        poruka.save()
        return redirect('pocetna_stranica_igraca.html')
    return redirect('pocetna_stranica_igraca.html')

#upis u bazu utakmice nakon zakazivanja
@login_required(login_url='login')
def organizujMec(request):
    forma = ProslediForma3(data=request.POST or None)
    if forma.is_valid():
        stringonja3 = forma.cleaned_data['skriveno3']
        listaStr = stringonja3.split(", ")
        porucica = PorukeIgraca()
        porucica.idi1 = Igrac.objects.get(username=listaStr[2])
        porucica.idi2 = Igrac.objects.get(username=listaStr[0])
        porucica.idt1 = Tim.objects.get(idt=listaStr[3])
        porucica.idt2 = Tim.objects.get(idt=listaStr[1])
        porucica.tip = 2
        porucica.termin = listaStr[4]
        porucica.save()
        return redirect('pocetna_stranica_igraca.html')
    return redirect('pocetna_stranica_igraca.html')

#zakazivanje utakmice sa rivalom
@login_required(login_url='login')
def duoZakazan(request):
    #prikupljanje podataka
    forma = ProslediForma6(data=request.POST or None)
    if forma.is_valid():
        stringic6 = forma.cleaned_data['skriveno6']
        lista1 = stringic6.split(", ")
        tim1 = Tim.objects.get(idt=lista1[1])
        sala1 = Sala.objects.get(ids=lista1[0])
        tim2 = Tim.objects.get(idt=lista1[3])
        ig1 = Igrac.objects.get(username=lista1[4])
        ig2 = Igrac.objects.get(username=lista1[5])
        poruka = PorukeIgraca.objects.get(idp=lista1[6])
        daumIvreme = lista1[2].split(":")
        if (int(daumIvreme[1]) < 10):
            daumIvreme[1] = "0" + daumIvreme[1]
        listaObrisi = sala1.slobodnitermini.split(", ")
        stringNeObrisanih = ""
        listaObrisi.pop()

        # brise termin za sale
        for lo in listaObrisi:
            if (lo == lista1[2]):
                continue
            else:
                stringNeObrisanih = stringNeObrisanih + lo + ", "
        sala1.slobodnitermini = stringNeObrisanih;
        sala1.save()

        # brise termin za tim
        listaObrisi = tim1.presektermina.split(", ")
        stringNeObrisanih = ""
        listaObrisi.pop()

        # brise termin za tim
        for lo in listaObrisi:
            if (lo == lista1[2]):
                continue
            else:
                stringNeObrisanih = stringNeObrisanih + lo + ", "
        tim1.presektermina = stringNeObrisanih
        tim1.save()

        # brise termine za igrace iz tima
        prip = Pripada2.objects.all().filter(idt=tim1).values_list()
        igraciSvi = []
        for p in prip:
            igraciSvi.append(p[2])
        fudbaleri = []
        for iS in igraciSvi:
            fudbaleri.append(Igrac.objects.get(username=iS))
        for f in fudbaleri:
            listaTerm = f.termini.split(", ")
            listaTerm.pop()
            sTerm = ""
            for luton in listaTerm:
                if (luton == lista1[2]):
                    continue
                else:
                    sTerm = sTerm + luton + ", "
            f.termini = sTerm
            f.save()

            # brise termin za tim2
            listaObrisi = tim2.presektermina.split(", ")
            stringNeObrisanih = ""
            listaObrisi.pop()

            # brise termin za tim2
            for lo in listaObrisi:
                if (lo == lista1[2]):
                    continue
                else:
                    stringNeObrisanih = stringNeObrisanih + lo + ", "
            tim2.presektermina = stringNeObrisanih
            tim2.save()

            # brise termine za igrace iz tima2
            prip = Pripada2.objects.all().filter(idt=tim2).values_list()
            igraciSvi = []
            for p in prip:
                igraciSvi.append(p[2])
            fudbaleri = []
            for iS in igraciSvi:
                fudbaleri.append(Igrac.objects.get(username=iS))
            for f in fudbaleri:
                listaTerm = f.termini.split(", ")
                listaTerm.pop()
                sTerm = ""
                for luton in listaTerm:
                    if (luton == lista1[2]):
                        continue
                    else:
                        sTerm = sTerm + luton + ", "
                f.termini = sTerm
                f.save()

        #generisanje i pamcenje tekme
        daumIvreme[1] = daumIvreme[1] + ":00:00"
        tekma = TerminUtakmice()
        tekma.idt1 = tim1
        tekma.idt2 = tim2
        tekma.ids = sala1
        tekma.cena = sala1.cenovnik
        tekma.vreme = daumIvreme[1]
        tekma.placen = 0
        tekma.dan = daumIvreme[0]
        tekma.save()

        poruka.delete()

        #generisanje i slanje notifikacije timovma(igracima timova)
        poruka4 = PorukeIgraca()
        poruka4.tip = 4
        poruka4.idi1 = ig2
        poruka4.idi2 = ig1
        poruka4.idt1 = tim2
        poruka4.idt2 = tim1
        poruka4.save()

        #generisanje i slanje notifikacije vlasnicima sala da su im terminin uplaceni za odredjeni dogadjaj
        porukaSali = Poruke()
        porukaSali.idk1 = ig2
        porukaSali.idk2 = sala1.idk
        porukaSali.idk3 = ig1
        porukaSali.ids = sala1
        porukaSali.tip = 4
        porukaSali.termin = lista1[2]
        porukaSali.save()
        return redirect('pocetna_stranica_igraca.html')
    return redirect('pocetna_stranica_igraca.html')

#brisanje poruke nakon citanja
@login_required(login_url='login')
def noted(request):
    forma = ProslediForma8(data=request.POST or None)
    if forma.is_valid():
        stringonja8 = forma.cleaned_data['skriveno8']
        intS = int(stringonja8)
        poruka = Poruke.objects.get(idp=intS)
        poruka.delete()
        return redirect('pocetna_stranica_igraca.html')
    return redirect('pocetna_stranica_igraca.html')

#uplata igraca na racun tima
@login_required(login_url='login')
def uplatiTimu(request):
    forma = ProslediForma9(data=request.POST or None)
    if forma.is_valid():
        stringonja9 = forma.cleaned_data['skriveno9']
        s = stringonja9.split(", ")
        tim = Tim.objects.get(idt=int(s[0]))
        upl = Pripada2.objects.get(idk=request.user.username, idt=tim)
        upl.uplata += int(s[1])

        rac = RacunTima.objects.get(idt=tim)
        rac.stanje += int(s[1])

        upl.save()
        rac.save()
        return redirect('pocetna_stranica_igraca.html')
    return redirect('pocetna_stranica_igraca.html')

#uplata termina na racun vlasnila(pendng dok obe ekipe ne uplate)
@login_required(login_url='login')
def uplatiSalu(request):
    forma = ProslediForma2(data=request.POST or None)
    if forma.is_valid():
        #prikupljanje podataka
        stringonja = forma.cleaned_data['skriveno2']
        lista = stringonja.split(", ")
        idT = int(lista[1])
        idTerm = int(lista[2])
        placane = int(lista[0])
        termin = TerminUtakmice.objects.get(idtr=idTerm)
        timce = Tim.objects.get(idt=idT)
        racunce = RacunTima.objects.get(idt=timce)
        sala = termin.ids
        vlasnikSale = sala.idk
        if placane != 3:
            if racunce.stanje >= termin.cena:
                #uplata vrednosti od strane tima
                racunce.stanje = racunce.stanje - termin.cena
                termin.placen += placane
                termin.save()
                racunce.save()
            else:
                #negativan odgovor(neuspesan zahtev)
                por = PorukeIgraca()
                por.idi1 = Igrac.objects.get(username=request.user.username)
                por.idi2 = Igrac.objects.get(username=request.user.username)
                por.tip = 6
                por.save()

        else:
            if racunce.stanje >= (termin.cena / 2):
                #uplata pola vrednosti od strane jednog tima
                racunce.stanje = racunce.stanje - (termin.cena / 2)
                termin.placen += placane
                termin.save()
                racunce.save()
            else:
                #negativan odgovor(neuspesan zahtev)
                por = PorukeIgraca()
                por.idi1 = Igrac.objects.get(username=request.user.username)
                por.idi2 = Igrac.objects.get(username=request.user.username)
                por.tip = 6
                por.save()


        if termin.placen == 3:
            #uplata vlasniiku nakon pendinga
            vlasnikSale.stanjeracuna += termin.cena
            vlasnikSale.save()
        return redirect('pocetna_stranica_igraca.html')
    return redirect('pocetna_stranica_igraca.html')

#kapiten salje poziv novom igracu da im se pridruzi
@login_required(login_url='login')
def newPlayer(request):
    forma = ProslediForma10(data=request.POST or None)
    if forma.is_valid():
#proveri da li je igrac vec u timu

        try:
            idIgr = Igrac.objects.get(username=forma.cleaned_data['vidljivo10'])
            pom =  Pripada2.objects.all().filter(idk=idIgr, idt=Tim.objects.get(idt=int(forma.cleaned_data['skriveno10'])))
            if len(pom)==0:
                por = PorukeIgraca()
                por.idi1 = Igrac.objects.get(username=request.user.username)
                por.idi2 = idIgr
                por.idt1 = Tim.objects.get(idt=int(forma.cleaned_data['skriveno10']))
                por.tip = 1
                por.save()
        except:
            por = PorukeIgraca()
            por.idi1 = Igrac.objects.get(username=request.user.username)
            por.idi2 = Igrac.objects.get(username=request.user.username)
            por.tip = 5
            por.save()
        return redirect('pocetna_stranica_igraca.html')
    return redirect('pocetna_stranica_igraca.html')

#brisanje poruke nakon citanja
@login_required(login_url='login')
def noted2(request):
    forma = ProslediForma8(data=request.POST or None)
    if forma.is_valid():
        stringonja8 = forma.cleaned_data['skriveno8']
        intS = int(stringonja8)
        poruka = PorukeIgraca.objects.get(idp=intS)
        poruka.delete()
        return redirect('pocetna_stranica_igraca.html')
    return redirect('pocetna_stranica_igraca.html')