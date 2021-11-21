from google.cloud import vision
import io
import timeit
import time
import os    
import timeit
import time
import webbrowser

def get_document_bounds(response, feature):
    document = response.full_text_annotation
    bounds=[]
    for i,page in enumerate(document.pages):
        for block in page.blocks:
            if feature=="FeatureType.BLOCK":
                bounds.append(block.bounding_box)
            for paragraph in block.paragraphs:
                if feature=="FeatureType.PARA":
                    bounds.append(paragraph.bounding_box)
                for word in paragraph.words:
                    for symbol in word.symbols:
                        if (feature == "FeatureType.SYMBOL"):
                            bounds.append(symbol.bounding_box)
                    if (feature == "FeatureType.WORD"):
                        bounds.append(word.bounding_box)
    return bounds
def draw_boxes(image, bounds, color,width=5):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        draw.line([
            bound.vertices[0].x, bound.vertices[0].y,
            bound.vertices[1].x, bound.vertices[1].y,
            bound.vertices[2].x, bound.vertices[2].y,
            bound.vertices[3].x, bound.vertices[3].y,
            bound.vertices[0].x, bound.vertices[0].y],fill=color, width=width)
    return image
def detect(num):
    start_time = time.time()
    list1=[]
    b=""
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="key.json"
    client = vision.ImageAnnotatorClient()
    color = (255, 0, 0)
    path = "test2.jpg".format(num)
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    bounds=get_document_bounds(response,"FeatureType.WORD")
    for bound in bounds:
        cv2.rectangle(image,
                    (bound.vertices[0].x, bound.vertices[0].y),
                    (x + w, y + h),
                    (0, 0, 255), 2)

    print(bounds)
    #print(response)
    texts = response.text_annotations
    print('Texts:')
    words=[]
    xi=[]
    yi=[]
    wi=[]
    hi=[]
    for text in texts:
        print('\n"{}"'.format(text.description))
        
        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])
        print(vertices)
        #verti='{}'.format(','.join(vertices)))
        #print('bounds: {}'.format(','.join(vertices)))
    #for text in response.text_annotations:
       # list1.append(text.description)
    
    #print(list1)
   # b=list1[0]
    cv2.imshow('Detected text', img)
    cv2.waitKey(0)
    
detect(0)
