import pytesseract 
from googlesearch import *      
import timeit
import time
import webbrowser
import urllib3
import urllib.request
import requests
import cv2
import numpy as np
from PIL import Image  

def ocr():
    start_time = time.time()
    # adds image processing capabilities 
    img = Image.open('NewPicture.png')
    pytesseract.pytesseract.tesseract_cmd =r'C:/Program Files/Tesseract-OCR/tesseract.exe'
    query = pytesseract.image_to_string(img) 
    #query="Former Australian captain Mark Taylor has had several nicknames over his playing career. Which of the following was NOT one of them?"
    #iexplorer_path = r'C:\Program Files (x86)\Internet Explorer\iexplore.exe %s'
    chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
    for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
     webbrowser.open("https://google.com/search?q=%s" % query)
    print(img)
    print("--- %s seconds ---" % (time.time() - start_time))
ocr()