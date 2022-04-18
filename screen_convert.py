"""Convert an image to RGBA format which can be used on DJI goggles."""
import argparse
from PIL import Image, UnidentifiedImageError

expectedWidth = 1440
expectedHeight = 810

parser = argparse.ArgumentParser(
    description='Convert image for DJI HD FPV goggles.')
parser.add_argument('inputPath', metavar='INPUT_PATH',
                    help='path to the image to be converted')
parser.add_argument('outputPath', metavar='OUTPUT_PATH',
                    help='path to the result image')
args = parser.parse_args()

# Try to load the image
try:
    im = Image.open(args.inputPath)
except UnidentifiedImageError:
    print('Could not open image, sure it is actually an image?')
    exit(1)

# Make sure that the size matches
width, height = im.size
if width == expectedWidth and height == expectedHeight:
    # Swap R and B channel
    converted = im.convert('RGBA')
    for x in range(width):
        for y in range(height):
            pixel = converted.getpixel((x, y))
            red, green, blue, alpha = pixel
            converted.putpixel((x, y), (blue, green, red, alpha))

    # Convert to bytes and write
    converted = converted.tobytes()
    targetFile = open(args.outputPath, "wb")
    targetFile.write(converted)
else:
    print('Image resolution does not match. Should be %dx%d' %
          (expectedWidth, expectedHeight))
    exit(1)
