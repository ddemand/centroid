import geopandas as gpd
from shapely.geometry import Polygon

# Define your three coordinate pairs (longitude, latitude)
coords = [
    (-101.606709, 48.231550),  # ND
    (-109.772232, 47.10535),  # MT
    (-103.893143, 41.231061)   # NE
]

# Create a Polygon from the coordinates
polygon = Polygon(coords)

# Create a GeoDataFrame with the polygon
gdf = gpd.GeoDataFrame(index=[0], geometry=[polygon], crs="EPSG:4326")

# Calculate the centroid
centroid = gdf.centroid.iloc[0]

# Extract longitude and latitude of centroid
centroid_lon, centroid_lat = centroid.x, centroid.y

# Print results
print(f"Input Coordinates:")
for i, (lon, lat) in enumerate(coords, 1):
    print(f"Point {i}: ({lon}, {lat})")
print(f"\nCentroid Coordinates:")
print(f"Longitude: {centroid_lon:.6f}")
print(f"Latitude: {centroid_lat:.6f}")