# Python Docker Image; server side
FROM python:latest

# Copies file to the image
COPY . /app

# Change the dir
WORKDIR /app

# Install all depndencies
RUN pip3 install -r requirements.txt

# Exposes Container to port 8080
EXPOSE 8080

# Defined CMD when starting a container
CMD ["python3","server.py"]