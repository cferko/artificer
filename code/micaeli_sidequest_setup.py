import numpy as np
import random
import itertools
#import scipy.signal.sawtooth

from numpy.fft import rfft, irfft

def ms(x):
    """Mean value of signal `x` squared.
    :param x: Dynamic quantity.
    :returns: Mean squared of `x`.
    """
    return (np.abs(x)**2.0).mean()

def normalize(y, x=None):
    """normalize power in y to a (standard normal) white noise signal.
    Optionally normalize to power in signal `x`.
    #The mean power of a Gaussian with :math:`\\mu=0` and :math:`\\sigma=1` is 1.
    """
    #return y * np.sqrt( (np.abs(x)**2.0).mean() / (np.abs(y)**2.0).mean() )
    if x is not None:
        x = ms(x)
    else:
        x = 1.0
    return y * np.sqrt( x / ms(y) )

def noise(N, color='white'):
    """Noise generator.
    
    :param N: Amount of samples.
    :param color: Color of noise.
    
    """
    try:
        return _noise_generators[color](N)
    except KeyError:
        raise ValueError("Incorrect color.")


def white(N):
    """
    White noise.
    
    :param N: Amount of samples.
    
    White noise has a constant power density. It's narrowband spectrum is therefore flat.
    The power in white noise will increase by a factor of two for each octave band, 
    and therefore increases with 3 dB per octave.
    """
    return np.random.randn(N)
    
def pink(N):
    """
    Pink noise. 
    
    :param N: Amount of samples.
    
    Pink noise has equal power in bands that are proportionally wide.
    Power density decreases with 3 dB per octave.
    
    """
    # This method uses the filter with the following coefficients.
    #b = np.array([0.049922035, -0.095993537, 0.050612699, -0.004408786])
    #a = np.array([1, -2.494956002, 2.017265875, -0.522189400])
    #return lfilter(B, A, np.random.randn(N))
    # Another way would be using the FFT
    #x = np.random.randn(N)
    #X = rfft(x) / N  
    uneven = N%2
    X = np.random.randn(N//2+1+uneven) + 1j * np.random.randn(N//2+1+uneven)
    S = np.sqrt(np.arange(len(X))+1.) # +1 to avoid divide by zero
    y = (irfft(X/S)).real
    if uneven:
        y = y[:-1]
    return normalize(y)


def blue(N):
    """
    Blue noise. 
    
    :param N: Amount of samples.
    
    Power increases with 6 dB per octave.
    Power density increases with 3 dB per octave. 
    
    """
    uneven = N%2
    X = np.random.randn(N//2+1+uneven) + 1j * np.random.randn(N//2+1+uneven)
    S = np.sqrt(np.arange(len(X)))# Filter
    y = (irfft(X*S)).real
    if uneven:
        y = y[:-1]
    return normalize(y)


def brown(N):
    """
    Brown noise.
    
    :param N: Amount of samples.
    
    Power decreases with -3 dB per octave.
    Power density decreases with 6 dB per octave. 
    """
    uneven = N%2
    X = np.random.randn(N//2+1+uneven) + 1j * np.random.randn(N//2+1+uneven)
    S = (np.arange(len(X))+1)# Filter
    y = (irfft(X/S)).real
    if uneven:
        y = y[:-1]
    return normalize(y)


def violet(N):
    """
    Violet noise. Power increases with 6 dB per octave. 
    
    :param N: Amount of samples.
    
    Power increases with +9 dB per octave.
    Power density increases with +6 dB per octave. 
    
    """
    uneven = N%2
    X = np.random.randn(N//2+1+uneven) + 1j * np.random.randn(N//2+1+uneven)
    S = (np.arange(len(X)))# Filter
    y = (irfft(X*S)).real
    if uneven:
        y = y[:-1]
    return normalize(y)


_noise_generators = {
    'white'  : white,
    'pink'   : pink,
    'blue'   : blue,
    'brown'  : brown,
    'violet' : violet,
    }


def noise_generator(N=44100, color='white'):
    """Noise generator. 
    :param N: Amount of unique samples to generate.
    :param color: Color of noise.
     
    Generate `N` amount of unique samples and cycle over these samples.
    
    """
    #yield from itertools.cycle(noise(N, color)) # Python 3.3
    for sample in itertools.cycle(noise(N, color)):
        yield sample
    

def heaviside(N):
    """Heaviside.
    
    Returns the value 0 for `x < 0`, 1 for `x > 0`, and 1/2 for `x = 0`.
    """
    return 0.5 * (np.sign(N) + 1)