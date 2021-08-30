FROM python:3.9.2-slim-buster
RUN mkdir /bot && chmod 777 /bot
WORKDIR /bot
ENV DEBIAN_FRONTEND=noninteractive
RUN apt -qq update && apt -qq install -y git wget pv jq python3-dev ffmpeg mediainfo
# Install Dependency

RUN apt-get install -y libdc1394-22-dev

# Change repo 

RUN echo deb http://http.us.debian.org/debian/ testing non-free contrib main > /etc/apt/sources.list && \

    apt -qq update
COPY . .
RUN pip3 install -r requirements.txt
CMD ["bash","run.sh"]
