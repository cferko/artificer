from __future__ import division

import subprocess
from IPython.core.magic import (Magics, magics_class, line_magic,
                                cell_magic, line_cell_magic)
import os         
from datetime import datetime
import pandas as pd
import pexpect

import IPython
from IPython.display import Audio
import numpy as np
from scipy.io import wavfile

import matplotlib.pyplot as plt

from IPython import get_ipython
ipython = get_ipython()
ipython.magic("matplotlib inline")

import seaborn as sns
sns.set_context("notebook")

from matplotlib.pyplot import *
from numpy.fft import rfft as raw_fft

def standardize(old_rate, audio):
    if audio.ndim == 2:
        audio = audio.mean(axis=1)
    
    if old_rate == 44100:
        return audio

    n = len(audio)
    upsample_factor = float(old_rate)/44100
    new_audio = np.interp(np.arange(0, n, upsample_factor),
                          np.arange(0, n, 1), audio)

    return new_audio
    
def frequency_domain(audio_sample):
    rfft_output = raw_fft(audio_sample)
    strengths = [np.sqrt(i.real**2 + i.imag**2)/len(rfft_output) for i in rfft_output]

    rate=44100
    num_samples = len(audio_sample)
    freqs = [(i*1.0/num_samples)*rate for i in range(num_samples/2+1)]
    
    ## Keep only first 5000 for simplicity
    strengths = np.array(strengths[:5000])
    freqs = np.array(freqs[:5000])
    
    return freqs, strengths
    

def get_male_example():
    male_rate, male_audio = wavfile.read("../../audio/male_sample.wav")
    return standardize(male_rate, male_audio)
    
def get_female_example():
    female_rate, female_audio = wavfile.read("../../audio/female_sample_two.wav")
    return standardize(female_rate, female_audio)

def get_aberrant_example():
    aberrant_rate, aberrant_audio = wavfile.read("../../audio/queen_annoyance3.wav")
    return standardize(aberrant_rate, aberrant_audio)

def get_concert_A():
    note_rate, note_audio = wavfile.read("../../audio/concert_a.wav")
    return standardize(note_rate, note_audio)

def get_c_major_scale():
    scale_rate, scale_audio = wavfile.read("../../audio/c_major_scale.wav")
    return standardize(scale_rate, scale_audio)

def get_chord_example():
    chord_rate, chord_audio = wavfile.read("../../audio/major_triad.wav")
    return standardize(chord_rate, chord_audio)

def listen(audio):
    return IPython.display.Audio(audio, rate = 44100)
        
def frequency_domain_demo():
    from IPython.display import HTML
    video_encoded = open("../../images/fourier.mp4", "rb").read().encode("base64")
    video_tag = '<video controls alt="test" src="data:video/{0};base64,{1}">'.format("mp4", video_encoded)
    return HTML(data=video_tag)

def my_specgram(x, NFFT=256, Fs=2, Fc=0, detrend=mlab.detrend_none,
             window=mlab.window_hanning, noverlap=128,
             cmap=None, xextent=None, pad_to=None, sides='default',
             scale_by_freq=None, minfreq = None, maxfreq = None, **kwargs):
    #####################################
    # modified  axes.specgram() to limit
    # the frequencies plotted
    #####################################

    # this will fail if there isn't a current axis in the global scope
    ax = gca()
    Pxx, freqs, bins = mlab.specgram(x, NFFT, Fs, detrend,
         window, noverlap, pad_to, sides, scale_by_freq)

    # modified here
    #####################################
    if minfreq is not None and maxfreq is not None:
        Pxx = Pxx[(freqs >= minfreq) & (freqs <= maxfreq)]
        freqs = freqs[(freqs >= minfreq) & (freqs <= maxfreq)]
    #####################################

    Z = 10. * np.log10(Pxx)
    Z = np.flipud(Z)

    if xextent is None: xextent = 0, np.amax(bins)
    xmin, xmax = xextent
    freqs += Fc
    extent = xmin, xmax, freqs[0], freqs[-1]
    im = ax.imshow(Z, cmap, extent=extent, **kwargs)
    ax.axis('auto')

    return Pxx, freqs, bins, im

def spectrogram(audio):    
    f, ax = plt.subplots()

    if (np.array_equal(audio, get_c_major_scale()) or 
        np.array_equal(audio, get_concert_A()) or
        np.array_equal(audio, get_chord_example()) ):
        max_freq = 7000
    
    else:
        max_freq = 15000
    
    Pxx, freqs, bins, im = my_specgram(audio, Fs=44100, cmap="jet", 
                                      minfreq=0, maxfreq=max_freq)
    return    
    
def compare_speech():
    male_audio = get_male_example()
    female_audio = get_female_example()
    aberrant_audio = get_aberrant_example()
    
    f, axarr = plt.subplots(3)
    axarr[0].specgram(female_audio, Fs=44100, cmap="jet")
    axarr[0].set_title('Female Spectrogram')
    axarr[1].specgram(male_audio, Fs=44100, cmap='jet')
    axarr[1].set_title('Male Spectrogram')
    axarr[2].specgram(aberrant_audio, Fs=44100, cmap='jet')
    axarr[2].set_title('Aberrant Spectrogram')

@magics_class
class MyMagics(Magics):

    @line_magic
    def checkpoint(self, line):
        """For signup, just save name if it exists
        """
        try:                
            print "Checkpoint complete."
        
        except:
            print "Christian made a mistake."

def commit():
    subprocess.call("""cd /home/main/notebooks/logs/micaeli;
                     git config --global user.email "ferko7@hotmail.com";
                     git config --global user.name "jttalks";
                     git pull""", shell=True)
    
    
    ## Change this to get the index corresponding to this character
    my_indices = [int(f) for f in os.listdir('/home/main/notebooks/logs/') if '.' not in f]

    timestamp = datetime.now().ctime()
    
    ## Change this to the relevant data
    my_data = pd.Series([me.real_name,
                         me.character_name,
                         me.email,
                         me.race,
                         me.house,
                         timestamp])
    
    my_data.to_csv("/home/main/notebooks/records/"+new_index,
                   index=False)
                   
    subprocess.call("""cd /home/main/eldritch-signup/records/;
                      git add *;
                      git commit -m "ADD: signup" """, shell=True)
                     
    pexpect.run('git push -u origin master', 
                cwd='/home/main/notebooks/logs/',
               events={'Username*':'jttalks\n', 'Password*':'jttalks1\n'})    
        
if __name__ == "__main__":
    ip = get_ipython()
    ip.register_magics(MyMagics)
    
    me = Character()
    
    print "Micaeli setup complete."
    
