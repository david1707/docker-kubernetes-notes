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
sudo chmod 644 /var/run/docker.sock

```

Test it:

```
docker run hello-world
```

## Basic commands

```
# List all images
docker images

# Download or execute a container from an image
docker run <IMAGE_NAME>

# Download a specific version
docker run <IMAGE_NAME>:<VERSION>

# Assign a name to the container on start
docker run --name <NEW_CONTAINER_NAME> <IMAGE_NAME> 

# Remove a container after it is stopped
docker run --rm <IMAGE_NAME>

# Restart a stopped container
docker start <CONTAINER_ID>

# Execute a container in the background (Detached to the container: You can see the logs)
docker run -d <IMAGE_NAME>

# Bring a container from the background to the foreground (Attached to the container: You can see the logs)
docker attach <IMAGE_NAME>

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
docker container inspect <NAME_OR_ID>

# Get logs from a container running in the background
docker logs <NAME_OR_ID>

# Get all the layers from an image
docker history <IMAGE_NAME>

# Stop a container
docker stop <IMAGE_NAME_OR_ID>

# Build an image from a Dockerfile
docker build . -t <NAME>:<TAG>

# Copy files
docker cp <FOLDER/FILE_PATH> <CONTAINER_ID>:<DESTINATION_PATH>

# Environment values
docker run <OPTIONS> -e <KEY>=<VALUE>
docker run <OPTIONS> -e PORT=8000

# Argument values
docker build <OPTIONS> --build-arg <ARG_VALUE> .
docker build <OPTIONS> --build-arg DEFAULT_PORT=8000 .
```

# Remove containers/images
```
# Remove permanently a container
docker rm <IMAGE_NAME_OR_ID>

# Remove all stopped containers
docker container prune

# Remove all containers
docker rm $(docker ps -aq)

# Remove permanently an image that isn't being used
docker rmi <IMAGE_NAME>

# Remove all unused images
docker image prune

# Remove all images
docker image prune -a
```

### Volumes 
```
# Anonymous volume
docker run <OPTIONS> -v <CONTAINER_PATH> <IMAGE_NAME>
docker run <OPTIONS> -v /app/feedback <IMAGE_NAME>

# Create a Named (persistent) volume
docker run <OPTIONS> -v <NAME>:<CONTAINER_PATH> <IMAGE_NAME>
docker run <OPTIONS> -v feedback:/app/feedback <IMAGE_NAME>

# Create a Bind Mount (managed by you) 
docker run <OPTIONS> -v <NAME>:<CONTAINER_PATH> -v <HOSTMACHINE_ABSOLUTE_PATH>:<CONTAINER_WORKDIR> <IMAGE_NAME>
docker run <OPTIONS> -v feedback:/app/feedback -v '/home/david/Documents/docker-kubernetes-notes/05 - Data volumes/:/app' <IMAGE_NAME>

# Read only volumes
docker run <OPTIONS> -v <HOSTMACHINE_ABSOLUTE_PATH>:<CONTAINER_WORKDIR>:ro <IMAGE_NAME>

# List existing volumes
docker volume ls

## Overview
# Anonymous volume
docker run -v /app/data

# Named volume
docker run -v data:/app/data

# Bind mount
docker run -v /local/path:/app/data
```

### Networks
```
# Create a network
docker network create <NETWORK_NAME>

# Inspect existing networks
docker network ls

# Start an image using a network
docker run <OPTIONS> --network <NETWORK_NAME> <IMAGE_NAME>
docker run -d --name mongodb --network favourites-net mongo
```
# How to...

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
3. Build your image with `docker build -t <DOCKERHUB_USER_NAME>/<IMAGE_NAME>:<TAG> .`
4. Push it to the Docker Hub with `docker push <DOCKERHUB_USER_NAME>/<IMAGE_NAME>:<TAG> `
5. Now you can check your newly updated image. For example, mine is https://hub.docker.com/repository/docker/david1707/first_dockerized_code/general

## How to connect containers
1. Create a new network with ``docker network create <NETWORK_NAME>``.
2. Start an image, using the network ``docker run <OPTIONS> --network <NETWORK_NAME> <IMAGE_NAME>``.
3. Now, you can replace its name to use it as a domain ``mongoose.connect('mongodb://<NETWORK_NAME>:27017/my_database')``.
4. Rebuild the Docker image, as we have changed the code.
5. Run the container that will connect to that network with ``docker run <OPTIONS> --network <NETWORK_NAME>``.