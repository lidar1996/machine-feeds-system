# How to Run the Project

# Prerequisites:
1. Docker & Docker Compose installed
2. Ports 5001–5004 and 8080 available on your machine

# Download the Project:
option 1 - Download ZIP
1. Download the project as a ZIP file.
2. Unzip the project folder to your local machine:
   ```unzip machine-feeds-system.zip```
option 2 - Clone from GitHub
1. ```git clone https://github.com/lidar1996/machine-feeds-system.git```

# Run the Project
1. ```cd machine-feeds-system```
2. Run the following command to build and start all services:
   ```docker-compose up --build```

# This will:

Build all microservices (machine_configuration_service, repair_service, session_service, machine_feeds_service).
Start the services on the following ports:
5001 → Machine Configuration Service
5002 → Repair Service
5003 → Session Service
5004 → Machine Feeds Service
8080 → API Gateway (Nginx)

# Accessing the API
Send a GET request to:
```http://localhost:8080/machine-feeds/<machine_id>```

Example:
```curl http://localhost:8080/machine-feeds/1```
This will return a JSON response containing the machine configuration and a combination of repairs and sessions as activities for the specified machine ID.








