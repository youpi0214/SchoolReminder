#!/usr/bin/bash

# Description: This script is used to build and run the bot locally in a docker container

# Usage: ./bot_run.sh [--build] [--run] [--clean]

# Options:
#   --build: Build the docker image
#   --run: Run the docker container
#   --clean: Clean the docker container and image
#   --help: Show this help message
#   --no-cache: Build the docker image without cache

# Example: ./bot_run.sh --build --run
# Example: ./bot_run.sh --clean
# Example: ./bot_run.sh --build --no-cache
# Example: ./bot_run.sh --build --run --no-cache
# Example: ./bot_run.sh --build --run --clean

# Check if the 'docker' command-line tool is installed
if ! command -v docker &> /dev/null; then
  echo "The 'docker' command-line tool is required. Please install it."
  exit 1
fi

# Usage function
usage() {
    echo "Usage: $0 [--build] [--run] [--clean] [--no-cache] [--help]"
    echo
    echo "Options:"
    echo "  --build     Build the docker image"
    echo "  --run       Run the docker container"
    echo "  --clean     Clean the docker container and image"
    echo "  --no-cache  Build the docker image without cache"
    echo "  --help      Show this help message"
}

# Constants
DOCKER_IMAGE_NAME="schoolreminderbot:dev"
DOCKER_CONTAINER_NAME="schoolreminderbot"


# Parse command line arguments
BUILD=false
RUN=false
CLEAN=false
NO_CACHE=false
HELP=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --build)
            BUILD=true
            shift
            ;;
        --run)
            RUN=true
            shift
            ;;
        --clean)
            CLEAN=true
            shift
            ;;
        --no-cache)
            NO_CACHE=true
            shift
            ;;
        --help)
            HELP=true
            shift
            ;;
        *)
            echo "Unknown option: $1"
            usage
            exit 1
            ;;
    esac
done

# Show help message if --help is passed
if [ "$HELP" = true ]; then
    usage
    exit 0
fi

# Clean the docker container and image if --clean is passed
if [ "$CLEAN" = true ]; then
    echo "Cleaning the docker container and image..."

    if [ "$(docker ps -q -f name=$DOCKER_CONTAINER_NAME)" ]; then
        docker stop $DOCKER_CONTAINER_NAME
    fi
    docker rm -f $DOCKER_IMAGE_NAME
    docker rmi -f $DOCKER_IMAGE_NAME
fi

# Build the docker image if --build is passed
if [ "$BUILD" = true ]; then
    if [ "$NO_CACHE" = true ]; then
        echo "Building the docker image without cache..."
        docker build --no-cache -t $DOCKER_IMAGE_NAME .
    else
        echo "Building the docker image..."
        docker build -t $DOCKER_IMAGE_NAME .
    fi
fi

check_env_file_exists() {
    if [ ! -f .env ]; then
        echo ".env file not found. Please create one."
        exit 1
    fi
}


# Run the docker container if --run is passed
if [ "$RUN" = true ]; then
    echo "Running the docker container..."
    check_env_file_exists
    docker run -d -it --rm --env-file .env --name $DOCKER_CONTAINER_NAME $DOCKER_IMAGE_NAME
fi