import cv2
import numpy as np
import json
import os
root = os.path.dirname(os.path.realpath(__file__))
print root,os.path.realpath(__file__)
data_dir = os.path.join(root,"data")
test_dir = os.path.join(root,"test")

model = cv2.createLBPHFaceRecognizer()

train_data = []
train_label = []
label_list = []


def identify(data):
    a = np.asarray(bytearray(data), dtype=np.uint8)
    b = cv2.imdecode(a, cv2.IMREAD_UNCHANGED)
    b = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)

    [res, confidence] = model.predict(b)

    return json.dumps({
        "id": label_list[res],
        "url":"https://api.shopstyle.com/action/apiVisitRetailer?id="+label_list[res]+"&pid=uid7616-38024704-23"
        "size": b.shape,
        "version": cv2.__version__,

    })


print "TRAINING DATABASE..."

for subdir, dirs, files in os.walk(data_dir):

    for file in files:
        path = os.path.join(subdir, file)

        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        label = subdir[len(data_dir) + 1:]
        train_data.append(np.asarray(img, dtype=np.uint8))

        if label not in label_list:
            label_list.append(label)

        train_label.append(label_list.index(label))

        print "ADDING:", path, label

model.train(np.asarray(train_data), np.asarray(train_label))

print "Train done!"

if __name__ == "__main__":
    total_count = 0
    correct_count = 0
    for subdir, dirs, files in os.walk(test_dir):
        for file in files:
            path = os.path.join(subdir, file)

            img = open(path, 'rb').read()
            label = file.split(".")[0].split("_")[0]

            total_count += 1
            print label, json.loads(identify(img))['id']
            if label == json.loads(identify(img))['id']:
                correct_count += 1
    print "Total Test:", total_count, "Correct Count:", correct_count
