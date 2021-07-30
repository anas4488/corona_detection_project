
# from keras.models import load_model
# from keras.preprocessing import image
import numpy as np
# import tensorflow as tf 
import joblib
import cv2
# model = tf.keras.models.load_model('mymodel.h5')
data = joblib.load('model_joblib.h5')
# model.compile(loss='binary_crossentropy',optimizer='rmsprop',metrics=['accuracy'])

def read_image(file_path):
    img = cv2.imread(file_path, cv2.IMREAD_COLOR)
    return cv2.resize(img, (ROWS, COLS), interpolation=cv2.INTER_CUBIC)

def sigmoid(z):
    s = 1/(1+np.exp(-z))
    return s

def predict(w, b, X):    
    m = X.shape[1]
    Y_prediction = np.zeros((1, m))
    w = w.reshape(X.shape[0], 1)
    
    z = np.dot(w.T, X) + b
    A = sigmoid(z)
    
    for i in range(A.shape[1]):
        # Convert probabilities A[0,i] to actual predictions p[0,i]
        if A[0,i] > 0.5:
            Y_prediction[[0],[i]] = 1
        else: 
            Y_prediction[[0],[i]] = 0
    
    return Y_prediction

ROWS = 64
COLS = 64
CHANNELS = 3
    
def predictwin(my_dic):

    my_image = read_image(my_dic).reshape(1, ROWS*COLS*CHANNELS).T
    my_predicted_image = predict(data["w"], data["b"], my_image)
    res = np.squeeze(my_predicted_image)
    print(res)
    if res == 0.0:
        ans = "The image you provided contains corona"
    else:
        ans = "The image you provided does not contains corona"
    res = int(res)
    print(res)
    return res
	# c = my_dic
	# img = image.load_img(c, target_size=(150, 150))
	# x = image.img_to_array(img)
	# x = np.expand_dims(x, axis=0)
	# images = np.vstack([x])
	# classes = model.predict_classes(images, batch_size=10)
	
	# return classes


