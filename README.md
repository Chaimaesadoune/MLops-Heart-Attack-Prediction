<h1 align="center">MLops: Heart Attack Prediction</h1>

This repository contains the code for a machine learning-powered API that predicts the likelihood of heart attacks. The API is built using FastAPI and is monitored using Grafana. It is containerized using Docker for ease of deployment and scalability.

## Installation

There are only two prerequisites:

* [Docker](https://docs.docker.com/get-docker/)
* [Docker-compose](https://docs.docker.com/compose/install/)

Having both, you'll need to clone the repository:

``` bash
git clone https://github.com/Chaimaesadoune/MLops-Heart-Attack-Prediction
```

## Usage

You'll need to run the docker containers:

``` bash
docker-compose up
```

Now you have access to those three containers and their respective ports:

* Prometheus: http://localhost:9090/
* Grafana: http://localhost:3000/
* FastAPI: http://localhost:8000/

Credentials:
* Username: admin
* Password: admin

Students:
* Hiba Nokra
* Chaimae Sadoune
* Hamza Iben Jellal
* Nabil Ramdani
