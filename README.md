# Two Tier Flask + MySQL Application (Docker Compose)

This project is a Docker-based two-tier application where:

- Flask acts as the backend
- MySQL stores the data
- Docker Compose starts both services
- A Docker volume stores MySQL data permanently

## Commands to Run

# Start the application
docker compose up -d

# Stop the application
docker compose down

## Check Containers
docker compose ps

## Access Web App
http://<EC2-PUBLIC-IP>:8080

## Enter MySQL
docker exec -it mysql-db mysql -uroot -prootpass

## MySQL Commands
USE akashdb;
SELECT * FROM messages;
