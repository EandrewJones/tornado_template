FROM ubuntu:22.04

ENV VIRTUAL_ENV=venv
ENV PATH="/bin/bash:$VIRTUAL_ENV/bin:$PATH"

# Install python version
RUN apt-get update && apt-get install -y software-properties-common gcc apt-utils && \
    add-apt-repository -y ppa:deadsnakes/ppa
RUN apt-get update && apt-get install -y python{{cookiecutter.python_major_version}}.{{cookiecutter.python_minor_version}} python{{cookiecutter.python_major_version}}.{{cookiecutter.python_minor_version}}-venv python3-distutils python3-pip python3-apt

# Copy all source code
COPY makefile requirements.txt .env app.py config.py ./
COPY app app

# Setup dependencies
RUN make venv && make install-prod

ENTRYPOINT [ "python3", "app.py" ]