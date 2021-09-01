FROM python:3.9.2-slim-buster
RUN mkdir /bot && chmod 777 /bot
WORKDIR /bot
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get -y install handbrake-cli
COPY . .
RUN pip3 install -r requirements.txt
CMD ["bash","run.sh"]
