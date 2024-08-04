#Installing the neccessary packages
get_ipython().system('pip install rasterio')
get_ipython().system('pip install matplotlib')
get_ipython().system('pip install geopandas')
get_ipython().system('pip install pyproj')
get_ipython().system('pip install earthpy')
get_ipython().system('pip install os')
get_ipython().system('pip install folium')




#Importing the required packages
import os
import geopandas as gpd
from pyproj import CRS
import matplotlib.pyplot as plt
import rasterio
get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib.patches import Rectangle
import numpy as np
import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep
import folium
import matplotlib.cm as cm





#Creating a "relative filepath" of the folder for acessing files from that folder

# Specifing the directory or path where all the  files in that folder are stored
directory = "D:/Kaushal_Rhythem/Data"

# For getting the "absolute path" of all files in the directory specified above
file_paths = []
for file_name in os.listdir(directory):
    file_path = os.path.join(directory, file_name)
    if os.path.isfile(file_path):
        file_paths.append(file_path)

# To print the "absolute paths" of all files
for file_path in file_paths:
    print(file_path)


# Vector data processing:

# Defining the file path of Indian boundary
Indian_Bundary = file_paths[17]  
# Reading the shapefile of Indian Boundary
shapefile1 = gpd.read_file(Indian_Bundary) 
# reading and plotting the map of India
shapefile1 = gpd.read_file(Indian_Bundary)
shapefile1.plot()
plt.title(" Map of India")
plt.show()

# Defining the file path of State(Himachal Pradesh) of my area of interest
Himachal_Pradesh = file_paths[11]

# Reading the shapefile of Himachal Pradesh,India
shapefile2 = gpd.read_file(Himachal_Pradesh)    

# Clip Himachal Pradesh  from Indian boundary
clipped_state = gpd.clip(shapefile1, shapefile2)
# plotting the map of clipped Himachal Pradesh
clipped_state.plot()


# reading and plotting the map of Himachal Pradesh, India
shapefile2 = gpd.read_file(Himachal_Pradesh)
shapefile2.plot()
plt.title(" Map of HimachalPradesh")
plt.show()

# Defining the file path of district of my area of interest(Kausauli)
Solan_shp_path = file_paths[36]

# reading the shapefile of Solan district
shapefile3 = gpd.read_file(Solan_shp_path)

# Clip Solan district from the state of Himachal Pradesh
clipped_district = gpd.clip(shapefile2,shapefile3)
# Plot the intersection result
clipped_district.plot()

# Display the plot
plt.show()

# To intersect area of interest( Kasauli) from Solan
# Define the file paths
Solan_shp_path = file_paths[36]
Kasauli_shp_path = file_paths[25]
# Read the shapefiles
shapefile3 = gpd.read_file(Solan_shp_path)
shapefile4 = gpd.read_file(Kasauli_shp_path)

# Perform the intersection
intersection = gpd.overlay(shapefile3, shapefile4, how='intersection')

# Plot the intersection result
intersection.plot()

# Display the plot
plt.show()
# Defining the file path of railways
Railways_shp_path = file_paths[44]
# Reading the shapefile of railways
shapefile5= gpd.read_file(Railways_shp_path)
# Plotting the shapefile of railways
shapefile5.plot()
plt.show()


# To check if the railway lines lie within the Kasauli town
Railways_shp_path = file_paths[44]
Kasauli_shp_path = file_paths[25]
# Read the shapefiles
shapefile5= gpd.read_file(Railways_shp_path)
shapefile4 = gpd.read_file(Kasauli_shp_path)
#Performing intersection
intersected_railways = gpd.overlay(shapefile5, shapefile4, how='intersection')
#Plot the result
intersection.plot()
# Display the plot
plt.show()

# Create a new figure and axis
fig, ax = plt.subplots(figsize=(10, 10))
# Plot the area of interest shapefile
shapefile4.plot(ax=ax, facecolor='none', edgecolor='black')
#Plot the railways that come inside the area of interest
intersected_railways.plot(ax=ax, color='black', linewidth=2)

# Show the plot
plt.show()

# Since railways lie within our study region therefore, we can clip it from the boundary of Kasauli shapefile


