# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Install iproute2 to get the 'ip' command
RUN apt-get update && apt-get install -y iproute2

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir Flask

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME NetworkInfo

# Run server.py when the container launches
CMD ["python", "server.py"]
