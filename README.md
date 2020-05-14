# Django Project to Access a Public API

In this repo you will find a small Django application that accesses the [PokéAPI](https://pokeapi.co) and communicates with it via REST. To comply with the guidelines of this public API, the data is stored in a local database and is accessed from there when the page is accessed.
The purpose behind this is to compare the procedure of creating a page with Flask and Django. The same application (only created with Flask), you can find in my other repo: https://github.com/sj-192277/pa_hofmeister_flask_public_api

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Needless to say you need to install [Python](https://www.python.org)

Due to Python venv (Virtual Environment) there is no need for any prerequisites. Just Pull this Repo and start it within your IDE. If there should be any reason, why you want to start it in your CLI, you need to activate venv with the following command.

```
.\venv\Scripts\activate
```

More Information about Python [Virtual Environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

### Installing

To start the lokal debug server you need to excecute the following command in your IDE terminal or CLI

```
manage.py runserver
```

The Flask app should be now running on http://127.0.0.1:8000/ 

## Built With

* [Django](https://www.djangoproject.com) - The web framework used
* [Requests](https://requests.readthedocs.io/en/master/) - HTTP library for Python
* [PokéAPI](https://pokeapi.co) - Public API used to obtain data
* [Bootstrap](https://getbootstrap.com) - Used to have nice Styling :)
* [Mathfilters](https://github.com/dbrgn/django-mathfilters) - Provides a set of simple math filters for Django.
