===================
 My Metrics README
===================

This is a web application for tracking and displaying personal metrics.

Setup Dependencies
==================

1. Install virtualenv (http://www.virtualenv.org/en/latest/index.html#installation)
    a. ``easy_install virtualenv``
    b. ``virtualenv --no-site-packages <virtualenv dir>``
2. Install Pyramid (http://docs.pylonsproject.org/projects/pyramid/en/1.2-branch/narr/install.html)
    a. ``<virtualenv dir>/bin/easy_install pyramid``
3. Install Jinaj2 (http://jinja.pocoo.org/docs/intro/#installation)
    a. ``<virtualenv dir>/bin/easy_install Jinja2``
4. Install PostgreSQL (http://postgresapp.com/)
    a. May need to fix a library: ``cd /usr/lib``, ``sudo ln -s libpq.5.4.dylib libpq.5.dylib``
    b. (Optional) Add extras to PATH in .bashrc: ``export PATH="/Applications/Postgres.app/Contents/MacOS/bin:$PATH"``
    c. (Optional) Install pgAdmin3 (http://www.postgresql.org/ftp/pgadmin3/release/v1.14.3/osx/)
5. Install SQLAlchemy (http://docs.sqlalchemy.org/en/latest/intro.html#installation)
    a. ``<virtualenv dir>/bin/easy_install SQLAlchemy``
6. Install psycopg (http://initd.org/psycopg/install/)
    a. ``<virtualenv dir>/bin/easy_install psycopg2``
7. Install sqlalchemy-migrate  (http://sqlalchemy-migrate.readthedocs.org/en/v0.7.2/download.html)
    a. ``<virtualenv dir>/bin/easy_install sqlalchemy-migrate``
8. (Optional) Install Docutils (http://docutils.sourceforge.net/)
    a. ``<virtualenv dir>/bin/easy_install docutils``
    
Running Development Server
==========================

``<virtualenv dir>/bin/python main.py``

Running Development Database
============================

1. Start Postgres.app
2. Connect to Postgres:
    - Host: ``localhost``
    - Port: ``5432``
    - User: ``<your username>``

Setting Up a New Database
=========================

1. Add your database to migration repository (http://sqlalchemy-migrate.readthedocs.org/en/v0.7.2/versioning.html#version-control-a-database):
    a. ``<virtualenv dir>/bin/python migration_repo/manage.py version_control <database URL> migration_repo/``
2. Update ``manage_db.py`` to reflect your database settings
3. Upgrade to latest version:
    a. ``<virtualenv dir>/bin/python manage_db.py upgrade``