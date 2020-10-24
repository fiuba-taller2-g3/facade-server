FROM python:latest
COPY ./app.py .
RUN pip install gunicorn
RUN pip install Flask
EXPOSE $PORT
CMD gunicorn app:app
