FROM aexea/aexea-base
MAINTAINER Stuttgart Python Interest Group

EXPOSE 8000

ADD . /opt/code
WORKDIR /opt/code
RUN pip3 install -Ur requirements.txt

# uid1000 is created in aexea-base
USER uid1000
WORKDIR letusorderit
