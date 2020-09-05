# DevOps Assingment

Lets go through Dockerfile first
Line 01    : Taking tomcat base image from DockerHub
Line 02-03 : Setting Dockerfile author name and mail ID
Line 04-06 : Setting Enviorment variable as instructed
Line 07    : Changing working directory to /usr/local/tomcat/webapps/
Line 08-09 : Updating and installing instructed packages
Line 10    : Copying war file to webapps
Line 11    : Setting Persistent Volume so data won't get deleted
Line 12    : Exposing port 8080 outside the container


To build this docker file, run following command:

docker build -t akshanshsingh/aktomcat:v1.0 .

{Note here "akshanshsingh" is dockerhub username, followed by image name and version }


After the build is sucessfull, we can run the container using following command:

docker run -it -d -p 9191:8080 --name aktomcat akshanshsingh/aktomcat:v1.0

Here,
 -it is used to give interactive terminal
 -d is used to run container in detached mode
 -p is used to map port 8080 of container to Working OS port 9191

To check container is running:
docker ps

To check Tomcat application is running,
 - open your browser and goto http://localhost:9191/SampleWebApp/

Pushing Image to Dockerhub:

Create account on hub.docker.com and verify your email

Docker Login into cli

docker login

--------------o/p--------------------
Username: akshanshsingh
Password: 
-------------------------------------

Pushing Image to DockerHub:

docker push akshanshsingh/aktomcat:v1.0