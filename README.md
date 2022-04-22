# drf-api

API for articles and comments

## Setup

Clone the repository:

```sh
$ git clone https://github.com/CHAMPMOON/drf-api.git
$ cd drf-api/
```

Create a virtual environment:

```sh
$ python -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
````

Create .env file similar example.env:

```sh
$ cp example.env .env
````

Do Database migrations:

```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

Run development server:

```sh
$ python manage.py runserver
```

## Usage

Open `http://127.0.0.1:8000/docs/`


![image](https://user-images.githubusercontent.com/72620861/164618058-bc305825-0a61-4ee3-aafb-b7861ca4735c.png)


