# DRS_analysis

The script is used to analyze data taken by the DRS Oscilloscope.
Details of the DRS Oscilloscope can be found [here](https://www.psi.ch/drs/DocumentationEN/manualrev50.pdf).

---

## This script serves three main purposes:
- Converts binary data from DRS into a root file with higher level information like pulse time, pulse area, etc.
- Generates waveforms of individual events recorded by DRS.
- Generates histograms of DRS data based on predefined histograms.
---
### In order to run the script successfully the user must answer questions about the experiment being analyzed. Below is a guide on how to answer each question.

1. What is the filename? (no extension)
   - Enter the name of the file exactly as you see it **without** the extension.
2. Do you need to process these events from binary to root? (yes or no)
   - **Answer "yes" if this is the first time** running the script for this file.
   -This step can be skipped if this file has been processed before by answering "no".
3. How many events are in this file?
   - This number was specified by the user in the DRS application during the setup of the experiment.
4. Do you want to make waveforms? (yes or no)
   - Generating waveforms help the user approximate a time window that encompasses most of the waveforms recorded.
   - This will be the window of data used to calculate the higher level info.
5. How many plots (per channel) would you like to make?
   - More plots means a better approximation of the time window. (Suggest ~50)
6. Do you want to run post-processing on these events? (yes or no)
   - **Answer "yes" if its the first time** running the script for this file.
   - This step can be skipped if this file has been processed before by answering "no".
7. What was the trigger threshold (in mV) for the events?
   - This value was specified by the user in the DRS application during the setup of the experiment.
8. Do you want to make histograms for these events? (yes or no)
   - Answering "yes" generates the histograms specified in "makeHistograms.py".
   - User can create customized histograms by adding to "makeHistograms.py" before running script.
9. Would you like to save these histograms as .png files? (yes or no)
   - Pretty self explanatory.
10. Would you like to click through the histograms as they are being generated? (yes or no)
    - Answering "yes" will generate a histogram then waint until the user double-clicks on the plot before generating the next histogram.
    - Answering "no" will generate all the histograms consecutively.
The remaining questions are Channel info that was specified by the user in the DRS application during the setup of the experiment.
11. Does Ch.1 have data? (yes or no)
    - Was there an input connected to Ch.1 during the experiment?
      11.1 Choose a time before the beginning of most waveforms recorded by Ch.1. (in ns)
           - This value can be arrived at by looking through a few waveforms.
      11.2 Choose a time after the end of most waveforms recorded by Ch.1. (in ns)
      
Likewise for the remaining channels.

---

### Location of generated root files, waveforms and histograms.

Root files are saved in the 'unprocessed data' directory inside the 'DRS_data' directory.
Waveforms have their own directory in the 'processed data' directory inside the 'DRS_data' directory.
Histograms also have their own directory in the 'processed data' directory inside the 'DRS_data' directory.
