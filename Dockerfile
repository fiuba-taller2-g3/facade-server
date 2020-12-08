FROM python:latest
RUN pip install gunicorn
RUN pip install Flask
RUN pip install -U flask-cors
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE $PORT
CMD gunicorn app:app
