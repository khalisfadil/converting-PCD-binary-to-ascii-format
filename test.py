from pypcd import pypcd
import pprint
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

## load pcd file
cloud = pypcd.PointCloud.from_path("2021_09_27_11_20_41_179.pcd")
## pretty print the meta data
pprint.pprint(cloud.get_metadata())
## acces the point cloud as numpy structured array
## print the first 10 row (optional to look)
print(cloud.pc_data[:10])
## only access a specific column (here the z-column) (optional)
# print(cloud.pc_data["z"])
## create a copy of the loaded cloud
# Store the cloud uncompressed
cloud.save("new_cloud.pcd")

# this is to edit the file in a numpy array
# -------------------------------------------------------------
# new_cloud_data = cloud.pc_data.copy()
## convert the structured numpy array to a ndarray
# new_cloud_data = np.array(cloud.pc_data.tolist())

## print the shape of the new array
# print(new_cloud_data.shape)
## print the first 10 rows
# print(new_cloud_data[:10])

## split the rgb column into three columns: red, green and blue
# rgb_columns = pypcd.decode_rgb_from_pcl(cloud.pc_data["intensity"])
## normalize the rgb values (they should be between [0, 1])
# rgb_columns = (rgb_columns / 255.0).astype(np.float64)
## print rgb values
# print(rgb_columns[:100])
# Encode the colors (distinct red, green and blue color columns => one single column)
# encoded_colors = pypcd.encode_rgb_for_pcl((rgb * 255).astype(np.uint8))
