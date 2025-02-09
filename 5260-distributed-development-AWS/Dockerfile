# Step 1: Specify the runtime environment
FROM python:3.10

# Step 2: Copy the program into the container
WORKDIR /app
COPY requirements.txt /app/
COPY consumer.py /app/

# Step 3: Specify the command to run the program
RUN pip install -r requirements.txt
CMD ["python", "consumer.py", "--storage-strategy", "s3", "--bucket-name", "usu-cs5260-excludedartichoke-requests", "--queue-name", "cs5260-requests"]
