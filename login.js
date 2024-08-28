// Benutzerdaten
const benutzer = [
    { benutzername: "cassa", passwort: "dollars", rolle: "cassa" },
    { benutzername: "TEST", passwort: "", rolle: "Platzchenshop" },   
    { benutzername: "Shop1", passwort: "Marmelade", rolle: "Shop1" },
    { benutzername: "Shop2", passwort: "Knarren", rolle: "Shop2" },
    { benutzername: "Shop3", passwort: "Koks", rolle: "Shop3" },
    { benutzername: "Shop4", passwort: "Polizia", rolle: "Shop4" },
    { benutzername: "Shop5", passwort: "Moin", rolle: "Shop5" },
    { benutzername: "Shop6", passwort: "Brandstifer", rolle: "Shop6" },
    { benutzername: "Shop7", passwort: "KriminellerMika", rolle: "Shop7" },
    { benutzername: "Hans", passwort: "Gunter", rolle: "Hansgunter" },

  ];


  
  // Funktion zum Überprüfen des Logins
  function login() {
    // Eingabe des Benutzernamens und des Passworts durch den Benutzer
    const benutzernameEingabe = document.getElementById("benutzername").value;
    const passwortEingabe = document.getElementById("passwort").value;
  
    // Überprüfung der Eingaben
    const benutzerdaten = benutzer.find(benutzer => benutzer.benutzername === benutzernameEingabe && benutzer.passwort === passwortEingabe);
  
    if (benutzerdaten) {
      // Wenn Benutzername und Passwort korrekt sind, wird der Benutzer eingeloggt
      
      if (benutzerdaten.rolle === "cassa") {
        window.location.assign("cassa.html"); // Weiterleitung zur cassa-Seite
      } else {
        window.location.assign("index.html"); // Weiterleitung zur allgemeinen Startseite
      }


if (benutzerdaten.benutzername === "KakaoShop") {

alert("hi")

}

    } else {
      
      
      
      // Andernfalls wird eine Fehlermeldung angezeigt
      console.log("Ungültige Anmeldedaten!");
     


       document.getElementById('error-message').classList.remove('hidden');

       setTimeout(function(){
        document.getElementById('error-message').classList.add('hidden');
       },5000);
       
     


    }
  }
  
  // Beispiel für die Verwendung von HTML-Formularelementen
  document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Verhindert das automatische Absenden des Formulars
    login(); // Ruft die Login-Funktion auf
  });