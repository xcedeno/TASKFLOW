FROM python:3.11-slim

# Set a project directory
WORKDIR /usr/src/app

# Copy requirements and install
COPY requirements.txt /usr/src/app/requirements.txt
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# Copy full project into container so package `app` exists at /usr/src/app/app
COPY . /usr/src/app

# Expose port
EXPOSE 8000

# Run the app using package import (app.main)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
