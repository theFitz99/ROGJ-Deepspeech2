# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 10:23:56 2022

@author: filip
"""

import scipy.io.wavfile
import scipy.signal
import os
import numpy as np

path = os.getcwd()
os.chdir(path)

if os.path.isdir("resampled"):
    pass
else:
    os.mkdir("resampled")

new_rate = 16000
print("Resampling u tijeku. Moze potrajati nekoliko minuta...")

for d in sorted(os.listdir("wav")):
    for file in sorted(os.listdir(os.path.join(path, "wav", d))):
        rate, wav = scipy.io.wavfile.read(os.path.join(path, "wav", d, file))
        samples = round(len(wav) * float(new_rate) / rate)
        new_data = scipy.signal.resample(wav, samples)
        scipy.io.wavfile.write(os.path.join(path, "resampled", file), new_rate, new_data.astype(np.dtype('i2')))

print("Uspjesno izvresen resampling!")
