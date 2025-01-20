import os

from redis import Redis

REDIS_CONNECTION = Redis(host=os.environ['REDIS_HOST'],
                         port=os.environ['REDIS_PORT'],
                         password=os.environ['REDIS_PASSWORD'])