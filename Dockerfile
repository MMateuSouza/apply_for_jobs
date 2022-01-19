# syntax=docker/dockerfile:1

FROM python:3.8-bullseye

WORKDIR /app

COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -e .

ENV FLASK_APP=${FLASK_APP}
ENV FLASK_ENV=${FLASK_ENV}
ENV FLASK_DEBUG=${FLASK_DEBUG}

EXPOSE 5000
CMD [ "flask", "run", "--host=0.0.0.0" ]
