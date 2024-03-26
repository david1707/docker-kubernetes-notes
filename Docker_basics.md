## Install Docker

```
# Uninstall previous Docker versions
sudo apt-get purge docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin docker-ce-rootless-extras
sudo rm -rf /var/lib/docker
sudo rm -rf /var/lib/containerd

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh

# Check that Docker is installed 
sudo docker version

# Don't get asked for sudo permissions
sudo chmod 666 /var/run/docker.sock
```


Test it:

```
docker run hello-world
```

## Create an image

1. Create a file named **Dockerfile**.
2. Write the code. For example:
```
# syntax=docker/dockerfile:1

FROM ubuntu:22.04
COPY . /app
RUN make /app
CMD python /app/app.py
```
3. Build it with ``docker build .``
4. Check out the ID of the image with ``docker images``
5. Run it with ``docker run <IMAGE_ID>``
6. When you are done, close it with ``docker stop <IMAGE_ID>``

Mind you: This is a simple and quick way to create an image to understand how Docker works. This doesn't have a port exit to reach out, nor persistance.

## How to publish an image
How to build, and then publish, an image to https://hub.docker.com/

1. Make sure you are logged in with ``docker login``
2. After your are logged in, check again with ``docker login``. You should see the "Login Succeeded" message.
3. Build your image with `docker build -t <IMAGE_NAME> .`
4. Tag it with your username `docker tag <IMAGE_NAME> <DOCKERHUB_USER_NAME>/<IMAGE_NAME>:v1`
5. Push it to the Docker Hub with `docker push david1707/f<IMAGE_NAME>:v1`
6. Now you can check your newly updated image. For example, mine is https://hub.docker.com/repository/docker/david1707/first_dockerized_code/general


## Basic commands

```
# List all images
docker images

# Download or execute a container from an image
docker run <IMAGE_NAME>

# Download a specific version
docker run <IMAGE_NAME>:<VERSION>

# Execute a container in the background
docker run -d <IMAGE_NAME>

# Bring a container from the background to the foreground
docker run attach <ID>

# Execute a command
docker run ubuntu cat /etc/*release*
docker run ubuntu sleep 15

# Download an image to run it later
docker pull <IMAGE_NAME>

# Execute a command inside the docker container
docker exec <COMMAND>

# Connect to the container's bash
docker run -it <IMAGE_NAME> bash

# List all running containers
docker ps

# List ALL containers, running or not
docker ps -a

# Run a container with a link to other container:
docker run -p <PORT_LOCAL>:<PORT_DEFAULT> --link <IMAGE_NAME_TO_LINK>:<IMAGE_NAME_TO_LINK> <IMAGE_NAME>
docker run -p 5000:80 --link redis:redis voting-app

# Get details from an image or container in JSON format
docker inspect <NAME_OR_ID>

# Get logs from a container running in the background
docker logs <NAME_OR_ID>

# Get all the layers from an image
docker history <IMAGE_NAME>

# Stop a container
docker stop <IMAGE_NAME_OR_ID>

# Remove permanently a container 
docker rm <IMAGE_NAME_OR_ID>

# Remove permanently an image that isn't being used
docker rmi <IMAGE_NAME>

# Build an image from a Dockerfile
docker build . -t <NAME>

# Environment variables
docker run -e <VARIABLE>=<VALUE> <IMAGE_NAME>
docker run -e APP_COLOR=blue simple-webapp-color
```