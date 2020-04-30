# Keskustelufoorumi

Tarkoituksena on luoda keskustelufoorumi tietokantojen harjoitustyökurssille. Käyttäjät voivat kirjautumisen jälkeen osallistua keskusteluun lukemalla ja lähettämällä viestejä. Viestit lähetetään keskustelijoiden näkökulmasta anonyymeinä. Viestit voidaan myös kohdistaa tiettyihin Aloituksiin. Sivulla on myös hakutoiminto. Ylläpitäjillä on oma alue keskustelufoorumin hallintaan.

[Herokulinkki](https://cryptic-temple-28944.herokuapp.com/login "cryptic-temple-28944.herokuapp.com")

Testitunnukset:
admin - admin
Rekisteröimällä uuden käyttäjän käyttäjätunnuksella admin, kyseinen tunnus saa ylläpito-oikeudet automaattisesti.

Toimintoja:

Kirjautuminen, Kirjoituksen lisääminen, Kirjoitusten näyttäminen eri kriteerein, Ryhmän jäsenen lisääminen, muokkaaminen ja poistaminen, Vastineen laatiminen ja muokkaus, Kirjoitusten poistaminen, Aiheiden määrittely, muokkaus ja poisto.

[User storyt ja niiden SQL-lauseet](../master/Dokumentaatio/UserStoryt.md)

[Asennusohje](../master/Dokumentaatio/Asennusohje.md)

[Käyttöohjeet](../master/Dokumentaatio/Käyttöohjeet.md)

[Create Table -lauseet](../master/Dokumentaatio/CreateTable-Lauseet.txt)

HUOM!
30.4. Herokun kanssa ilmeni erikoinen ongelma, jota en ole onnistunut selvittämään. Joidenkin toimintojen kohdalla Herokun SQLAlchemy on jotenkin solmussa eikä kaikki kyselyt mene läpi. Lokaalisti toimii ongelmitta:
Esim. Uuden aloituksen tekeminen päättyy Herokussa virheeseen: column answer.createdon does not exist (Mikä on tietysti väärin, koska sarakkeen nimi on createdOn) ja ohje antaakin HINT:  Perhaps you meant to reference the column "answer.createdOn".
Tosin kysely on kyllä koodissa oikein. Lokeihinkin tulostuu ajettu kysely ja muoto on myös siellä oikein:
[SQL: SELECT * FROM Answer WHERE (Answer.post_id = %(postId)s) ORDER BY answer.createdOn ASC]
Homma myös pelitti vielä muutama tunti aiemmin ongelmitta.


Jatkokehitysideoita:
 - Sovelluksen ulkonäkö jäi keskeneräiseksi ja olisi kaivannut siistimistä
 - Etusivulla lista uusimmista viesteistä ja suora linkki niihin
 - Mahdollisuus lisätä kuvaus alueille
 - Mahdollisuus liputtaa viestejä ja ylläpitäjilläe näkymä liputetuista viesteistä
 - "tykkäysmahdollisuus" viesteihin ja aloituksiin


Tietokantakaavio:


![alt text](https://github.com/Meemeimei/Keskustelufoorumi/blob/master/Dokumentaatio/0e73f6ec.png)
