#python packages245
import arcpy
import numpy
import pandas as pd
from scipy import stats
#setting the environment
dir_path = r"C:/Users/Warda/Box/BIHS_withMaheenJavaid/Flood data/"
arcpy.env.workspace = dir_path

day_path_list=[]#initialize list
day_list = list(range(182,273,1))
for day_num in day_list:
    day_path_list.append(r'MWP_2010'+str(day_num)+r'_060E030N_3D3OT.tif;MWP_2010'+str(day_num)+r'_060E040N_3D3OT.tif;MWP_2010'+str(day_num)+r'_070E030N_3D3OT.tif;MWP_2010'+str(day_num)+r'_070E030N_3D3OT.tif')
day_path_list

i=182
for day in day_path_list:
    arcpy.MosaicToNewRaster_management(input_rasters=day, output_location='', raster_dataset_name_with_extension=r"compiled_data_"+i+".tif", coordinate_system_for_the_raster="", pixel_type="8_BIT_UNSIGNED", cellsize="", number_of_bands="1", mosaic_method="LAST", mosaic_colormap_mode="FIRST")
    i=i+1