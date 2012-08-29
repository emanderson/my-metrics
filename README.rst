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
6. (Optional) Install Docutils (http://docutils.sourceforge.net/)
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
