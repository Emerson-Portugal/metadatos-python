import exifread
import urllib.parse

# Open the image file for reading (binary mode)
f = open("./img/Foto2.jpg", "rb")

# Return Exif tags
tags = exifread.process_file(f)

# Get latitude and longitude values from the metadata
lat = tags.get("GPS GPSLatitude")
lon = tags.get("GPS GPSLongitude")

# Construct a Google Maps URL using the latitude and longitude values
url = f"https://maps.google.com/?q={lat},{lon}"

# Write the metadata and URL to a text file
with open('metadata.txt', 'w') as file:
    for tag in tags.keys():
        if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
            file.write(f"{tag:25}: {tags[tag]}\n")
    file.write(f"\nGoogle Maps URL: {url}\n")

# Close the file
f.close()
