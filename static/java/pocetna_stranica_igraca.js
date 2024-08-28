//otvaranje odgoarajuceg popup prozora
function openPopup() {
  document.getElementById("myPopup").style.display = "block";
   }
      function openPopup1() {
  document.getElementById("myPopup1").style.display = "block";
   }
   function openPopup2() {
  document.getElementById("myPopupPorukePoslate").style.display = "block";
   }
      function openPopup3() {
  document.getElementById("myPopupPorukePrimljene").style.display = "block";
   }
   //zatvaranje odgoarajuceg popup prozora
function closePopup() {
  document.getElementById("myPopup").style.display = "none";
   }
   function closePopup1() {
  document.getElementById("myPopup1").style.display = "none";
   }
   function closePopup2() {
  document.getElementById("myPopupPorukePoslate").style.display = "none";
   }
   function closePopup3() {
  document.getElementById("myPopupPorukePrimljene").style.display = "none";
   }
   //globalne promenljive, ne dirati potrebna komunikacija medju funkcijama u ralicito vreme
    //smatrati maltene nitima i asinhronim pozivima, good luck, pitaj sta treba Scepana :)
var niz = ""
var termin1=""

//popunjavanje odgovarajucih delova kalendara igraca
function toggleAvailability(cell) {
    if (cell.classList.contains("available")) {
      cell.classList.remove("available");
      cell.classList.add("unavailable");
    } else {
      cell.classList.remove("unavailable");
      cell.classList.add("available");
    }
  }
//popunjavanje odgovarajucih delova kalendara tima
  function toggleAvailability2(cell) {
    if (cell.classList.contains("available1"))
    {
        document.getElementById("myPopup").style.display = "block";
        termin1 = cell.id;
        let x = cell.id.split(":");
        var d
        r = parseInt(x[1])+1 ;
        if(x[1].length==1)
        {
            y = "0"+x[1] +":00";
            x[1]= y;
            // alert(x[1]);
        }
        else
        {
            y = x[1] +":00";
            x[1]= y;
        }

        if(r<10)
        {
            y = "0"+r +":00";
            r= y;
            // alert(x[1]);
        }
        else
        {
            y = r +":00";
            r= y;
        }
         switch (x[0])
         {
            case 'PO':
                d = "Ponedeljak od " + x[1] + " do " + r;
                break;
            case 'UT':
                d = "Utorak od " + x[1] + " do " + r;
                break;
            case 'SR':
                d = "Sreda od " + x[1] + " do " + r;
                break;
            case 'CT':
                d = "Četvrtak od " + x[1] + " do " + r;
                break;
            case 'PT':
                d = "Petak od " + x[1] + " do " + r;
                break;
            case 'SU':
                d = "Subota od " + x[1] + " do " + r;
                break;
            case 'NE':
                d = "Nedelja od " + x[1] + " do " + r;
                break;

        }
        // alert(d);
        // return d;
        // document.getElementById("pSala").innerHTML = "Pretraga sala za termin u " + d;
        // document.getElementById("pTim").innerHTML = "Pretraga timova za termin u " + d;
        document.getElementById("naslov").innerHTML = d;
    }
  }

  //posalji funkcije su od 1 do tipa 12 sada vec, funkcije za prosledjivanje hidden podataka u views
  function posalji()
  {
      STRIG = isAvailable();
      $("#f1 #id_skriveno").val(STRIG);
  }
  //pise gore
    function posalji2(t)
  {
      $("#f2 #id_skriveno2").val(t);
  }
    //pise gore
   function posalji3(c)
  {
      let tC = c + ', '+ termin1 +', '+ niz;
      //alert(tC)
      $("#f3 #id_skriveno3").val(tC);
  }
  //pise gore
    function posalji4(tca)
  {
      $("#f4 #id_skriveno4").val(tca);
  }
  //pise gore
  function posalji5(sID)
  {
      STRIG5 = sID + ", "+isAvailable5();
      $("#f5 #id_skriveno5").val(STRIG5);
  }

    //pise gore
function posalji6(kk)
  {
      b=""
      b= kk
      $("#f6 #id_skriveno6").val(b);
  }
     //pise gore
 function posalji7(kk)
  {
      let b=""
      b= kk
      $("#f7 #id_skriveno7").val(b);
  }
    //pise gore
function posalji8(kk)
  {
      let b = ""
      b= kk
      $("#f8 #id_skriveno8").val(b);
  }
   //pise gore
 function posalji9(kk,u)
  {
      let b = ""
      b= kk+", "+u
      // alert(b)
      $("#f9 #id_skriveno9").val(b);
  }
  //trazi validne/slobodne datume, Max ovde zna vise obratiti se njemu ili Scepanu
  function isAvailable() {
    var stringonja = ""; let dan = "PO"


    for (let i = 8; i<23; i++) {
        for (let j = 0; j < 7; j++) {
            switch (j) {
                case 0:
                    dan = "PO:";
                    break;
                case 1:
                    dan = "UT:";
                    break;
                case 2:
                    dan = "SR:";
                    break;
                case 3:
                    dan = "CT:";
                    break;
                case 4:
                    dan = "PT:";
                    break;
                case 5:
                    dan = "SU:";
                    break;
                case 6:
                    dan = "NE:";
                    break;
            }

            let o = document.getElementById(dan + i + "");

            if (o.classList.contains("available")) {

                stringonja = stringonja + dan + i + ", ";
            }
        }
    }

    stringonja = stringonja+" ";
    return stringonja;
  }
