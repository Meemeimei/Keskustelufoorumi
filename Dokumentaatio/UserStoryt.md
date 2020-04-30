### User storyt

[x] Käyttäjänä haluan rekisteröityä foorumille
	INSERT INTO Account username, password, admin VALUES ...

[x] Käyttäjänä haluan voida kirjautua rekisteröimilläni tunnuksilla foorumille
	SELECT * FROM Account WHERE username = annettuKayttajatunnus AND password = annettuSalasana 

[x] Käyttäjänä haluan aloittaa keskusteluita foorumille
	INSERT INTO Post title, content VALUES ...

[x] Käyttäjänä haluan luoda uusia alueita
	INSERT INTO Area name, content VALUES ...

[x] Käyttäjänä haluan lisätä käyttäjiä ryhmiini
	INSERT INTO Groupuser group_id, user_id VALUES ...

[x] Käyttäjänä haluan nähdä ryhmäni aloitukset
	SELECT * FROM Posts WHERE group_id = halutunRyhmanId

[x] Käyttäjänä haluan vastata aloituksiin
	INSERT INTO Answer WHERE post_id = vastattavaAloitus

[x] Käyttäjänä haluan vaihtaa salasanaani tarvittaessa
	UPDATE Account SET password = uusiSalasana WHERE user_id = omaId

[x] Ylläpitäjänä haluan poistaa tunnuksia
	DELETE FROM Account Where user_id = poistettavanTunnuksenId

[x] Ylläpitäjänä haluan poistaa aiheita, ryhmiä ja viestejä
	DELETE FROM Area/Post/Group Where id = poistettavanId

[x] Ylläpitäjänä haluan tehdä käyttäjistä ylläpitäjiä
	UPDATE Account SET admin = True Where user_id = päivitettävänTunnuksenId
