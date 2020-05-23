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
    """
    Parameters
    ----------
    already_compressed : TYPE
        DESCRIPTION.
    data_path : TYPE
        DESCRIPTION.
    mp3_names : TYPE
        DESCRIPTION.
    remove_mp3 : TYPE, optional
        DESCRIPTION. The default is False.

    Returns
    -------
    None.

    """
    
    command0 = 'cmd /k TO& cd C:/Users/juan/Desktop/rtve_podcasts '
    command1 = '' 
    for mp3_name in mp3_names: 
        if mp3_name.replace('mp3','pcf') in already_compressed:
            continue
        full_name = os.path.join(data_path, mp3_name)
        command1 += ' && precomp ' + full_name
    command2 = ' && exit TO&'
    command = command0 + command1 + command2
    error = os.system(command.replace('TO&', '"'))
    
    if remove_mp3 and error == 0:
        for mp3_name in mp3_names: os.remove(os.path.join(data_path, mp3_name))

        
def decompress_mp3(already_compressed, data_path, mp3_names, remove_pcf = False):
    """
    Parameters
    ----------
    already_compressed : TYPE
        DESCRIPTION.
    data_path : TYPE
        DESCRIPTION.
    mp3_names : TYPE
        DESCRIPTION.
    remove_pcf : TYPE, optional
        DESCRIPTION. The default is False.

    Returns
    -------
    None.

    """
    
    command0 = 'cmd /k TO& cd C:/Users/juan/Desktop/rtve_podcasts '
    command1 = '' 
    for comp in already_compressed: 
        if comp.replace('pcf','mp3') in mp3_names:
            continue
        full_name = os.path.join(data_path, comp)
        command1 += ' && precomp -r -o' + full_name.replace('pcf','mp3') +' '+ full_name
    command2 = ' && exit TO&'
    command = command0 + command1 + command2
    error = os.system(command.replace('TO&', '"'))
    
    if remove_pcf and error == 0:
        for comp in already_compressed: os.remove(os.path.join(data_path, comp))
    
    

# Compress and remove 
data_path = r'C:\Users\juan\Desktop\rtve_podcasts\data\discopolis'
already_compressed = [f for f in os.listdir(data_path) if f[-3:] == 'pcf']
mp3_names = [f for f in os.listdir(data_path) if f[-3:] == 'mp3']
compress_mp3(already_compressed, data_path, mp3_names[:30], remove_mp3 = True)
#decompress_mp3(already_compressed, data_path, mp3_names, remove_pcf = True)




