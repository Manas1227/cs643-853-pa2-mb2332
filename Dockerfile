# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables to prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install Java (required for Spark) and other dependencies
RUN apt-get update && apt-get install -y \
    openjdk-11-jdk \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set JAVA_HOME environment variable
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

# Install PySpark
RUN pip install pyspark findspark boto3

# Set the working directory
WORKDIR /app

# Copy training and prediction scripts to the container
COPY training_manas.py prediction_manas.py /app/

# Command to execute (default: show help message)
CMD ["python", "--help"]
