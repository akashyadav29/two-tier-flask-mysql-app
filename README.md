# Two Tier Flask + MySQL Application

This project is a Docker-based two-tier application where:
- Flask acts as the backend
- MySQL stores the data
- Docker custom network connects both

## Commands to Run

- docker network create mynet
- docker run -d --name mysql-db --network mynet -e MYSQL_ROOT_PASSWORD=rootpass -e MYSQL_DATABASE=akashdb mysql:5.7
- docker build -t flask-app .
- docker run -d --name flask-app -p 8080:5000 --network mynet flask-app
