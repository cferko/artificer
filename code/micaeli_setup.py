import IPython
from IPython.display import Audio
import numpy as np
from scipy.io import wavfile

import matplotlib.pyplot as plt

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

def get_aberrant_example():
    aberrant_rate, aberrant_audio = wavfile.read("../../audio/queen_annoyance3.wav")
    return aberrant_audio

def listen(audio):
    if np.array_equal(audio, male_audio):
        return IPython.display.Audio("../../audio/male_sample.wav")
        
    elif np.array_equal(audio, female_audio):
        return IPython.display.Audio("../../audio/female_sample.wav")
    
    else:
        return IPython.display.Audio(audio, rate = 22050)
        
def frequency_domain_demo():
    from IPython.display import HTML
    video_encoded = open("../../images/fourier.mp4", "rb").read().encode("base64")
    video_tag = '<video controls alt="test" src="data:video/{0};base64,{1}">'.format("mp4", video_encoded)
    return HTML(data=video_tag)
    
def compare_speech():
    f, axarr = plt.subplots(2, sharex=True)
    axarr[0].specgram(female_audio)
    axarr[0].set_title('Female Spectrogram')
    axarr[1].specgram(male_audio)
    axarr[1].set_title('Male Spectrogram')