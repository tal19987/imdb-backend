# Python Docker Image; server side
FROM python:latest

# Copies file to the image
COPY . /app

# Change the dir
WORKDIR /app

# Install all depndencies
RUN pip install -r requirements.txt

# Defined Enyrtpoint when starting a container
ENTRYPOINT ["python"]

# Defined CMD when starting a container
CMD ["server.py"]