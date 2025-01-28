import os

from rq import Worker
from tiler.config import REDIS_CONNECTION

from eoreader.reader import Reader as EOReader
from eoreader.bands import SpectralBandNames
from rio_tiler.io import Reader



def tile(s2_product_path, band, z, x, y, tilesize=256):
    s2_product_path_full_path = os.path.join('/opt/satellite-data', s2_product_path)
    product = EOReader().open(s2_product_path_full_path)
    band_paths = product.get_raw_band_paths()
    band_path = band_paths[SpectralBandNames.from_value(band)]

    with Reader(band_path) as image:
        result = image.tile(z, x, y, tilesize=tilesize).data[0]

    return result


if __name__ == "__main__":
    worker = Worker(["default"], connection=REDIS_CONNECTION)
    worker.work()
