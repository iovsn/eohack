from eolearn.core import EOPatch, FeatureType
from sentinelhub import BBox, CRS
import numpy as np
from openeo_udf.api.udf_data import UdfData, RasterCollectionTile, SpatialExtent


def udf_to_eopatch(udf_data):
    eopatch = EOPatch()

    for tile in udf_data.raster_collection_tiles:
        eopatch[(FeatureType.DATA, tile.id)] = tile.data[..., np.newaxis]

    extent = udf_data.raster_collection_tiles[0].extent
    bbox = BBox((extent.left, extent.bottom, extent.right, extent.top), CRS.WGS84)
    eopatch.bbox = bbox

    return eopatch

def eopatch_to_udf(eopatch):
    bbox = eopatch.bbox
    extent = SpatialExtent(bottom=bbox.min_y, top=bbox.max_y, left=bbox.min_x, right=bbox.max_x)

    tiles = [RasterCollectionTile(id=name, extent=extent, data=data.squeeze()) for name, data in eopatch.data.items()]

    return tiles

