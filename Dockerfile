# Use an official Python runtime as a parent image
FROM python:slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN apt-get update && \
    apt-get install -y python3-dev build-essential gcc ffmpeg && \
    pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Set the FLASK_APP environment variable
ENV FLASK_APP microservice.py

# Run the Flask application with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:80", "microservice:app"]
