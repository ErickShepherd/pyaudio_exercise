#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''

A simple Python music exercise.

Metadata:

    File:           dj.py
    File version:   1.0.0
    Python version: 3.7.3
    Date created:   2021-07-12
    Last updated:   2021-07-12


Authors:

    Erick Edward Shepherd
     - E-mail:  Contact@ErickShepherd.com
     - GitHub:  https://www.github.com/ErickShepherd
     - Website: https://www.ErickShepherd.com

    Timothy Michael Shepherd


Description:
    
    A simple Python music exercise.


Copyright:
    
    Copyright (c) 2021 of Erick Shepherd and Timothy Shepherd, all rights
    reserved.

'''

# %% Third party imports.
import numpy as np
import pyaudio

# %% Dunder definitions.
# - Versioning scheme: SemVer 2.0.0 (https://semver.org/spec/v2.0.0.html)
__author__  = "Erick Shepherd and Timothy Shepherd"
__version__ = "1.0.0"

# %% Constant definitions.
AUDIO_BINDINGS   = pyaudio.PyAudio()
DEFAULT_VOLUME   = 0.5    # A float in the range [0.0, 1.0]
DEFAULT_DURATION = 1.0    # A floating point number of seconds.
SAMPLE_RATE      = 44100  # The integer sampling rate in Hertz.
CHANNELS         = 1      # An integer number of stream channels.
CHUNK_SIZE       = 1024   # An integer chunk size for the stream.
STREAM_FORMAT    = pyaudio.paFloat32
STREAM           = AUDIO_BINDINGS.open(
    format            = STREAM_FORMAT,
    channels          = CHANNELS,
    rate              = SAMPLE_RATE,
    frames_per_buffer = CHUNK_SIZE,
    output            = True
)


# %% Function definition: end_audio_session
def end_audio_session() -> None:
    
    '''
    
    Closes the pyaudio stream and terminates its audio bindings.
    
    :return: None
    :rtype: None
    
    '''
    
    # Terminates the PyAudio bindings and stream instances.
    STREAM.stop_stream()
    STREAM.close()
    AUDIO_BINDINGS.terminate()


# %% Function definition: play_sound
def play_sound(frequency : float,
               duration  : float = DEFAULT_DURATION,
               volume    : float = DEFAULT_VOLUME) -> None:
    
    '''
    
    Plays a sine wave.
    
    :param frequency: The frequency of the sound.
    :type frequency: float
    
    :param duration: The duration of the sound in seconds.
    :type duration: float
    
    :param volume: The volume, between 0.0 and 1.0, of the sound.
    :type volume: float
    
    :return: None
    :rtype: None
    
    '''
    
    # Aliasing for brevity.
    f  = frequency
    fs = SAMPLE_RATE
    t  = duration
    V  = volume
    
    # Creates a frequency array adjusted for the sample rate.
    f_array = np.arange(fs * t) * f / fs
    
    # Converts frequency to angular frequency.
    w_array = 2 * np.pi * f_array
    
    # Creates the frequency samples at the desired volume.
    samples = V * np.sin(w_array).astype(np.float32)
    
    # Outputs the sound.
    STREAM.write(samples)
    

# %% Main entry point.
if __name__ == "__main__":
    
    ##############################
    # YOUR CODE GOES BELOW HERE. #
    ##############################
    
    E4 = 329.63
    F4 = 349.23
    A4 = 440.00
    C5 = 523.25
    
    play_sound(A4)
    play_sound(C5)
    play_sound(E4)
    play_sound(F4)
    
    ##############################
    # YOUR CODE GOES ABOVE HERE. #
    ##############################
    
    end_audio_session()
