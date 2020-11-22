import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.optimize import curve_fit

def model_function(x, a, b): #Defining function that will take in voltage and use 1/R as slope
    return a*x+b      #and outputs voltage 

CR=np.loadtxt('DataCurrentResistor.txt') #Importing Current data for resistor
VR=np.loadtxt('DataVoltageResistor.txt') #Importing voltage data for reistor
ER=np.loadtxt('ErrorR.txt') #Importing uncertanty data for reistor
CP=np.loadtxt('DataCurrentP.txt') #Importing current data for potentiometer
VP=np.loadtxt('DataVoltageP.txt') #Importing voltage data for potentiometer
EP=np.loadtxt('ErrorP.txt') #Importing uncertanty data for potentiometer

p_optR , p_covR = curve_fit(model_function, VR , CR , p0=[(1/470),0] ,sigma=ER , absolute_sigma=True) #Create a line of best fit for Resistor Data

p_optP , p_covP = curve_fit(model_function, VP , CP , p0=[(1/1290),0] ,sigma=EP , absolute_sigma=True) #Create a line of best fit for Potentiometer Data


plt.subplot(221) #Creating plot of I versus V for resistor
plt.title('Resistor')
plt.plot(VR,CR,'ro')
plt.errorbar(VR,CR,yerr=ER)
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)') 

LR=[] #For loop to create line of best fit using slope and b value given by curve fit function
for i in range(0,len(VR)):
   LR.append(p_optR[0]*VR[i]+p_optR[1])

plt.plot(VR,LR) #Overplotting the line of best fit  
plt.show()


plt.subplot(222)
plt.title('Potentiometer')
plt.plot(VP,CP,'bo')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')

LP=[] #For loop to create line of best fit using slope and b value given by curve fit function
for i in range(0,len(VP)):
    LP.append(model_function(VP[i],p_optP[0],p_optP[1]))
    
plt.plot(VP,LP) #Overplotting the line of best fit
plt.show()

print(EP)
print(VP)



