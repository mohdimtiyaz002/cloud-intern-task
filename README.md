Creating an EC2 Instance 
------------------------
01. Open google
02. Search for Aws console login
03. Click the first link
04. Sign in into the console as root user
05. Select a region 
06. Search for EC2
07. click on instances(running)
08. click on launch instances
09. Edit Nummber of Instances as per your requirement
10. Name the server if you are creating only one else leave empty
11. Select an appropriate OS (Amazon Machine Image [AMI]) in our case ubuntu
12. Select t2.micro for free tier in Instance type
13. Create a key pair or select existing key pair
	 a. To create a key pair click on create key pair.
	 b. Name the key pair and click on create key pair
    c. After clicking the key pair gets downloaded in downloads folder
14. Edit network settings by changing type from SSH to All traffic
15. Lastly click on launch instance
16. Once it displays successful message click on instaces
17. Check the state, if instance state is equal to running then select the machine
18. After selecting click on connect
19. go to ssh client and copy example command

Connecting to EC2
-----------------
01. Open google
02. Search for git download
03. Open the first link
04. click on windows
05. Download the appropriate application as per os architechture
06. Open the downloaded file and install by pressing next, next ... install
07. Once git is installed it automatically installs an application named "git bash"
08. Open git bash
09. move into downloads folder as our key got downloaded there 
10. paste the command that was copied earlier in 19th step of (Creating an EC2 Instance) and hit enter
11. Then enter "yes"
12. After a few seconds you  will notice that your cursor jumps from local machine to remote server

update the apt repository 
-------------------------
01. sudo apt-get update 
 
install docker on ubuntu server
---------------------------------
01. open google 
02. search for get.docker.com
03. click the first link 
04. scroll down to find "install the latest stable versions of Docker CLI, Docker Engine, and their dependencies"
05. copy and paste 1st and 4th command which installs and executes a shell script which inturn install docker depending on the linux flavour

create  python code to display hello world
-------------------------------------------- 
01. create a folder at present working directory and name it as docker-project
02. move into the directory using the command "cd docker-project"
03. create a file named "app.py" uisng the command "vim app.py"
04. paste the following code and save the file

code:

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
 
create dockerfile which creates a customized docker image 

01. create a file named "Dockerfile" using "vim dockerfile" without any extentions 
02. paste the following code and save the file

code:

FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3-pip

RUN pip3 install Flask

WORKDIR /home/ubuntu/docker-project/app

COPY app.py .

EXPOSE 5000

CMD ["python3", "app.py"]


Build the Docker image 
----------------------
01. Execute the following command to build the customized docker image  
"sudo docker build -t my-flask-app ."

Create the container from the docker image 
-------------------------------------------
01.  Execute the following command to create the container 
"sudo docker run -p 5000:5000 my-flask-app"

Check wether the application is running or not by copying the public ip of docker host followed by specified port no in the run cmmand  







 
