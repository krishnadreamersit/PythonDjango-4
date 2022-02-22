# https://github.com/UB-Mannheim/tesseract/wiki
# Download and Install tesseract Windows App (32 bits)

import cv2 # pip install opencv-python
import pytesseract # pip install pytesseract

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
# tmp_text = pytesseract.image_to_string('image_1.png')
# tmp_text = pytesseract.image_to_string('image_2.jpg')
# tmp_text = pytesseract.image_to_string('image_3.png')
tmp_text = pytesseract.image_to_string('image_4.jpg')
print(tmp_text)
# Complete Read - No
# Optimized - No
# We need to create our own library (OCR)

# NLP - Natural Language Processing