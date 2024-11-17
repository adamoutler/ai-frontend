# Dockerfile for AI Frontend

# Base Image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt into the container
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY src/python/app /app
COPY src/python/app/css /app/css

# Expose port (default Gradio port)
EXPOSE 7860

# Define environment variables to be passed from Docker Compose
ENV APIKEY=${APIKEY}
ENV BOTID=${BOTID}
ENV COMPLETIONSURL=${COMPLETIONSURL}
ENV SYSTEMPROMPT=${SYSTEMPROMPT}

# Run the application
CMD ["python", "ai-frontend.py"]
