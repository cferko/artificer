from scipy.io import wavfile
import os
from audio_functions import *

samples=[]
identity_label = []
annoyed_label = []

features = []

for f in os.listdir('../audio/'):
    this_name = f.split('.')[0]
    creature_name = this_name.split('_')[0]
    annoyed = ("annoyance" in this_name)
    
    identity_label.append(creature_name)
    annoyed_label.append(annoyed)    
    
    rate, x = wavfile.read('../audio/'+f)
    samples.append((this_name, rate, x))

for sample in samples:
    this_x = sample[2]
    this_zcr = stZCR(this_x)
    this_energy = stEnergy(this_x)
    this_entropy = stEnergyEntropy(this_x)

    features.append([this_zcr, this_energy, this_entropy])