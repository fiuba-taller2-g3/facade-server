# facade-server

local:
sudo docker build . -t facade-image
sudo docker run --name facade-server -d -e PORT=5432 -p 5433:5432 facade-image

heroku:
https://frozen-basin-86298.herokuapp.com/
frozen-basin-86298
