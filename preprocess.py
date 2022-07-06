# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 22:11:06 2022

@author: filip
"""

import os

path = os.getcwd()
os.chdir(path)
txt = []
wav = []

for t in sorted(os.listdir("txt")):
    for file in sorted(os.listdir(os.path.join(path, "txt", t))):
        txt.append(os.path.splitext(file)[0])
    
for w in sorted(os.listdir("wav")):
    for file in sorted(os.listdir(os.path.join(path, "wav", w))):
        if file.endswith(".wav"):   
            wav.append(os.path.splitext(file)[0])
        else:
            os.remove(os.path.join(path, "wav", w, file))
            
for w in wav:
    if w not in txt:
        for r, d, f in os.walk(os.path.join(path, "wav")):
            for file in f:
                if file == w + ".wav":
                    os.remove(os.path.join(r, file))
        print(w + ".wav nema pripadacuje .txt datoteke pa je izbrisana.")

for t in txt:
    if t not in wav:
        for r, d, f in os.walk(os.path.join(path, "txt")):
            for file in f:
                if file == t + ".txt":
                    os.remove(os.path.join(r, file))
        print(t + ".txt nema pripadajuce .wav datoteke pa je izbrisana.")     
        
print("Podaci su spremni!")