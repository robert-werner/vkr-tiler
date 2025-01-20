FROM python:3.12-slim

RUN apt-get update
RUN apt-get install -y libjemalloc-dev
ENV LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libjemalloc.so

COPY . /opt/vkr_tiler
WORKDIR /opt/vkr_tiler

RUN pip install --no-cache-dir -r requirements.txt

