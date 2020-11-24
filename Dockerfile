FROM python:latest
RUN pip install gunicorn
RUN pip install Flask
RUN pip install requests
RUN pip install pyjwt

COPY . .
EXPOSE $PORT
CMD gunicorn app:app
