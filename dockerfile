FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3-pip

RUN pip3 install Flask
RUN pip3 install requests pytest
RUN apt-get install -y openjdk-11-jdk
ADD https://get.jenkins.io/war-stable/2.263.4/jenkins.war  /
WORKDIR /home/ubuntu/docker-project/app

COPY app.py .
COPY test_my_website.py .
EXPOSE 5000

CMD ["python3", "app.py"]

