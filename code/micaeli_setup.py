import IPython
from IPython.display import Audio as listen
from scipy.io import wavfile

%matplotlib inline
from matplotlib.pyplot import *
import np.fft.rfft as raw_fft

def fft(audio_sample):
    return [sqrt(i.real**2 + i.imag**2)/len(rfft_output) for i in rfft_output]
    
def fft_freq(audio_sample):
    rate = 22050
    num_samples = len(audio_sample)
    return [(i*1.0/num_samples)*sample_rate for i in range(num_samples/2+1)]
    
