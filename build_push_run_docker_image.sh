#!/bin/bash
#
# Build and tag docker image, push to DockerHub registry and run it locally.
#
# There are two tags one containing the latest commit's short hash and the other with a 'latest' string.
#
# Prerequisite : .env file of the repository.
# It can recieve docker image name as an argument. If not provided it will use the DOCKER_REPO environment variable from your .env file.

docker_image_name=${1:-$(grep "DOCKER_REPO" .env | cut -d "=" -f2-)}

docker_username=$(grep "DOCKER_USER" .env | cut -d "=" -f2-)
docker_password=$(grep "DOCKER_PASSWORD" .env | cut -d "=" -f2-)
port=$(grep "PORT" .env | cut -d "=" -f2-)
version=$(git log -1 --pretty=%h)
tag="$docker_image_name:$version"
latest="${docker_image_name}:latest"
build_timestamp=$( date '+%F_%H:%M:%S' )
container_name="OC-lettings"

echo "Connecting to Docker..."
docker login --username $docker_username --password $docker_password

if [ $? -eq 0 ]; then
    echo "Successfully connected."
else
    echo "Failed to connect to docker hub. Please verify your credentials."
    exit 1   
fi

echo "Building Docker image..."
echo "Tagging with hash of the last commit and with a 'latest' tag..."

docker build -t "$tag" -t "$latest" --build-arg version="$version" --build-arg build_timestamp="$build_timestamp" .

if [ $? -eq 0 ]; then
    echo "Successfully built."
else
    echo "Failed to build! Make sure that your docker deamon is running."
    exit 1   
fi

echo "Pushing to DockerHub registry..."

docker push "$tag" 
docker push "$latest"

if [ $? -eq 0 ]; then
    echo "Successfully pushed."
else
    echo "Failed to push!"
    exit 1   
fi
            

echo "Running a docker container with the latest image..."
if [ ! "$(docker ps -a -q -f name=$container_name)" ]; then
    if [ "$(docker ps -aq -f status=exited -f name=$container_name)" ]; then
        # cleanup
        docker rm $container_name
    fi
    # run the container
    docker run --env-file .env --name $container_name -p $port:$port -it -d $latest
fi


if [ $? -eq 0 ]; then
    echo "The docker container is running successfully."
    echo "You can access the site at : http://0.0.0.0:$port/"
else
    echo "The docker container couldn't be run."
    exit 1
fi