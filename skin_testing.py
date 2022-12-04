import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
image1=cv2.imread("E:/Jupyter/datatree/train/akiec/ISIC_0026171.jpg")
from tensorflow.keras.preprocessing import image
model=load_model("E:/Jupyter/datatree/skin.h5")
test_image=image.load_img('E:/Jupyter/datatree/train/akiec/ISIC_0026171.jpg',target_size=(64,64))
test_image=image.img_to_array(test_image)
test_image=np.expand_dims(test_image,axis=0)
result=model.predict(test_image)
#classIds,confs,bbox=model.predict(test_image)
#print(classIds,confs)
#net=cv2.dnn_DetectionModel('E:/Jupyter/datatree/skin.h5')
#classIds,confs,bbox=net.detect(test_image)
#print(classIds,confs)
#training_set.class_indices

if result[0][0]==1:
    print(" This is an Actinic keratoses and intraepithelial carcinoma")
    cv2.putText(image1, 'Akiec', (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
elif result[0][1]==1:
    print("This is Basal cell carcinoma ")
    #for (x, y, w, h) in image1:
     #   cv2.rectangle(image1, (x, y, x + w, y + h), (0, 255, 255), 2)
    cv2.putText(image1, ' Basal cell carcinoma', (40, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
elif result[0][2]:
    print(" This is Benign lesions of the keratosis.")
    cv2.putText(image1, 'BLK', (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
elif result[0][3]==1:
    print("This is an Dermatofibroma")
    cv2.putText(image1, 'Dermatofibroma', (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
elif result[0][4]==1:
    print(" This is an melanoma")
    cv2.putText(image1, 'melanoma', (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
elif result[0][5]==1:
    print(" This an Nervus Pigmentosus")
    cv2.putText(image1, 'NP', (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
elif result[0][6]==1:
    print(" This is an vascular lesions")
    cv2.putText(image1, 'Vl', (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
cv2.imshow("Image",image1)
cv2.waitKey(10000)

