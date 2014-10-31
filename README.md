letusorderit
============

Gemeinsam bestellen von Dingen und Essen mit dieser modernen Internettechnologie
==================================================================================


Domain: http://letusorder.it/

Technischer Foo
---------------

* sessionbasiert
* Name der Session und Shop-URL beim Öffnen festlegen / angeben
* Preise pro Item angebbar
* Master/Eröffner kann editieren
* rest-api als erste Version
* mehrere defaulttimeouts (pizza 30mins, reichelt 1 woche; usw.)
* dauer und nicht enddatum als feld
 * "Interface" wie bei at(1) oder find(1)?
* eröffnen auch über restapi. alles über restapi
* eröffner sollte einen account haben
* auth-tokens und nutzer
* emailadresse reicht vielleicht
* Als zweiter Schritt API-Konsumenten (IRC, Hipchat, ... siehe unten)
* API-Anbindung an venmo.com



Wir nehmen Django weil:
-----------------------

* allauth (optional, aber sinnvoll)
* Django-Rest-Framework
* haben wir schon 1000x gemacht
* Projekt braucht eine Datenbank


Ablauf für den Initiator
------------------------

* Start einer Session wird angefordert: 'lang' oder 'kurz' bzw 'Dauer' oder 'bis zum Zeitpunkt'
* der Initiator soll angeben können ob Mitbesteller einen Account haben sollen
- Account im Sinne von Erreichbarkeit z.B. per E-Mail, damit ausstehende Zahlungen eingefordert oder der Eingang der Items mitgeteilt werden kann
* Als Antwort kommen 2 IDs oder auch gleich URLs:
 * die 'private' URL zur Verwaltung der Session
 * die 'public' URL zur Weitergabe an Mitbesteller
* Für den initiator wird aufgebaut eine nach Mitbestellern gruppierte Liste von Items mit Anzahl, Einzelpreis, Zwischensummen und Endsummen (je Mitbesteller und Gesamtbestellung)
* Nach Ende der Session kann der Initiator markieren, welcher Mitbesteller zu welchem Grad bezahlt hat
 * "user@example.com 19.00 EUR" (hat 19 EUR der ausstehenden Forderung beglichen) oder "user@example.com complete" (hat alle Forderungen beglichen)
* Mitbesteller mit Ausständen können abgerufen werde (Höhe des Austands wird ebenfalls angezeigt)
* Registrierte Initiatoren können alle ihre Sessions einsehen (aktive, laufende; abgelaufene; abgeschlossene)
 * Für laufende Sessions können die public/private-URLs abgerufen werden
* Der Initiator kann eine Liste aller Items abrufen und einzelne Items aus der Session entfernen


Ablauf für Mitbesteller
-----------------------

* Bekommen irgendwie die 'public' URL mitgeteilt
* GET auf die URL gibt an Wo bestellt wird (z.b. die shopurl)
 * ggfs registriert oder authentifiziert sich der Mitbesteller
 * hat der Mitbesteller keinen Account muss er bei jeder Interaktion eine E-Mailadresse angeben
* Mithilfe der Session-URL (die public URL des Initiators) kann ein Item mit seinem Preis der gemeinsamen Bestellsession hinzugefügt werden; dies lässt sich mehrfach machen
 * z.B. "3x 7555; 2.23 EUR" was bedeutet "dreimal das Item '7555' zu einem Einzelpreis von EUR 2.23", was wiederum bedeutet, dass der Endpreis für diesen Vorgang bei 3 * 2.23 EUR also 6.69 EUR liegt
* Wurde ein Item erfolgreich hinzugefügt wird als Antwort eine sog. Löschen-URL ausgegeben, mit der die Bestellung dieses Items zurückgezogen werden kann. Nach Ablauf der Sammelbestellungssession werden diese URLs ungültig


Kooperationsplan
----------------

* Wir machen das als Projekt für den Python-Workshop; mit Neulingen oder -gierigen als Zielgruppe
* soll zusammen gemacht werden. Also eigentlich keine Arbeiten ausserhalb des Workshops.


weitere Projekte
----------------

* irc-Anbindung
* HipChat-Anbindung
* EmberJS frontend
* AngularJS frontend
* Android / iOS / WinPhone / FirefoxOS
* Twitter-Anbindung
* text dialog client: http://sourceforge.net/projects/pythondialog/

