# facade-server

local:
sudo docker build . -t facade-image
sudo docker run --name facade-server -d -e PORT=5432 -p 5433:5432 facade-image

heroku develop:
https://facade-server-develop.herokuapp.com/
facade-server-develop


heroku production:
https://facade-server-production.herokuapp.com/
facade-server-production
