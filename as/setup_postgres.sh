sudo apt-get install libpq-dev python-dev
sudo apt-get install postgresql postgresql-contrib

# create user
sudo su - personal_webapp
createdb personal
createuser -P
psql
GRANT ALL PRIVILEGES ON DATABASE personal TO personal_webapp;
