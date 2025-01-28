import os

from eoreader.bands import *
from eoreader.reader import Reader
from rq.decorators import job

from tiler.config import REDIS_CONNECTION


@job('high', connection=REDIS_CONNECTION)
def tile(s2_product_path, band, z, x, y, tilesize=256):
    ...