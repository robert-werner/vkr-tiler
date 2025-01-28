from rq import Worker

from tiler.config import REDIS_CONNECTION


def tile(s2_product_path, band, z, x, y, tilesize=256):
    return s2_product_path, band, z, x, y, tilesize


if __name__ == "__main__":
    worker = Worker(["default"], connection=REDIS_CONNECTION)
    worker.work()
