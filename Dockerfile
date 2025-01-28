FROM python:3.12-slim

RUN apt-get update
RUN apt-get install -y libjemalloc-dev
ENV LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libjemalloc.so

COPY . /opt/vkr-tiler
WORKDIR /opt/vkr-tiler

RUN pip install --no-cache-dir -e .

ENTRYPOINT /opt/vkr-tiler/scripts/exec_service.sh