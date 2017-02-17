import cv2
import numpy as np
import json
def identify(data):
    a = np.fromstring(data)

    return json.dumps({
        "id":66666,
        "size":len(data),
        "version":cv2.__version__
    })