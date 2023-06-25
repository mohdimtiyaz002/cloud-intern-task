FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3-pip

RUN pip3 install Flask

WORKDIR /home/ubuntu/docker-project/app

COPY app.py .

EXPOSE 5000

CMD ["python3", "app.py"]
