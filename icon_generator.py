# using utf-8
import os
import sys
import json
from PIL import Image

JSON_STRING = '''
{
  "images" : [
    {
      "idiom" : "iphone",
      "scale" : "2x",
      "size" : "20x20"
    },
    {
      "idiom" : "iphone",
      "scale" : "3x",
      "size" : "20x20"
    },
    {
      "idiom" : "iphone",
      "scale" : "2x",
      "size" : "29x29"
    },
    {
      "idiom" : "iphone",
      "scale" : "3x",
      "size" : "29x29"
    },
    {
      "idiom" : "iphone",
      "scale" : "2x",
      "size" : "40x40"
    },
    {
      "idiom" : "iphone",
      "scale" : "3x",
      "size" : "40x40"
    },
    {
      "idiom" : "iphone",
      "scale" : "2x",
      "size" : "60x60"
    },
    {
      "idiom" : "iphone",
      "scale" : "3x",
      "size" : "60x60"
    },
    {
      "idiom" : "ipad",
      "scale" : "1x",
      "size" : "20x20"
    },
    {
      "idiom" : "ipad",
      "scale" : "2x",
      "size" : "20x20"
    },
    {
      "idiom" : "ipad",
      "scale" : "1x",
      "size" : "29x29"
    },
    {
      "idiom" : "ipad",
      "scale" : "2x",
      "size" : "29x29"
    },
    {
      "idiom" : "ipad",
      "scale" : "1x",
      "size" : "40x40"
    },
    {
      "idiom" : "ipad",
      "scale" : "2x",
      "size" : "40x40"
    },
    {
      "idiom" : "ipad",
      "scale" : "1x",
      "size" : "76x76"
    },
    {
      "idiom" : "ipad",
      "scale" : "2x",
      "size" : "76x76"
    },
    {
      "idiom" : "ipad",
      "scale" : "2x",
      "size" : "83.5x83.5"
    },
    {
      "idiom" : "ios-marketing",
      "scale" : "1x",
      "size" : "1024x1024"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
'''
ICON_DIR_NAME = "AppIcon.appiconset"
JSON_FILE_NAME = "Contents.json"

if len(sys.argv) < 3 :
    print("argument error.\nexpamle: python icon_generator.py my_icon.png ./dir")
    sys.exit(-1)

input_file = sys.argv[1]
output_dir = sys.argv[2]
dest_dir = os.path.join(output_dir, ICON_DIR_NAME)
json_file_path = os.path.join(dest_dir, JSON_FILE_NAME)

if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)

input_image = Image.open(input_file)
info_map = json.loads(JSON_STRING)
icon_array = info_map["images"]
output_map = info_map
output_map["images"] = []
for icon in icon_array:
    output_icon = icon
    idiom = icon["idiom"]
    scale = icon["scale"]
    size = icon["size"]
    output_width = int(float(size[:size.find("x")]) * float(scale[:scale.find("x")]))
    output_height = output_width
    output_image = input_image.resize((output_width, output_height))
    output_name = idiom + scale + "@" + size + ".png"
    output_path = os.path.join(dest_dir, output_name)
    output_image.save(output_path, "png")
    output_image.close()
    output_icon["filename"] = output_name
    output_map["images"].append(output_icon)

json_file = open(json_file_path, "w")
json_file.write(json.dumps(output_map))
json_file.close()

input_image.close()

