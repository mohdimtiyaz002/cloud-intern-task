# Use the official Python base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask and any other dependencies
RUN pip install Flask

# Expose the port that Flask app will listen on
EXPOSE 5000

# Set the command to run your Flask app
CMD ["python", "app.py"]


