# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy application code
COPY app app
COPY tests tests

# Expose port
EXPOSE 5000

# Command to run the application
CMD ["python", "-m", "app.api"]

