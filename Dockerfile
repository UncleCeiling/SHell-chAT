ARG PYTHON_VER=3.13.5
FROM python:${PYTHON_VER}-slim

# Prevent `pyc` files.
ENV PYTHONDONTWRITEBYTECODE=1
# Prevent lost logs.
ENV PYTHONUNBUFFERED=1

# Sets the working directory for the rest of the Dockerfile
WORKDIR /

# apt req
RUN apt update -y && apt upgrade -y

# pip req
RUN python3 -m pip install --upgrade pip
COPY requirements.txt ./
RUN python3 -m pip install -r requirements.txt

# copy files
COPY ./client_config.json.sample ./data/client_config.json
COPY ./server_config.json.sample ./data/server_config.json
COPY . .

# run the bot
CMD ["python3","server.py"]