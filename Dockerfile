FROM python:latest
COPY ./app.py .
RUN pip install gunicorn
RUN pip install Flask
RUN pip install requests
EXPOSE $PORT
CMD gunicorn app:app
