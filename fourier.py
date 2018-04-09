#compute FFT for a given signal a
import numpy as np

def fourier (a, timestep =1):
    transform = np.fft.fft(a)
    #print transform
    freq = np.fft.fftfreq(len(a), d=timestep)
    #print 'frequencies', freq
    maximum = np.argmax(abs(transform))
    #print 'prominent frequency', freq[maximum]
    return (freq[maximum]), transform, freq 