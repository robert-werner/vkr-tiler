import os

from eoreader.bands import *
from eoreader.reader import Reader


def tile(s2_product_path, bands, z, x, y, tilesize=256):
    ...