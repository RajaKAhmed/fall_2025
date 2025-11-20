# Use the official lightweight Python image
FROM python:3.11-slim 

# Set the working directory in the container
WORKDIR /app 

# Copy the requirements file
COPY requirements.txt . 

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt 

# Install dependencies
COPY app.py . 

# Expose the port the app runs on
EXPOSE 5000 

# Command to run the application
CMD ["python", "app.py"] 