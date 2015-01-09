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



## PRODUCTION

FIXME

```
docker pull nginx
docker pull aexea/aexea-base
docker run -d --name letusorderit-data -v /home/uid1000 aexea/aexea-base
docker build --tag=letusorderit-prod .
docker run -d --volumes-from letusorderit-data --name letusorderit letusorderit-prod
docker run --name letusorderit-nginx --volumes-from letusorderit-data --link letusorderit:letusorderit -p 8080:80 -v `pwd`/nginx.conf:/etc/nginx/nginx.conf -d nginx

```
