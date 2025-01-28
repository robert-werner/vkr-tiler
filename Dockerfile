FROM python:3.12-slim

RUN apt-get update
RUN apt-get install -y libjemalloc-dev expat
ENV LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libjemalloc.so

WORKDIR /app
ADD . /app
RUN pip install -e .
RUN pip install setuptools --upgrade

CMD ["python", "worker.py"]