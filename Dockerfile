FROM python:latest
COPY ./users_service.py .
COPY authorization_service.py .
COPY ./app.py .
RUN pip install gunicorn
RUN pip install Flask
RUN pip install requests
RUN pip install pyjwt
EXPOSE $PORT
CMD gunicorn app:app
