# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


###########
# IMPORTS #
###########

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import rc


# establishing file path and two data files that will be used
path = '/Users/jmzator/Desktop/'
iceData = path + 'ice_spectra.txt'
KBOdata = path + 'spectrum_measured.txt'

# check file contents to insure correct files being used
with open(iceData) as l:
    print(l.read())

with open(KBOdata) as m:
    print(m.read())

givenSpectra = np.loadtxt(iceData, skiprows=1)
wavelength, h20_spectrum, co2_spectrum, nh3_spectrum, ch4_spectrum = givenSpectra.T

KBO = np.loadtxt(KBOdata, skiprows=1)
KBO_wavelength, KBO_reflect, KBO_reflecterror = KBO.T


# now for some plotting
plt.plot(wavelength, h20_spectrum, label='H2O Spectrum')
plt.plot(wavelength, co2_spectrum, label='CO2 Spectrum')
plt.plot(wavelength, nh3_spectrum, label='NH3 Spectrum')
plt.plot(wavelength, ch4_spectrum, label='CH4 Spectrum')
plt.plot(KBO_wavelength, KBO_reflect, label='KBO Measured Spectrum')
plt.title('Unknown Kuiper Belt Object Spectra Comparison to Known Species')
plt.xlabel('Wavelenght in Microns')
plt.ylabel('Received Spectra')
plt.legend(loc=0, bbox_to_anchor=(1.0, 0.65))
plt.show()



import scipy as sp
