# Project X Website Mock API

## How to run with Docker

Two steps:

- Build the image from Dockerfile
- Run the built image

```sh
# Build the Docker image with tag python-docker
docker build --tag python-docker .

# Run the Docker image porting from 5000 Docker image to port 8000 on our localhost, with .env as environment variables
docker run --publish 8000:5000 --env '.env' python-docker
```

### How to get API_KEY

Contact Tuan Nguyen 😊
