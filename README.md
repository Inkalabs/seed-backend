### Inkalabs Backend Seed

This repository is intended for use as a base for new projects in Inkalabs.

It is meant to be used with https://bitbucket.org/inkalabsinc/seed-frontend as a single web application.

This project template includes the follwoing standards used in the company:

* Fabutils
* Environment Variables
* Django Rest
* Integration with frontend

In order to start your own project with this one as a base use the following command

```
$ django-admin.py startproject --template=https://github.com/Inkalabs/seed-backend/archive/master.zip mynewproject
```

Once this is done, you will need a .env file one directory before this one with the following structure:

```
DEBUG=on
SECRET_KEY=<your_key>
DATABASE_URL=psql://user@localhost:5432/db_name
ENVIRONMENTS={"dev": {"hosts": ["user@server.com"], "core_dir": "/var/www/somedir/", "gunicorn_pid": "/path/to/pid.pid", "gunicorn_server_socket": "127.0.0.1:9050", "gunicorn_user": "user", "is_production": false,  "is_staging": false, "domain_name": "my-domain", "token_logger": "getfromredmine", "branch": "master"}}
ALLOWED_HOSTS=localhost
```

Finally you will be able to run the project with all the standards in place.


This section of the readme is for you to edit in order to use your own project_name

# {{ project_name }}


## Installation
There is the complete list of packages required by the project
```
$ sudo apt-get install build-essential libssl-dev libffi-dev python-dev python python-virtualenv python-pip python3-venv libfreetype6 libfreetype6-dev pkg-config npm postgresql-client postgresql postgresql-contrib postgresql-server-dev-9.x git python3-dev
```

## Configure packages

### Postgres

```
$ sudo su postgres -c psql

postgres$ create user <user> with password '<password>';

postgres$ create database <database> owner <user> encoding 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';
```

#### Only for local purposes to use fabric

```
postgres$ alter user <user> with superuser;
```

Edit the `/etc/postgresql/9.x/main/pg_hba.conf` file as root user:

```
local all postgres trust

local all all trust
```

Restart the service

```
$ /etc/init.d/postgresql restart
```

## Configure the project
### Create a virtualenv

```
$ python3 -m venv {{ project_name }}
```

This command will create a new folder with the name `{{ project_name }}`

### Clone the project

First verify your SSH Keys on bitbucket configuration `https://bitbucket.org/account/user/<your_user>/ssh-keys/`
then if you dont have a key that points to your computer follow this tutorials:

* https://confluence.atlassian.com/bitbucketserver/creating-ssh-keys-776639788.html
* https://confluence.atlassian.com/bitbucket/add-an-ssh-key-to-an-account-302811853.html

```
$ git clone git@bitbucket.org:inkalabsinc/{{ project_name }}.git
```

### Activate your enviroment
Inside the `{{ project_name }}` folder run the following command

```
$ source bin/activate
```

After this you will see the virtualenv name in your prompt. i.e.:

```
({{ project_name }}) $
```

### Install requirements
```
({{ project_name }})$ cd {{ project_name }}-backend

({{ project_name }})$ pip install -r requirements.txt
```

### Setting up environment variables for project

Add the .env file like: https://redmine.fincite.net/projects/{{ project_name }}/wiki/Internal_information

### Run the project

Once you have everything ok, you can run the project.

```
({{ project_name }}) $ ./manage.py check

({{ project_name }}) $ ./manage.py migrate

({{ project_name }}) $ ./manage.py runserver
```
