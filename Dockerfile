# Use the official Python 3.9 image from Docker Hub as the base image
FROM python:3.9

# Set the working directory in the container to /code
WORKDIR /code

# Copy the requirements.txt file from the host machine to the /code directory in the container
COPY ./requirements.txt /code/requirements.txt

# Install the Python dependencies listed in requirements.txt, with no cache to reduce image size
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the entire app directory from the host machine to the /code directory in the container
COPY ./app /code/app

# Command to run FastAPI application using uvicorn (fastapi command should be changed to uvicorn)
# Exposes the application on port 80 inside the container
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]