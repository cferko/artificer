import IPython
from IPython.display import Audio as listen
import numpy as np
from scipy.io import wavfile

from IPython import get_ipython
ipython = get_ipython()
ipython.magic("matplotlib inline")

male_rate, male_audio = wavfile.read("../../audio/male_sample.wav")
female_rate, female_audio = wavfile.read("../../audio/female_sample.wav")

male_audio = np.mean(male_audio, axis=1)
female_audio = np.mean(female_audio, axis=1)

from matplotlib.pyplot import *
from numpy.fft import rfft as raw_fft

def fft(audio_sample):
    rfft_output = raw_fft(audio_sample)
    return [sqrt(i.real**2 + i.imag**2)/len(rfft_output) for i in rfft_output]
    
def fft_freq(audio_sample):
    rate = 22050
    num_samples = len(audio_sample)
    return [(i*1.0/num_samples)*sample_rate for i in range(num_samples/2+1)]
    
def get_male_example():
    return male_audio
    
def get_female_example():
    return female_audio

def listen(audio):

    if np.array_equal(audio, male_audio):
        return IPython.display.Audio("../../audio/male_sample.wav")
        
    elif np.array_equal(audio, female_audio):
        return IPython.display.Audio("../../audio/female_sample.wav")
    
    else:
        return IPython.display.Audio(audio, rate = 22050)