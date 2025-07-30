import librosa 
import librosa.display
import sounddevice as sd
import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
def play_audio():
    audio_path="dataset/open/open1.wav"
    data,sr= sf.read(audio_path)
    sd.play(data,sr)
    sd.wait()
    # playsound(audio_path)
