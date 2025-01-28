FROM python:3.12-slim

WORKDIR /app
ADD . /app
RUN pip install -e .

RUN apt-get update
RUN apt-get install -y libjemalloc-dev
ENV LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libjemalloc.so

CMD ["python", "worker.py"]