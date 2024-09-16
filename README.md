# python-fastapi-mongo-docker

A simple FastAPI application integrated with MongoDB, built with Docker for easy deployment and scalability.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Installation](#Installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)

## Overview
This project is a basic CRUD API built using **FastAPI** and connected to a **MongoDB** database. The application is containerized using Docker, making it easy to deploy in various environments. FastAPI is used for developing the RESTful API, while MongoDB stores the application data.

## Features
- FastAPI for building high-performance APIs.
- MongoDB integration for persistent storage.
- Docker containerization for isolated and portable environments.
- RESTful API for managing users (Create, Read, Update, Delete).

## Prerequisites
Before running this project, ensure you have the following installed on your machine:
- **Docker**: [Download Docker](https://docs.docker.com/get-docker/)
- **Python 3.9 or higher** (if running outside of Docker)
- **MongoDB** (if not using Docker for the database)


## Project Structure
```bash
.
├── app
│   ├── config
│   │   └── database.py           # MongoDB connection setup
│   ├── models
│   │   └── user.py               # Pydantic models for validation
│   ├── routes
│   │   └── route.py              # API routes for user CRUD operations
│   ├── schemas
│   │   └── schemas.py            # Schemas for serializing data
│   └── main.py                   # FastAPI application entry point
├── Dockerfile                    # Dockerfile for building the FastAPI app
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

##  Installation

Build the project from source:

1. Clone the python-fastapi-mongo-docker.git repository:

```sh
❯ git clone https://github.com/sultanhaseeb/python-fastapi-mongo-docker.git
```

2. Navigate to the project directory:
```sh
❯ cd python-fastapi-mongo-docker.git
```

3. Install the required dependencies:
```sh
❯ pip install -r requirements.txt
```

###  Usage

To run the project, execute the following command:

```sh
❯ python main.py
```

###  Running the Application

To run the application using Docker, follow these steps:

1. Clone the python-fastapi-mongo-docker.git repository:

```sh
❯ git clone https://github.com/sultanhaseeb/python-fastapi-mongo-docker.git
```

2. Navigate to the project directory:
```sh
❯ cd python-fastapi-mongo-docker.git
```

3. Build the Docker image for the FastAPI application:
```sh
❯ docker build -t fastapi-mongo-app .
```

4. Run the Docker container from the image:
```sh
❯ docker run -d --name fastapi-container -p 8000:80 fastapi-mongo-app
```

4. To stop and remove the Docker container, use the following commands:
```sh
❯ docker stop fastapi-container
❯ docker rm fastapi-container

```