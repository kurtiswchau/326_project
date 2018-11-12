# 12 Creating Our Homepage

## Installing Django

To run any of the examples this class you need to make sure Django is
installed. To do this you must run the following command to install
Django:

```bash
$ pip3 install django
```

## Installing Faker

[Faker](https://faker.readthedocs.io/en/latest/index.html) is a Python
library that is used to generate "fake" data. This is tremendously
helpful for building applications that require some data for
testing. To use the example code, you must install Faker:

```bash
$ pip3 install faker
```

## Initializing the Database

This class covers relational databases and modeling. We also include
some additional scripts that make adding mock data to the database
easier. In particular, we include an [`init.py`](locallibrary/init.py)
script that demonstrates how you can add data to the database
programmatically. This script can be easily invoked from that
directory with the following command:

```bash
$ python3 manage.py shell < init.py
```

We use the `manage.py` script provided by Django to ensure that the
Django environment is setup correctly. We use the `<` redirection
operator to redirect standard input of Django's shell from the
`init.py` file. Note, you can easily execute any of the commands found
in the `init.py` file by invoking the shell and typing them in
manually:

```bash
$ python3 manage.py shell
>>> from catalog.models import Genre, Book, BookInstance, Author
>>> genre = Genre(name='Science Fiction')
```

This is a great way to explore your data model interactively. In
addition to `init.py`, we have also included an
[`init.sh`](locallibrary/init.sh) script. This is a helper script that
will recreate the database when it is invoked from the command like
so:

```bash
$ ./init.sh
```

## Super User Creation

We have extended the `init.py` script to create a superuser account in
Django. The superuser account allows you to access the admin site with
the generated username and password. See `init.py` for more details.

## Running Django

To run the examples in your programming environment first `cd` into
one of the Django projects and run the following:

```bash
$ python3 manage.py runserver 0.0.0.0:8080
```

We use the IP address designation `0.0.0.0` to tell Django to bind
or listen on all IP addresses that the computer supports. If you
do not provide this you will not be able to send HTTP requests to
Django running in the class programming environment VM. Take a
look at [this StackOverflow post](https://stackoverflow.com/questions/1621457/about-ip-0-0-0-0-in-django).

Next, you need to contact the HTTP server using an HTTP client. You
can easily test this from the command line:

```bash
$ curl http://localhost:8080
```

Alternatively, and perhaps more interesting, you can open a browser on
your host operating system and navigate to http://localhost:8080. We
recommend using chrome, however, any browser should work. The HTTP
request will be sent to your localhost and port. We have mapped port
8080 on your host operating system to port 8080 in your virtual
machine environment.

[so_01]: https://stackoverflow.com/questions/7354588/django-charfield-vs-textfield

[models_01]: https://docs.djangoproject.com/en/2.1/topics/db/models
[mdn_01]: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models#Model_primer
[mdn_02]: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models#Model_management