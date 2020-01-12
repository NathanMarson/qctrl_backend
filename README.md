# qctrl_backend
My submission for the Q-CTRL Back-end Engineering challenge

## Requirements

Create a RESTful API using [Django](https://www.djangoproject.com/). The API should be backed by a [PostgreSQL](https://www.postgresql.org/) database, conform to the [JSON:API](https://jsonapi.org/) specification and should implement endpoints that provide the following functionality:

1. Create a new control
1. List all controls (five per page)
1. Get a specific control
1. Update a specific control
1. Delete a specific control
1. Bulk upload controls in CSV format
1. Download controls in CSV format

## Prerequisites

If you have not already, please install [Docker](https://docs.docker.com/v17.12/install/) and [PostgreSQL](https://www.postgresql.org/download/). Also, to easily create our python virtual environment we will use the virtualenv package.


```bash
pip install virtualenv
```

## Usage


### Installation
Firstly, lets clone the repository into a folder on our computer.

```bash
git clone https://github.com/NathanMarson/qctrl_backend project
```

This will clone our repo into the 'project' folder. Next, we will activate our virtual environment with these command.

```bash
virtualenv project
```

```bash
cd project
```

```bash
source scripts/activate
```

Or for mac:

```bash
source bin/activate
```

Now that we are running our virtual environment, lets install our package requirements.

```bash
pip install -r requirements.txt
```


### Setup
Lets set up our Docker container. Make sure that both Docker and PostgreSQL are running.

```bash
docker-compose up
```

Next, we will create the database that we want to use for our project. We will enter the psql terminal with the following command.

```bash
psql -U postgres
```

Once you have entered the terminal, we will use the following commands to create the database and a user.

```
CREATE DATABASE controls;
```
```
CREATE USER admin SUPERUSER PASSWORD 'password';
```
```
GRANT ALL PRIVILEGES ON DATABASE controls TO admin;
```
```
\q
```

The final step is for us to migrate the database to make sure it will work with out Django API (make sure you are back in your virtual environment).

```bash
python manage.py migrate
```


### Running

Now that we have set up everything that we need, we can run our Django API.

```bash
python manage.py runserver 0.0.0.0:8100
```

Now, when we navigate to http://localhost:8100/api/control/ we will see the list of controls with an interface to create new ones.

To select a specific control to edit or delete, navigate to control/:id where :id is the id of the control you wish to select.

To import/export a csv, navigate to control/export or control/import respectively.

