# letusorderit

Gemeinsam bestellen von Dingen und Essen mit dieser modernen Internettechnologie

Plan: plans.md

Domain: http://letusorder.it/


## Installationsanleitung:

### virtualenv einrichen

(mit virtualenvwrapper)

``mkvirtualenv letusorderit -p /usr/bin/python3``

### Pakete installieren

```pip install -r requirements.txt```


## Mit Docker und fig ausführen (development umgebung)

### Setup

* Installiere docker und fig ([Instructions](http://www.fig.sh/install.html))
* `fig up -d`
* warten
* falls noch keine datenbank existiert: `fig run web python3 manage.py migrate`
