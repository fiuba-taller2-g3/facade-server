# facade-server

local:
sudo docker build . -t facade-image
sudo docker run --name facade-server -d -e PORT=5432 -p 5433:5432 facade-image
