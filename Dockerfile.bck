# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /dk_app_hw

# Copy the current directory contents into the container
COPY main.py /dk_app_hw/main.py

# Install the required Python packages
RUN pip install --no-cache-dir flask gunicorn

# Expose the port the app runs on
EXPOSE 8080

# Set the environment variable for Flask
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV PORT=8080

# Command to run the application
CMD ["gunicorn", "-b", "0.0.0.0:8080", "main:app"]
# CMD ["python3", "/dk_app_hw/main.py"]

# End of file

