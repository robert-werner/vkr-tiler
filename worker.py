import os

from rq import Worker
from eoreader.reader import Reader
from eoreader.bands import *

from tiler.config import REDIS_CONNECTION


def tile(s2_product_path, band, z, x, y, tilesize=256):
    s2_product_path_full_path = os.path.join('/opt/satellite-data', s2_product_path)
    product = Reader().open(s2_product_path_full_path)
    print(product, flush=True)
    return product


if __name__ == "__main__":
    worker = Worker(["default"], connection=REDIS_CONNECTION)
    worker.work()
