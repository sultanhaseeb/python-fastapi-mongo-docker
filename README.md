# python-fastapi-mongo-docker

A simple FastAPI application integrated with MongoDB, built with Docker for easy deployment and scalability.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Installation and Setup](#installation-and-setup)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Docker Usage](#docker-usage)
- [Contributing](#contributing)

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
