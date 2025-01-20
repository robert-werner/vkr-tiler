import os
from pprint import pprint

import rioxarray
import xarray
import zarr
import rasterio
import rio_tiler
from cloudpathlib import S3Client
from eoreader.keywords import CLEAN_OPTICAL, TO_REFLECTANCE
from eoreader.products import CleanMethod
from eoreader.bands import *
from eoreader.reader import Reader
from rio_tiler.io import XarrayReader

S3_VKR_BUCKET = os.environ['S3_VKR_BUCKET']

def tile(s2_product_path, bands, z, x, y, tilesize=256):
    client = S3Client(aws_access_key_id=os.environ['S3_VKR_USER'],
                      aws_secret_access_key=os.environ['S3_VKR_PASSWORD'],
                      endpoint_url=os.environ['S3_VKR_ENDPOINT'])
    product_path = client.CloudPath(f's3://{S3_VKR_BUCKET}').joinpath(f'{s2_product_path}/')

    reader = Reader()
    prod = reader.open(product_path,
                       remove_tmp=True)
    band_paths = list(prod.get_band_paths(
        band_list=bands
    ).values())
    print(band_paths)







tile("S2A_MSIL1C_20190830T042701_N0208_R133_T48UUG_20190830T074135.SAFE",
           [RED, GREEN, BLUE],
           0,
           0,
           0,
           256)