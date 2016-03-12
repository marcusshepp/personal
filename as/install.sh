BASEPACKAGELIST="python-dev nginx python-pip python-virtualenv"

sudo apt-get upgrade
sudo apt-get update
sudo apt-get install $BASEPACKAGELIST

sudo mkdir /opt/envs/
sudo virtualenv /opt/envs/personal
source /opt/envs/personal/bin/activate

pip install django
pip install gunicorn

sudo mv -f /home/ubuntu/personal /opt/personal

cd /opt/personal/
