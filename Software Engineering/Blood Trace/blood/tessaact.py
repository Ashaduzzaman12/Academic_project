import pytesseract as pyt
import cv2

img = cv2.imread("masud.png")

pyt.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

text = pyt.image_to_string(img)

print(text)

with open("text00.txt","w+") as f:
    f.write(text) 
