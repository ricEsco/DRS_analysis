import struct
import datetime as dt
import json
import sys
import os
import ROOT as r
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

### allows us to call each script (which has been reformatted as a function) with corresponding inputs ###
import processMultiChanBinary
import makeWaveforms_new
import postprocessMultiChan
import makeHistograms

doProcess = False
doPostProcess = False
doWaveforms = False
doHistograms = False

tstart_1 = 0
tend_1   = 500
tstart_2 = 0
tend_2   = 500
tstart_3 = 0
tend_3   = 500
tstart_4 = 0
tend_4   = 500
N_PLOTS = 0
N_EVTS = 0
trig = 0
chn1 = False
chn2 = False
chn3 = False
chn4 = False
liveHistos = False
saveHistos = False

### processMultiChan variables and channel info for other scripts
name = raw_input("What is the filename? (no extension)   ")
process = raw_input("do you need to process these events from binary to root? (yes or no)   ").lower().strip()
if process == "yes":
    doProcess = True
    N_EVTS = int(raw_input("How many events are in this file?   "))

### makeWaveforms_new variable (channel info defined above)
waveforms = raw_input("Do you want to make waveforms? (yes or no)   ").lower().strip()
if waveforms == "yes":
    doWaveforms = True
    N_PLOTS = int(raw_input("How many plots (per channel) would you like to make?   "))

### postprocessMultiChan variable (channel info defined above)
postprocess = raw_input("Do you want to run post-processing on these events? (yes or no)   ").lower().strip()
if postprocess == "yes":
    doPostProcess = True
    trig = int(raw_input("What was the trigger threshold (mV) for the events?   "))

### makeHistograms variable
histograms = raw_input("Do you want to make histograms for these events? (yes or no)   ").lower().strip()
if histograms == "yes":
    doHistograms = True
    save = raw_input("Would you like to save this histograms as .png files? (yes or no)   ").lower().strip()
    if save == "yes":
        saveHistos = True
    live = raw_input("Would you like to click through the histograms as they are being generated? (yes or no)   ").lower().strip()
    if live == "yes":
        liveHistos = True

if doPostProcess or doWaveforms:
    CH1_info = raw_input("Does Ch1 have data? (yes or no)   ").lower().strip()
    if CH1_info == "yes":
        chn1 = True
        tstart_1 = int(raw_input("Choose a time before the beginning of most Ch1 waveforms. (ns)   "))
        tend_1 = int(raw_input("Choose a time after the end of most Ch1 waveforms. (ns)   "))
    
    CH2_info = raw_input("Does Ch2 have data? (yes or no)   ").lower().strip()
    if CH2_info == "yes":
        chn2 = True
        tstart_2 = int(raw_input("Choose a time before the beginning of most Ch2 waveforms. (ns)   "))
        tend_2 = int(raw_input("Choose a time after the end of most Ch2 waveforms. (ns)   "))

    CH3_info = raw_input("Does Ch3 have data? (yes or no)   ").lower().strip()
    if CH3_info == "yes":
        chn3 = True
        tstart_3 = int(raw_input("Choose a time before the beginning of most Ch3 waveforms. (ns)   "))
        tend_3 = int(raw_input("Choose a time after the end of most Ch3 waveforms. (ns)   "))

    CH4_info = raw_input("Does Ch4 have data? (yes or no)   ").lower().strip()
    if CH4_info == "yes":
        chn4 = True
        tstart_4 = int(raw_input("Choose a time before the beginning of most Ch4 waveforms. (ns)   "))
        tend_4 = int(raw_input("Choose a time after the end of most Ch4 waveforms. (ns)   "))

if doProcess:
    processMultiChanBinary.processMultiChanBinary(name, N_EVTS)
if doWaveforms:
    makeWaveforms_new.makeWaveforms(name, chn1, chn2, chn3, chn4, tstart_1, tstart_2, tstart_3, tstart_4, tend_1, tend_2, tend_3, tend_4, N_PLOTS)
if doPostProcess:
    postprocessMultiChan.postprocessMultiChan(name, tstart_1, tstart_2, tstart_3, tstart_4, tend_1, tend_2, tend_3, tend_4, chn1, chn2, chn3, chn4, trig)
if doHistograms:
    makeHistograms.makeHistograms(name,liveHistos,saveHistos)
