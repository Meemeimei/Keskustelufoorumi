## Asennusohje

Sovelluksen kloonaaminen omalle koneelle onnistuu kätevästi Gitin avulla komennolla
  git clone https://github.com/Meemeimei/Keskustelufoorumi.git

Seuraavana navigoi kansioon ja asenna tarvittavat riippuvuudet
  source venv/bin/activate
  pip install -r requirements.txt

Voit suorittaa ohjelman ajamalla run.py tiedoston.
  run.py



Herokuun viemiseen tulee ensin luoda uusi Heroku-sovellus ajamalla sovelluksen juuressa
  heroku create

Jonka jälkeen sovelluksen voi lähettää Herokuun
  git push heroku master

Tämän jälkeen tietokanta tulee vielä virittää PostgreSQL-tietokannaksi komennoilla
  heroku config:set HEROKU=1
  heroku addons:add heroku-postgresql:database-dev
