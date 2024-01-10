# Defines the base image to use
FROM python:3.10-alpine

# Setup python environment variables
# Python won’t try to write .pyc files on the import of source modules
ENV PYTHONDONTWRITEBYTECODE 1
# Non-empty buffer to show the output of the app in real time
ENV PYTHONUNBUFFERED 1

# Ensure latest pip and run pip commands as user
RUN pip install --upgrade pip

RUN adduser -D myuser
USER myuser
WORKDIR /home/myuser
ENV PATH "$PATH:/home/myuser/.local/bin"

# Configure Django environment variables
ENV SECRET_KEY $SECRET_KEY
ENV DEBUG $DEBUG
ENV SENTRY_DSN $SENTRY_DSN
ENV ALLOWED_HOSTS $ALLOWED_HOSTS

# Install dependencies and copy the application files
COPY --chown=myuser:myuser requirements.txt requirements.txt
RUN pip install --user --no-cache-dir -r requirements.txt
COPY --chown=myuser:myuser . .

# Exposing a port
EXPOSE 8000

# Run Django server after collecting static files
CMD python3 manage.py collectstatic --noinput && python3 manage.py runserver 0.0.0.0:8000
