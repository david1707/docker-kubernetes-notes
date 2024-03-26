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