//kale gospodar vremena ucitava podatke pri onload pozivu unutar stranice
function kale()
{
    let Kal = document.getElementById("hid").innerText;
    var lista = Kal.split(", ");
    lista.pop();
    for (let i = 0; i<lista.length;i++)
    {
        let o = document.getElementById(lista[i]);
        o.classList.remove("unavailable");
        o.classList.add("available");
    }
}

//kale1 isto kao i kale samo vise podataka za zahtevnije strane
function kale1()
{
    let Kal1 = document.getElementById("hid").innerText;
    // Kal1.slice(0, -1);
    // Kal1.slice(0, 1);
    var Kal = Kal1.replace("[", "")
    var Kal2 = Kal.replace("'", "")
    let listetina = Kal2.split(" '");
    var lis = Kal2.split(", ")
    var xx = [];
    for (let i=0;i<lis.length;i++)
    {
            if(lis[i].length<=2)
            {
                continue;
            }
            if(lis[i].charAt(0)=="'")
            {
                lis[i]=lis[i].slice(1);

            }
            let o = document.getElementById(lis[i]);

            if(o.innerText!="")
            {
                p = parseInt(o.innerText) +1;
                if(p>4)
                {
                    o.classList.add("available1");
                    o.classList.remove("unavailable1");
                    if(!xx.includes(lis[i]))
                    {
                        xx.push(lis[i]);
                    }

                }
                o.innerText=p+"";

            }
            else
            {

                o.innerHTML = "1";

            }
    }
    for (let j=0;j<xx.length;j++)
    {
        niz += xx[j];
        niz += ", "
    }
    niz = niz.slice(0,-1);
    niz = niz.slice(0,-1);

     //alert(niz);
    // document.getElementById("id_skriveno3").innerHTML = niz;
}



//pri pozivu trazenja ekipe poziva se ova funkcija sa sve alertom
function prosledi(q,x)
{
    let y = x.split(", ");
    // alert(y);
    let t = document.getElementById("hidac-"+q).innerText;
    let b = y[1]+", "+y[2];
    // alert(b);
    alert("Zahtev poslat, ekipa "+t+" će Vam brzo odgovoriti, nadamo se!");
    $("#f1 #id_skriveno").val(b);

}
//ucitavanje kalendara sala
function toggleAvailability3(cell) {
    if (cell.classList.contains("available3")) {
      cell.classList.remove("available3");
      cell.classList.add("unavailable3");
    } else {
      cell.classList.remove("unavailable3");
      cell.classList.add("available3");
    }
  }

  function isAvailable5() {
    var stringonja = ""; let dan = "PO"


    for (let i = 8; i<23; i++) {
        for (let j = 0; j < 7; j++) {
            switch (j) {
                case 0:
                    dan = "PO:";
                    break;
                case 1:
                    dan = "UT:";
                    break;
                case 2:
                    dan = "SR:";
                    break;
                case 3:
                    dan = "CT:";
                    break;
                case 4:
                    dan = "PT:";
                    break;
                case 5:
                    dan = "SU:";
                    break;
                case 6:
                    dan = "NE:";
                    break;
            }

            let o = document.getElementById(dan + i + "");

            if (o.classList.contains("available3")) {

                stringonja = stringonja + dan + i + ", ";
            }
        }
    }

    stringonja = stringonja+" ";
    return stringonja;
  }

  function kale2()
{
    let Kal = document.getElementById("hid5").innerText;
    var listaK2 = Kal.split(", ");
    // alert(listaK2);
    listaK2.pop();

    for (let i = 0; i<listaK2.length;i++)
    {
        let m = document.getElementById(listaK2[i]);
        m.classList.remove("unavailable3");
        m.classList.add("available3");
    }
}
//cisti sve u kalendaru sale, nije jos testirano moze da baci jednu AZ na bazu (apsolutno zlostavi bazu, poremeti je gore nego cipotle)
function brisisve(){
    let elem = document.querySelectorAll(".unavailable3")
    elem.forEach((e)=>{
        e.classList.add("available3");
        e.classList.remove("unavailable3");
        });
}

//funkcija za slanje poruke u bekend views
function posaljiProtivniku(kk)
{
  b=""
  b= kk
  // alert(b);
  $("#f3 #id_skriveno3").val(b);
}
//prosledjivanje uplata za sale u zadnji deo views
function uplataSale1(q,p,o){
    let b = ""
    b= q+", "+p+", "+o;
    // alert(b)
    $("#f2 #id_skriveno2").val(b);
}
//salje vrendnost iz forme za pretragu kapitena za nove clanove
function posalji10(a){
    let bx =""+a
    $("#f10 #id_skriveno10").val(bx);
}