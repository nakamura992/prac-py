FROM python:3.12

RUN apt-get update
RUN pip install --upgrade pip
RUN python -m pip install jupyterlab