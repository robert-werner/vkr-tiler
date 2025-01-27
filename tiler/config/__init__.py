from redis import Redis

from tiler.settings import Settings

REDIS_CONNECTION = Redis(host=Settings().redis_host, port=Settings().redis_port)
