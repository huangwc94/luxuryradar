import cv2
import numpy as np
import json
def identify(data):
    a = np.fromstring(data,np.uint32)


    return json.dumps({
        "id":62346,
        "size":len(data),
        "version":cv2.__version__
    })

if __name__ == "__main__":
    f = open("foo.jpg","rb")
    print identify(f.read())