# To clip the railways for Kasauli(area of interest)
# Defining file path
Railways_shp_path = file_paths[44]
Kasauli_shp_path = file_paths[25]
# Read the shapefiles
shapefile4 = gpd.read_file(Kasauli_shp_path)
shapefile5= gpd.read_file(Railways_shp_path)
# Performing clipping
clipped_railways = gpd.clip(shapefile4, shapefile5)
# Plot the result
clipped_railways.plot()
# Display the plot
plt.show()
# To clip the roads for Kasauli(area of interest)
# Defining file path
Roads_shp_path = file_paths[52]
Kasauli_shp_path = file_paths[25]
# Read the shapefiles
shapefile4 = gpd.read_file(Kasauli_shp_path)
shapefile6= gpd.read_file(Roads_shp_path)
# Performing clipping
clipped_roads = gpd.clip(shapefile4, shapefile6)
# Plot the result
clipped_roads.plot()
# Display the plot
plt.show()

# To clip the rivers/streams for Kasauli(area of interest)
# Defining file path
Rivers_shp_path = file_paths[60]
Kasauli_shp_path = file_paths[25]
# Read the shapefiles
shapefile4 = gpd.read_file(Kasauli_shp_path)
shapefile7= gpd.read_file(Rivers_shp_path)
# Performing clipping
clipped_Rivers = gpd.clip(shapefile4, shapefile7)
# Plot the result
clipped_Rivers.plot()
# Display the plot
plt.show()

# Plotting a base map of Kasauli using rivers, roads, railways, waterways shapefile.
# Define the file paths for the roads, railways, rivers, and area of interest shapefiles
Roads_shp_path = file_paths[52]
Railways_shp_path = file_paths[44]
Rivers_shp_path = file_paths[60]
Kasauli_shp_path = file_paths[25]
# Read the shapefiles
shapefile6= gpd.read_file(Roads_shp_path)
shapefile5= gpd.read_file(Railways_shp_path)
shapefile7= gpd.read_file(Rivers_shp_path)
shapefile4 = gpd.read_file(Kasauli_shp_path)

from matplotlib.patches import Rectangle

# Create a new figure and axis
fig, ax = plt.subplots(figsize=(10, 10))

# Plot the area of interest shapefile
shapefile4.plot(ax=ax, facecolor='none', edgecolor='black')

# Plot the roads, railways, and rivers
clipped_roads.plot(ax=ax, color='black', linewidth=2)
clipped_railways.plot(ax=ax, color='grey', linewidth=2)
clipped_Rivers.plot(ax=ax, color='blue', linewidth=2)
# Add a title
plt.title(' Base map of Area of Interest')
# Define legend handles and labels
legend_elements = [
    Rectangle([0, 0], 1, 1, color='black', label='Roads'),
    Rectangle([0, 0], 1, 1, color='grey', label='Railways'),
    Rectangle([0, 0], 1, 1, color='blue', label='Rivers'),
    
]
ax.legend(handles=legend_elements)

# Show the plot
plt.show()


# raster data analysis
#Assigning variables to the input files
Band4_2018 = file_paths[0]  
Band4_2020 = file_paths[1]  

Band4_2022 = file_paths[2]  
Band5_2018 = file_paths[3]  
Band5_2020 = file_paths[4]  

Band5_2022 = file_paths[5]  


# To Open the Band4_2018 using rasterio
raster = rasterio.open(Band4_2018)

# To check the "type" of  variable of raster
type(raster)

# Checking the properties of Band4(raster data) of the year 2018:

# Checking the projection
print(raster.crs)
# Affine transform (how raster is scaled, rotated, skewed, and/or translated)
raster.transform
# Checking the Dimensions( width and height) 
print(raster.width)
print(raster.height)
# Checking the number of bands in raster data 
raster.count
# Bounds of the raster data
raster.bounds
# Driver (data format of raster data)
raster.driver
# No data values for all channels
raster.nodatavals
# Checking all metadata for the whole raster dataset
raster.meta


# To Open the raster file"Band5_2018" using rasterio 
raster = rasterio.open(Band5_2018)

# Checking the "type" of variable raster
type(raster)

# Checking the properties of raster file  Band 5 of year 2018:

