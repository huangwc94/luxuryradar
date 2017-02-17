import cv2
import numpy as np
import json


def identify(data):
    a = np.asarray(bytearray(data), dtype=np.uint8)
    b = cv2.imdecode(a, cv2.IMREAD_UNCHANGED)

    print b.shape


    return json.dumps({
        "id": 127624791,
        "size": b.shape,
        "version": cv2.__version__,

    })


if __name__ == "__main__":
    f = open("foo.jpg", "rb")
    print identify(f.read())
