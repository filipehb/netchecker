# Internet Monitor

This project is a network monitoring tool that periodically tests internet speed, DNS resolution, ping, and traceroute for a list of domains. The results are logged into a text file for later analysis. The tool is packaged in a Docker container for ease of deployment and execution.

### Files Description

- **Dockerfile**: Specifies the base image and the steps to install dependencies and run the `netchecker.py` script.
- **requirements.txt**: Contains the Python libraries that need to be installed in the Docker container.
- **netchecker.py**: The main script that performs speed tests, DNS resolution, ping tests, and traceroute for each domain listed in `domains.txt`.
- **domains.txt**: A text file where each line represents a domain to be tested.
- **README.md**: This file, which provides an overview of the project and instructions on how to build and run the Docker container.

## Building the Docker Container

To build the Docker container, navigate to the project directory and run the following command:

```bash
docker build -t internet-monitor .
```

## Running the Project

Once the Docker image is built, you can run the container with the following command:

```bash
sudo docker run -d --name internet-monitor-container -v $(pwd)/internet_test_results.txt:/app/internet_test_results.txt internet-monitor
```

## Stopping the Container
To stop the container, run:

```bash
sudo docker stop internet-monitor-container
```

### To remove the container after stopping it:

```bash
sudo docker rm internet-monitor-container
```


