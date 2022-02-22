from PIL import Image # pip install Pillow
import sys
try:
    image_data = Image.open('image_1.png')
    image_data.show()
except:
    print("Error : ", sys.exc_info()[1])
finally:
    del image_data

# https://pillow.readthedocs.io/en/stable/