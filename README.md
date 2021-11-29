# converting-PCD-binary-to-ascii-format
# PCD-file converter

this algorithm suppose to convert the PCD file that is in binary format into ASCII format so that it can be vizualize in pcl-viewer. 

go to the `test.py` and put your file name in the 
```bash
 cloud = pypcd.PointCloud.from_path("your-filename.pcd")
``` 
like example,

```bash
cloud = pypcd.PointCloud.from_path("2021_09_27_11_20_41_179.pcd")
```


## save file

the file is saved as `new_cloud.pcd` after running the `test.py`

## open file

For Linux OS

to open the converted file by using `pcl-viewer` by installing the `pcl-tools` package.

```bash
pcl_viewer -multiview 1 <pcd_filepath>
```
