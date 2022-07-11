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

cnt_txt = 0
cnt_wav = 0
cnt_log = 0

for t in sorted(os.listdir("txt")):
    for file in sorted(os.listdir(os.path.join(path, "txt", t))):
        txt.append(os.path.splitext(file)[0])
    
for w in sorted(os.listdir("wav")):
    for file in sorted(os.listdir(os.path.join(path, "wav", w))):
        if file.endswith(".wav"):   
            wav.append(os.path.splitext(file)[0])
        else:
            os.remove(os.path.join(path, "wav", w, file))
            cnt_log += 1
            
for w in wav:
    if w not in txt:
        for r, d, f in os.walk("wav"):
            for file in f:
                if file == w + ".wav":
                    os.remove(os.path.join(r, file))
                    cnt_wav += 1
        print(w + ".wav nema pripadacuje .txt datoteke pa je izbrisana.")

for t in txt:
    if t not in wav:
        for r, d, f in os.walk("txt"):
            for file in f:
                if file == t + ".txt":
                    os.remove(os.path.join(r, file))
                    cnt_txt += 1
        print(t + ".txt nema pripadajuce .wav datoteke pa je izbrisana.")     
        
print(f"Podaci su spremni!\nUkupno je izbrisano {cnt_wav} \033[3m.wav\x1B[0m datoteka, {cnt_txt} \033[3m.txt\x1B[0m datoteka i {cnt_log} \033[3mlog\x1B[0m datoteka.")