# Checking the projection
print(raster.crs)
# Affine transform (how raster is scaled, rotated, skewed, and/or translated)
raster.transform
# Checking dimensions of raster(width, height)
print(raster.width)
print(raster.height)
# Checking the number of bands in raster data
raster.count
# Bounds of the file
raster.bounds
# Checking the Driver (data format)of raster file
raster.driver
# No data values for all channels
raster.nodatavals
# Checking all metadata for the whole raster dataset
raster.meta


# To Open the raster file" Band 4 from 2020" using rasterio
raster = rasterio.open(Band4_2020)

# Checking the "type" of the variable of raster
type(raster)

#Checking the properties of raster file "Band 4" of year 2020:

# To check the Projection
print(raster.crs)
# Affine transform (how raster is scaled, rotated, skewed, and/or translated)
raster.transform
# To check the dimensions( height and width) 
print(raster.width)
print(raster.height)
# Checking the number of bands
raster.count
# Bounds of the file
raster.bounds
# Checking the Driver (data format)
raster.driver
# No data values for all channels
raster.nodatavals
# Checking all metadata for the whole raster dataset
raster.meta


# To Open the raster file" Band5" of year 2020 using rasterio:
raster = rasterio.open(Band5_2020)

# To Check type of the variable 'raster'
type(raster)

## Verification of raster properties for Band 5 from 2018:

# To check the projection of raster
print(raster.crs)
# Affine transform (how raster is scaled, rotated, skewed, and/or translated)
raster.transform
# Checking dimensions(height, width) of raster 
print(raster.width)
print(raster.height)
# Checking the number of bands
raster.count
# Bounds of the file
raster.bounds
# Checking the Driver (data format)
raster.driver
# No data values for all channels
raster.nodatavals
# Checking all metadata for the whole raster dataset
raster.meta






# To Open the file" Band4_2022" using rasterio module
raster = rasterio.open(Band4_2022)

#  Checking the  "type" of the variable 'raster'
type(raster)

# Examining the properties of raster for Band 4 of year 2022:

# Checking the Projection of raster
print(raster.crs)
# Affine transform (how raster is scaled, rotated, skewed, and/or translated)
raster.transform
# To check the dimensions( height and width)
print(raster.width)
print(raster.height)
# Checking the number of bands
raster.count
# Bounds of the file
raster.bounds
# Checking the Driver (data format)
raster.driver
# No data values for all channels
raster.nodatavals
# Checking all metadata for the whole raster dataset
raster.meta





# Open the raster file"Band5" of year 2022 using rasterio module:
raster = rasterio.open(Band5_2022)

# To Check the "type" of the variable of raster
type(raster)

# Examining raster properties of Band 5 of year 2022:

# Checking the Projection
print(raster.crs)
# Affine transform (how raster is scaled, rotated, skewed, and/or translated)
raster.transform
# Checking the Dimensions( height and width)
print(raster.width)
print(raster.height)
# Checking the number of bands
raster.count
# Bounds of the file
raster.bounds
# Checking the Driver (data format)
raster.driver
# No data values for all channels
raster.nodatavals
# Checking all metadata for the whole raster dataset
raster.meta





# Raster data visualization  from different bands

# Opening all raster files using rasterio module
rasterBand4_2018 = rasterio.open(Band4_2018)
rasterBand5_2018 = rasterio.open(Band5_2018)

rasterBand4_2020 = rasterio.open(Band4_2020)
rasterBand5_2020 = rasterio.open(Band5_2020)

rasterBand4_2022 = rasterio.open(Band4_2022)
rasterBand5_2022 = rasterio.open(Band5_2022)





# Change the reaction of numpy in order to not complain about dividing with zero values
import numpy as np
np.seterr(divide='ignore', invalid='ignore')



# Reading  Band 4 and Band 5 from the year 2018 
with rasterio.open(Band4_2018) as src:
    band4 = src.read(1)  

with rasterio.open(Band5_2018) as src:
    band5 = src.read(1)  

#  Converting the data type of band 4 and band 5 into "float" data type
band4 = band4.astype('float32')
band5 = band5.astype('float32')

# Calculating NDVI(Normalized Difference Vegetation Index) for the year of 2018 using band 4 and band 5
NDVI = (band5 - band4) / (band5 + band4)

