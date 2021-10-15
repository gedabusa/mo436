FROM ubuntu:20.04
LABEL author="German Salazar"

ENV DEBIAN_FRONTEND noninteractive

COPY . /opt/app
WORKDIR /opt/app

RUN apt-get update && apt-get install -y \
	libopencv-dev \
        python3-pip \
	python3-opencv && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install -r requirements.txt

RUN cd
RUN mkdir -p notebooks
COPY conf/.jupyter /root/.jupyter
COPY run_jupyter.sh /

# Jupyter and Tensorboard ports
EXPOSE 8888 6006

# Store notebooks in this mounted directory
VOLUME /notebooks

# CMD ["chmod", "+x", "run_jupyter.sh"]
CMD ["/run_jupyter.sh"]