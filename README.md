# Matchmaker

A very simple [Django](https://www.djangoproject.com/) web app for tracking match game scores as a demo for [Django REST Framework](https://www.django-rest-framework.org/) use.

## Requirements

You will need docker and docker-compose installed in your system.

## Installation

First build containers

```bash
$ docker-compose build
```

Then run bootstrap

```bash
$ docker-compose run backend bootstrap
```

## Running & Development

Run docker-compose

```bash
$ docker-compose up
```

Go to browser under `http://localhost/`

You can start playing around.
