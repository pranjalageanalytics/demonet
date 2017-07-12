#
# Super simple example of a Dockerfile
#
FROM ubuntu:latest
MAINTAINER Admin Team "pranjal@ageanalytics.co"

RUN apt-get update
RUN apt-get install -y python python-pip wget
RUN pip install ansible
RUN ansible-playbook -i hosts -u root provision.yml
