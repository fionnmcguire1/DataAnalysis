FROM ubuntu:16.04
RUN apt-get update && \
    apt-get install -y software-properties-common apt-utils locales tzdata
RUN echo "tzdata tzdata/Areas select Europe" > timezone.txt
RUN echo "tzdata tzdata/Zones/Europe select London" >> timezone.txt
RUN debconf-set-selections timezone.txt
RUN rm /etc/timezone
RUN rm /etc/localtime
RUN dpkg-reconfigure -f noninteractive tzdata
#RUN apt-get install vim
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install build-essential checkinstall -y --fix-missing
RUN apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev \
    libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev wget -y
RUN cd /usr/src
RUN wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz
RUN tar xzf Python-3.7.3.tgz
WORKDIR Python-3.7.3
RUN ./configure --enable-optimizations
RUN make -j 1
RUN make altinstall
RUN alias python="python3.7"
RUN apt-get update -y
RUN export PYTHONPATH="/usr/local/lib/python3.7"
RUN python3.7 --version
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3.7 get-pip.py
RUN apt-get clean
#ARG PYTHON_VERSION_TAG=3.7.3
RUN apt-get install liblapack-dev -y
RUN apt-get install libatlas-base-dev -y
RUN apt-get install libfreetype6-dev -y
RUN apt-get install libxml2 -y
RUN apt-get install g++ -y
RUN pip3 install --upgrade pip
RUN mkdir -p DataAnalysis
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
WORKDIR /
#RUN python --version
EXPOSE 80 8080 3500 25 587
VOLUME ["/trace"]
VOLUME ["/root/.ssh"]
RUN apt-get update -y
RUN apt-get install git -y
RUN apt-get install vim -y
CMD sleep infinity
