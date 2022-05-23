import librosa
import numpy as np
from tensorflow import keras
from tensorflow.keras.models import Sequential
import os
model=Sequential()
model = keras.models.load_model('savedModel.bin')

def vyhodnot(filename):
    audio, sample_rate = librosa.load(filename, res_type='kaiser_fast') 
    mfccs_features = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    mfccs_scaled_features = np.mean(mfccs_features.T,axis=0)

    #print(mfccs_scaled_features)
    mfccs_scaled_features=mfccs_scaled_features.reshape(1,-1)
    #print(mfccs_scaled_features)
    #print(mfccs_scaled_features.shape)
    predicted_label=model.predict(mfccs_scaled_features)
    #predicted_label[0]=[round(predicted_label[0]),round(predicted_label[1])]
    #print(predicted_label)
    #prediction_class = labelencoder.inverse_transform(predicted_label) 
    #prediction_class
    print('spacek' if predicted_label[0][1] > predicted_label[0][0] else 'neco jineho')

import subprocess
while True:
    os.system("arecord -D plughw:3,0 --duration=15 test.wav")
    vyhodnot("test.wav")