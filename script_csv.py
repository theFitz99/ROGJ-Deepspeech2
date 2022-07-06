# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 13:53:57 2022

@author: filip
"""

import os
import csv

path = os.getcwd()
os.chdir(path)

filenames = []
transcriptions = []
       
for d in sorted(os.listdir("txt")):
    for file in sorted(os.listdir(os.path.join(path, "txt", d))):
        filenames.append(os.path.splitext(file)[0])
        with open(os.path.join(path, "txt", d, file), "r") as readFile:
            transcriptions.append(" ".join(readFile.readline().strip().split()))

with open("dataset.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerow(["filename", "transcription"])
    writer.writerows(zip(filenames, transcriptions))
    
print(".csv datoteka je spremna!")
