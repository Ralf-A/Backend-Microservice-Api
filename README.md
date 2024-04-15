# Microservice Application Using Docker

## Overview
This application consists of two Docker containers that work together to provide network interface information through an HTTP API. The first container runs an HTTP server that exposes an API endpoint to return details about the available network interfaces. The second container runs an HTTP client that periodically calls the server's endpoint and prints the results.

## How to Build and Run Containers

### Prerequisites
- Docker
- Docker Compose

### Building the Containers
1. Clone the repository to your local machine.
2. Navigate to the root directory of the project.
3. Run the following command to build the containers:

- `docker-compose build`


### Running the Containers
#### 1. To start the containers, run:

- `docker-compose up`

#### 2. To run the containers in the background, use:

- `docker-compose up -d`


## API Endpoints

### HTTP Server (Container 1)

#### GET /network
- **Description**: Returns details of all available network interfaces.
- **Response**:
```json
{
 "interfaces": "<interface_details>"
}
```

- ** Example**:

- `localhost:80/network`

#### GET /network?interface={interface_name}
- **Description**: Returns details of the specified network interface.
- **Parameters**:
- `interface`: The name of the network interface.
- **Response**:
```json

{
  "<interface_name>": "<interface_details>"
}
```

- **Error Response**:

```json
{
  "error": "Interface not found"
}
```

- ** Example**:

- `localhost:80/network?interface=eth0`
  
### HTTP Client (Container 2)
- Periodically calls the server’s endpoint and prints the results to the console.
#### Important Notes
- The HTTP server uses Flask without external libraries to read network interface information.
- The HTTP client is configured to call the server at a set interval, which can be modified in the client’s code.
- Error handling and logging have been implemented for robustness.
- Unit tests are included to ensure the API’s functionality.
### Assumptions Made During Development
- The application assumes that it is running on a Linux-based system where the ip addr command is available.
- Network interface details are obtained using shell commands executed from within the Python code.
- The Dockerfiles for both the server and client are set up to install all necessary dependencies.
