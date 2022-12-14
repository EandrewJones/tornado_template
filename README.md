<p align="center">
  <a href="" rel="noopener">
 <img width=286px height=72px src="TornadoWebServerLogo.png" alt="Tornado Web Serer logo"></a>
</p>

<h2 align="center">API Template</h2>

<div align="center">

</div>

---

## 🧐 About <a name = "about"></a>

This is a reusable template repository for getting a production-ready, Tornado web server up and running, fast.

## 🔖 Project structure

```
tornado_template/
|- app/                     # server application code
|----handlers/              # handler functions for each endpoint
|----server/                # code for running and structuring the API
|----src/                   # functions used in the endpoint handlers
|- tests/                   # Test files should mirror the src folder
|- app.py                   # Tornado server entrypoint
|- config.py                # application configuration
|- Makefile                 # automatize taks through make utility
|- docker-compose.yaml      # utility for easily building and deploying the app in a docker container
|- Dockfile                 # build file for the app docker container
|- pyproject.yaml           # Project configuration
|- requirements.in          # Production dependencies
|- requirements_dev.in      # Development dependencies
|- .flake8                  # flake8 linting configuration
|- .pre-commit-config.yaml  # pre-commit hooks configuration
```

## 🏁 Getting Started <a name = "getting_started"></a>

You can easily clone this repository to up and running.

```bash
$ git clone git@github.com:EandrewJonoes/tornado_template.git
```

### Prerequisites

Setup your environement and install project dependencies.

```bash
# Any environment with python will work, but it's
# best practice to use some sort of virtual environment
# if you want control over python and external dependency versioning
$ conda create -n my_project python=3.10
$ source activate my_project

$ make venv
$ make preinstall
$ make precommit-setup
```

### Dependency Management

For development, track your dependencies in `requirements_dev.in` and install from there.

```bash
$ make install-dev
```

For production, track necessary dependencies in `requirements.in` and install from there.

```bash
$ make install-prod
```

## 🔧 Running the tests

Tests are implemented in ./tests, you need to run the following command to run them.

```
make tests
```

## 🚀 Deployment

The application can easily be built as a docker container and launched with docker compose. Before building and launching the docker container, you must specify the required environment variables in a `.env` file:

```js
SERVER_PORT=<port-number>
SERVICE_TOKEN=<random-hash>
```

Then you can use the makefile commands.

```bash
$ make docker-inspect   # examine whethehr the docker-compose template compiles properly
$ make docker-setup     # re-/build the container(s)
$ make docker-launch    # launch the container
```

To teardown the container:

```bash
$ make docker-teardown
```

**Note**: _The makefile commands assume the system is runnning the newest version of docker compose which has a slight different CLI API (`docker compose` vs `docker-compose`). If your production server is running an older version of docker compose, you should change the makefile docker commands to match your CLI._

## ✍️ Authors

Evan JONES
