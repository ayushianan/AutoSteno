import os
import pickle as cPickle
import numpy as np
from scipy.io.wavfile import read
from featureextraction import extract_features
#from speakerfeatures import extract_features
import warnings
warnings.filterwarnings("ignore")
import time
import os.path as path

#path to training data
source   = "SampleData/"   
#path where training speakers will be saved
modelpath = "Speakers_models/"

gmm_files = [os.path.join(modelpath,fname) for fname in os.listdir(modelpath) if fname.endswith('.gmm')]

#Load the Gaussian gender Models
models    = [cPickle.load(open(fname,'r')) for fname in gmm_files]
speakers   = [fname.split("/")[-1].split(".gmm")[0] for fname in gmm_files]

print "Audio: speech.wav"
root=path.abspath(path.join(__file__ ,"../.."))
fname="\speech.wav"
sr,audio = read(root+fname)
vector   = extract_features(audio,sr)
 
log_likelihood = np.zeros(len(models)) 

for i in range(len(models)):
    gmm    = models[i]  #checking with each model one by one
    scores = np.array(gmm.score(vector))
    log_likelihood[i] = scores.sum()

winner = np.argmax(log_likelihood)
print "detected as - ", speakers[winner]

time.sleep(1.0)