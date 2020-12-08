#!/bin/bash

sudo apt-get install python3-setuptools python3-dev build-essential virtualenv python3-pytest

#django-projects - postgresql
sudo apt-get install postgresql-client postgresql postgresql-contrib libpq-dev curl
#django-projects - pgadmin4
curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add
sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'
sudo apt install pgadmin4-desktop

rm -rf venv3/
virtualenv -p python3 venv3
source venv3/bin/activate
pip install -r requirements.txt
deactivate