#Set the color scaling range for the created NDVI plot
vmin = 0.01
vmax = 1.0

# To Define a color map for the NDVI plot( for better Visualization)
cmap = cm.get_cmap('RdYlGn')

# To Set the figure size
plt.figure(figsize=(8,8))  # Adjust the dimensions as needed

# Visualize and Plot the NDVI with adjusted color scaling and color map
plt.imshow(NDVI, cmap=cmap, vmin=vmin, vmax=vmax)
plt.colorbar(label='NDVI', shrink=0.7)
plt.title("Normalized Difference Vegetation Index of 2018")


# To save the created NDVI plot as a JPEG file format to the already specified directory 
output_filename = "NDVI_2018.jpg"
output_filepath = os.path.join(directory, output_filename)

plt.savefig(output_filepath, format='jpg', dpi=300, bbox_inches='tight')

#Display the plot
plt.show()

# To read Band 4 and Band 5 from the year of 2020 
with rasterio.open(Band4_2020) as src:
    band4 = src.read(1)  

with rasterio.open(Band5_2020) as src:
    band5 = src.read(1)  

#Converting raster data type into float data type
band4 = band4.astype('float32')
band5 = band5.astype('float32')

# To Calculate NDVI for the year of 2020 using band 4 and band 5
NDVI = (band5 - band4) / (band5 + band4)

# To set the color scaling range for the created NDVI plot
vmin = 0.01
vmax = 1.0

# To Define a color map for the NDVI plot
cmap = cm.get_cmap('RdYlGn')

# Set the figure size
plt.figure(figsize=(10, 10))  

# Plotting and visualizing the resulted  NDVI with adjusted color scaling and color map
plt.imshow(NDVI, cmap=cmap, vmin=vmin, vmax=vmax)
plt.colorbar(label='NDVI', shrink=0.7)
plt.title("Normalized Difference Vegetation Index of 2020")


#  To save the NDVI plot as a JPEG file format to the directory 
output_filename = "NDVI_2020.jpg"
output_filepath = os.path.join(directory, output_filename)

plt.savefig(output_filepath, format='jpg', dpi=300, bbox_inches='tight')

#Display the plot

plt.show()



#Reading  Band 4and Band 5 of the year 2022 
with rasterio.open(Band4_2022) as src:
    band4 = src.read(1)  

with rasterio.open(Band5_2022) as src:
    band5 = src.read(1)  

# To convert the data type into float data type
band4 = band4.astype('float32')
band5 = band5.astype('float32')

#Calculate NDVI for year 2022 using band 4 and band 5
NDVI = (band5 - band4) / (band5 + band4)

# To Set the color scaling range for the NDVI plot
vmin = 0.01
vmax = 1.0

# Define a color map for the created NDVI plot
cmap = cm.get_cmap('RdYlGn')

# To Set the figure size
plt.figure(figsize=(10, 10))  

# Visualize the created NDVI with adjusted color scaling and color map
plt.imshow(NDVI, cmap=cmap, vmin=vmin, vmax=vmax)
plt.colorbar(label='NDVI', shrink=0.7)
plt.title("Normalized Difference Vegetation Index of 2022")


# To Save the plot of created NDVI as a JPEG file to the directory 
output_filename = "NDVI_2022.jpg"
output_filepath = os.path.join(directory, output_filename)

plt.savefig(output_filepath, format='jpg', dpi=300, bbox_inches='tight')

#Display the plot
plt.show()



# To create an interactive map of Area of Interest(Kasauli) 
# Creating an interactive map with the center at the location  tiles from the OpenStreetMap (default), here we have given coordinates of our area of interest
Map = folium.Map(location=[30.8986, 76.9659], zoom_start=8, control_scale=True)

# To Add a red marker for the location of Kasauli,Solan, Himachal pradesh,India (30.8986, 76.9659), enable popup with the name of the town
folium.Marker(location=[30.8986, 76.9659],
	      popup='Change detection kasauli, solan, Himachal Pardesh India',
	      icon=folium.Icon(color='red', icon='ok-sign'),
).add_to(Map)


# Exporting the map as HTML to the directory 

filename = "map.html"
output_fp = os.path.join(directory, filename)
Map.save(output_fp)

# To show the map
Map
