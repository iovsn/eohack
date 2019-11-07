from eolearn.core import EOPatch, FeatureType
import numpy as np

def udf_to_eopatch(udf_data):
    eopatch = EOPatch()

    arrays = [tile.data for tile in udf_data.raster_collection_tiles]
    arrays = np.asarray(arrays)
    newdata = np.moveaxis(arrays, 0, -1)
    eopatch[(FeatureType.DATA, 'ftr')] = newdata

    return eopatch