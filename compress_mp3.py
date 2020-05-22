# -*- coding: utf-8 -*-
"""
Created on Fri May 22 19:36:48 2020

@author: lokopobit
"""

# Information
# http://schnaader.info/precomp.php
# https://github.com/schnaader/precomp-cpp

# Load external libreries
import os

def compress_mp3(already_compressed, data_path, mp3_names, remove_mp3 = False):
    command0 = 'cmd /k TO& cd Desktop/rtve_podcasts '
    command1 = '' 
    for mp3_name in mp3_names: 
        if mp3_name.replace('mp3','pcf') in already_compressed:
            continue
        full_name = os.path.join(data_path, mp3_name)
        command1 += ' && precomp ' + full_name
    command2 = ' && exit TO&'
    command = command0 + command1 + command2
    os.system(command.replace('TO&', '"'))
    
    if remove_mp3:
        for mp3_name in mp3_names: os.delete(os.path.join(data_path, mp3_name))
    
    
data_path = ''
already_compressed = [f for f in os.listdir(data_path) if f[-3:] == 'pcf']
mp3_names = ['2012dic03.mp3', '2012dic04.mp3']