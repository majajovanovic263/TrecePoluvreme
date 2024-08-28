
// function submitForm() {
//   var username = document.getElementById("username").value;
//   if (username == "vlasnik") {
//     window.location.href = "pocetna_stranica_vlasnika_prostora.html";
//   } else if (username == "igrac") {
//     window.location.href = "pocetna_stranica_igraca.html";
//   } else {
//     alert("Invalid username!");
//   }
// }

function proveriFormu(){
  var ime = document.getElementById("id_ime").value;
  var email = document.getElementById("id_email").value;
  var prezime = document.getElementById("id_prezime").value;
  var godiste = document.getElementById("id_godiste").value;
  var telefon = document.getElementById("id_telefon").value;
  var broj = document.getElementById("id_brojdresa").value;
  var pozicija = document.getElementById("id_pozicija").value;
  // if(ime == "" || ime.lenght <3)
  // {
  //   alert("Niste uneli ime");
  // }
  // if(prezime == "" || prezime.lenght <3)
  // {
  //   alert("Niste uneli prezime");
  // }
  // if(telefon == "" || prezime.lenght <3)
  // {
  //   alert("Niste uneli telefon");
  // }
  // if(godiste == "" || prezime.lenght <3)
  // {
  //   alert("Niste uneli godiste");
  // }
  // if(pozicija == "" || prezime.lenght <3)
  // {
  //   alert("Niste uneli pozicija");
  // }
  // if(broj == "" || prezime.lenght <3)
  // {
  //   alert("Niste uneli broj");
  // }
  if (!(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email)))
  {
    alert("Email nije validan")
  }
  if(pozicija<1 || pozicija>4)
  {
    alert("Za poziciju postavite broj izmedju 1 i 4 gde 1 označava golmana, 2 odbrambenog, 3 veznog, a 4 napadača");
  }
  if(broj<1 || broj>99)
  {
    alert("U fudbalu brojevi idu od 1 do 99");
  }

}
function proveriFormu2() {

  var email = document.getElementById("id_email").value;
  if (!(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email)))
  {
    alert("Email nije validan")
  }
}


