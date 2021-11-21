import cv2
import pytesseract
from pytesseract import Output
import numpy as np
from translate_util.translate_tool import translate_other2cn,translate_other2en
from PIL import ImageFont, ImageDraw, Image
img = cv2.imread('test.png')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
color = (255, 0, 0) 
from translate import Translator
translator= Translator(to_lang="ja")

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\I554872\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
results = pytesseract.image_to_data(rgb, output_type=Output.DICT)

for i in range(0, len(results["text"])):

    x = results["left"][i]
    y = results["top"][i]
    w = results["width"][i]
    h = results["height"][i]

    text = results["text"][i]
    conf = int(float(results["conf"][i]))
      
    if conf > 0:
        print("Confidence: {}".format(conf))
        print("Text: {}".format(text))
        print("")
        text = "".join(text).strip()
        print(text)
        try: 
          text= translator.translate(text)

        except:
          print(":")
        print(text)
        cv2.rectangle(img,
                    (x, y),
                    (x + w, y + h),
                    (0, 0, 255), 2)

        fontpath = "./simsun.ttc"     
        font = ImageFont.truetype(fontpath,20)
        img_pil = Image.fromarray(img)
        draw = ImageDraw.Draw(img_pil)
        draw.text((x, y - 10),  text, font = font,fill = color) 
        img = np.array(img_pil)   
                 
       # cv2.putText(img,
                   # text,
                 #   ,
                 #   cv2.FONT_HERSHEY_SIMPLEX,
                  #  0.5, (0, 255, 255), 1) 

cv2.imshow('Detected text', img)
cv2.waitKey(0)