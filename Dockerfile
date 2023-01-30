# start by pulling the python image
FROM python:3.8

RUN echo "deb http://deb.debian.org/debian/ unstable main contrib non-free" >> /etc/apt/sources.list.d/debian.list
RUN apt-get update
RUN apt-get install -y --no-install-recommends firefox

# set display port to avoid crash
ENV DISPLAY=:99

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

COPY ./buster_setup /app/buster_setup

RUN chmod +x /app/buster_setup

RUN /app/buster_setup

# copy the buster browser extension
COPY buster_captcha_solver-2.0.1.xpi /app/buster_captcha_solver-2.0.1.xpi

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["audio_captcha.py" ]
