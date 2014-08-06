minimum-viable-django
=====================

The smallest possible (useful) Django project skeleton. Customised to my own
taste.


To use this project follow these steps:

#. Create your working environment
#. Install Django
#. Create the new project using the minimum-viable-django template
#. Set up the database
#. Install additional dependencies
#. Use the Django admin to create the project (`python {{ project_name}}/manage.py startapp`)
#. Run the Django server


Working Environment
===================

These are the dependencies which you need to have available in your global
environment, before you set up the project:

- `virtualenvwrapper`
- `autoenv`
- Postgres


Set up a Virtualenv with `virtualenvwrapper`
----------------------------------------------

In Linux and Mac OSX, you can install virtualenvwrapper (http://virtualenvwrapper.readthedocs.org/en/latest/),
which will take care of managing your virtual environments and adding the
project path to the `site-directory` for you:

    $ mkdir PROJECT_NAME
    $ mkvirtualenv -a PROJECT_NAME -p $(which python3) ENVNAME
    $ pip install django
    $ django-admin.py startproject --template=https://github.com/jeffbr13/minimum-viable-django/archive/master.zip --extension=py,rst,html --name=.env PROJECT_NAME ./


Installing Project Dependencies
===============================

Depending on where you are installing dependencies:

In development::

    $ pip install -r requirements/local.txt

For production::

    $ pip install -r requirements.txt

*note: We install production requirements this way because many Platforms as a
Services expect a requirements.txt file in the root of projects.*


Database Setup
==============

Skip this step if you already have a database setup or preconfigured.

    $ createdb PROJECT_NAME


Configure Django Settings
=========================

#. Set `DATABASE_USER` and `DATABASE_PASSWORD` in `.env`
#. Set `Admins` in `base.py`
#. Configure production settings
  #. `ALLOWED_HOSTS`
  #. Email SMTP settings


Run Server
==========

    $ honcho start

Acknowledgements
================

- This project follows best practices as espoused in [Two Scoops of Django: Best Practices for Django 1.6](http://twoscoopspress.org/products/two-scoops-of-django-1-6).
