############## Python base, all will have it ##################
FROM python:3.10-slim

############## working directory ##################
WORKDIR /app

############## opy app files ##################
COPY . /app

############## dependencies ##################
RUN pip install --no-cache-dir -r requirements.txt

############## Port ##################
EXPOSE 5000

############## Run Flask App ##################
CMD ["python", "app.py"]