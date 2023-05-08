import laspy
import geopandas as gpd

# read in the las file using laspy
las_file = laspy.read("3dbag_v210908_fd2cee53_lod22_3d_1654.las")

# create a GeoDataFrame from the x,y coordinates of the point cloud
points = gpd.GeoDataFrame(geometry=gpd.points_from_xy(las_file.x, las_file.y))

# set the CRS to EPSG:7415
points.crs = "EPSG:7415"

# convert a shapefile into a geodataframe
polygon = gpd.read_file("polygon.shp")

# set the CRS to EPSG:7415 (same as the point cloud)
polygon.crs = "EPSG:7415"

# clip the point cloud to the polygon
clipped_points = points.clip(polygon)

# create a new laspy file object
new_las = laspy.create(point_format=las_file.header.point_format,
                       file_version=las_file.header.version)


# set the x, y, and z values of the new las file
new_las.x = clipped_points.geometry.x.values
new_las.y = clipped_points.geometry.y.values
new_las.z = las_file.z[clipped_points.index]

# write the new las file
new_las.write("clipped_points.las")
