#!/bin/bash
#
# Pull a docker image from DockerHub and run it in your machine.
#
# Prerequisite : .env file of the repository.
# It can recieve docker image name as an argument. If not provided it will use the DOCKER_REPO environment variable from your .env file.

docker_image_name=${1:-$(grep "DOCKER_REPO" .env | cut -d "=" -f2-):latest}

docker_username=$(grep "DOCKER_USER" .env | cut -d "=" -f2-)
docker_password=$(grep "DOCKER_PASSWORD" .env | cut -d "=" -f2-)
port=$(grep "PORT" .env | cut -d "=" -f2-)
container_name="OC-lettings"

echo "Connecting to Docker..."
docker login --username $docker_username --password $docker_password

if [ $? -eq 0 ]; then
    echo "Successfully connected."
else
    echo "Failed to connect to docker hub. Please verify your credentials."
    exit 1   
fi

echo "Downloading docker image..."
docker pull $docker_image_name

if [ $? -eq 0 ]; then
    echo "The docker image has successfully downloaded."
else
    echo "The download of the docker image has failed. Please verify your repository name."
    exit 1
fi

echo "Running a docker container..."
if [ ! "$(docker ps -a -q -f name=$container_name)" ]; then
    if [ "$(docker ps -aq -f status=exited -f name=$container_name)" ]; then
        # cleanup
        docker rm $container_name
    fi
    # run the container
    docker run --env-file .env --name $container_name -p $port:$port -it -d $docker_image_name
fi


if [ $? -eq 0 ]; then
    echo "The docker container is running successfully."
    echo "You can access the site at : http://0.0.0.0:$port/"
else
    echo "The docker container couldn't be run."
    exit 1
fi