# clip_PC_using_shp
This simple script makes it possible to output a clipped .las point cloud using the extent of a polygon.

This Python script reads in a LAS point cloud file using the laspy library and converts the x, y coordinates of the point cloud into a GeoDataFrame using geopandas. It then reads in a shapefile polygon and clips the point cloud to the extent of the polygon. The clipped point cloud is then saved into a new LAS file using laspy. The script is useful for clipping large point clouds to a specific area of interest, such as a building footprint or a specific land cover type.

N.B: 
- Make sure you have your shapefile and your pointcloud in the same directory as the script, or else copy-paste their absolute path when reading them. 
- The two geodataframes(the one containing the polygon and the one containing the points) should have the same CRS. 
