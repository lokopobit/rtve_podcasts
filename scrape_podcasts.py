# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 20:10:26 2020

@author: lokopobit
"""

# Load external libreries
import os
from urllib import urlopen
from shutil import copyfileobj

# Define the url allocating the mp3 file. It must end with .mp3
url_sound = 'https://mediavod-lvlt.rtve.es/resources/TE_S180GRA/mp3/5/9/1582630851495.mp3'

def download_sound_file(url_sound, path_sound, filename):
    """
    Downloads a sound file allocated in the web. This file is accesible by a 
    url that ends with .mp3. The file is stored in path_sound with filename as
    file name.
    
    Paramaters:
        url_sound (str): url where the sound file is stored (must end with .mp3) 
        path_sound (str): the absolute path where the mp3 file will be saved.
                          If it does not exist it will be created.
        filename (str): the name of the mp3 file.
    """
    
    if not os.path.exists(path_sound):
        os.mkdir(path_sound)
    
    out_file = open(os.path.join(path_sound,filename)+'.mp3', 'wb') # Open de sound file that will store the mp3
    in_stream = urlopen(url_sound) # Download the stream data
    copyfileobj(in_stream, out_file) # Copy the stream data into the sound file 
    out_file.close() #Close the sound file 
