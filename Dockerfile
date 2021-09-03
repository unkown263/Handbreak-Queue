FROM python:3.9.2-slim-buster
RUN mkdir /bot && chmod 777 /bot
WORKDIR /bot
ENV DEBIAN_FRONTEND=noninteractive
RUN apt -qq update && apt -qq install -y git wget pv jq python3-dev ffmpeg mediainfo

# Change Debian Repo
RUN echo deb http://http.us.debian.org/debian/ testing non-free contrib main > /etc/apt/sources.list && \
    apt -qq update

# Install other dependencies
RUN apt-get install libcrypt1

# Install HandBrakeCLI
RUN apt-get install handbrake-cli -y

# Copy To Working Directory
COPY . .

# Install Requirements
RUN pip3 install -r requirements.txt

# Start Bot
CMD ["bash","run.sh"]
