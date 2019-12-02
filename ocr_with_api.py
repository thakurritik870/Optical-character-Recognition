import cv2
import numpy as np
import requests
import io
import json

img = cv2.imread("image.jpeg")
height, width, _ = img.shape

# Cutting image
# roi = img[0: height, 400: width]
roi = img

# Ocr engine
url_api = "https://api.ocr.space/parse/image"
_, compressedimage = cv2.imencode(".jpeg", roi, [1, 90])
file_bytes = io.BytesIO(compressedimage)

result = requests.post(url_api,
              files = {"image.jpeg": file_bytes},
              data = {"apikey": "8001a68e3a88957",
                      "language": "eng"})

result = result.content.decode()
result = json.loads(result)


parsed_results = result.get("ParsedResults")[0]
text_detected = parsed_results.get("ParsedText")
print(text_detected)


cv2.imshow("roi", roi)
cv2.imshow("Img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()