#!/bin/bash

sudo apt-get update

sudo apt-get -y install build-essential
sudo apt-get -y install libsqlite3-dev
sudo apt-get -y install sqlite3
sudo apt-get -y install bzip2 libbz2-dev

wget https://www.python.org/ftp/python/3.4.3/Python-3.4.3.tar.xz
tar xJf ./Python-3.4.3.tar.xz
cd ./Python-3.4.3
./configure --prefix=/opt/python3.4
make && sudo make install
cd ..

sudo apt-get -y install python3-pip
sudo pip3 install -r requirements.txt

cd polyclinic/
python3.4 manage.py makemigrations
python3.4 manage.py migrate
sudo python3.4 manage.py runserver 0.0.0.0:80
