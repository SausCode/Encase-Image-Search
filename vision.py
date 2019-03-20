import io
import os
import imagemounter
import sys
from glob import glob

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Import the Pillow Library
from PIL import Image

if len(sys.argv) < 3:
	print("Usage: vision.py encase_file_name google_credentials.json")
	exit()
else:
	encase_file = sys.argv[1]
	credential_path = sys.argv[2]

parser = imagemounter.ImageParser([encase_file])

for volume in parser.init():
	print(volume.get_description())
	volume.unmount()

index = raw_input("Enter the volume you want to search in: ")
volume = parser.get_by_index(index)
volume.init()
volume.mount()

result = []

for root, dirs, files in os.walk(volume.mountpoint):
	for file in files:
		if file.endswith((".jpg", ".png", ".gif")):
			result.append(os.path.join(root, file))

print("There are:", len(result), "images that will be searched.")

# Instantiates a client
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
client = vision.ImageAnnotatorClient()

tags = {}
show_file_name = raw_input("Press y(es) if you would like to see file names: ")
max_searches = raw_input("Enter max number of Google Cloud queries or nothing for unlimited: ")

try:
	os.chdir("/tmp")
	i = 0
	for file_name in result:
		# currently limit to 1000 queries as it costs a good amount
		# of money
		if max_searches is not None:
			if i > int(max_searches):
				break
		absolute_path = file_name
		file_name = "/".join(file_name.split("/")[2:])
		if show_file_name is "y" or show_file_name is "yes":
			print(file_name)

		# Loads the image into memory
		with io.open(file_name, 'rb') as image_file:
		    content = image_file.read()

		image = types.Image(content=content)

		# Performs label detection on the image file
		response = client.label_detection(image=image)
		labels = response.label_annotations

		for label in labels:
			label.description = label.description.lower()
			tags.setdefault(label.description, [])
			tags[label.description].append(absolute_path)
		i = i + 1
except Exception as e:
	print(e)

see_labels = raw_input("Press y(es) if you would like to see found labels: ")
if see_labels is "y" or see_labels is "yes":
	for key in tags:
		print(key)

while True:
	search = raw_input("Enter a search term or press enter to exit: ").lower()
	if search is None or search is "":
		break
	if search not in tags:
		print("Search term:", search, "is not in tags.")
	else:
		see_raw_images = raw_input("Press y(es) if you would like to see the images: ")
		for s in tags[search]:
			print(s)
			if see_raw_images is "y" or see_raw_images is "yes":
				Image.open(s).show()

parser.clean()