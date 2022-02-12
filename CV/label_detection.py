from mimetypes import init
from typing import Any
from google.cloud import vision
import asyncio

detector = None

class ImageAnnotator:
    def __init__(self):
        self.client = vision.ImageAnnotatorClient()

    def get_labels(self, content:bytes)-> list[Any]: 
        image = vision.Image(content=content)
        response = self.client.label_detection(image=image)
        labels = list(map(lambda x:{
            "description":x.description,
            "score": x.score
        }, response.label_annotations))
        
        return labels

async def async_init():
    global detector
    detector = ImageAnnotator()
    print("client inited")

def init():
    asyncio.run(async_init())
    


if __name__ == '__main__':
    import io
    with io.open("./wakeupcat.jpeg", 'rb') as image_file:
        content = image_file.read()
    detector = ImageAnnotator()
    labels = detector.get_labels(content)
    print(labels)
