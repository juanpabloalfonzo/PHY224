import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit #Import python libraries

def  Voltage(I, slope, intercept): #Define the curve fit with parameters needed to construct a linear trend
    return slope*I + intercept

def chi2(y_measure,y_predict,errors):
    #Calculate the chi squared value given a measurement with errors and prediction
    return np.sum( (y_measure - y_predict)**2 / errors**2 )

def chi2reduced(y_measure, y_predict, errors, number_of_parameters):
    #Calculate the reduced chi squared value given a measurement with errors and prediction,
    #and knowing the number of parameters in the model.
    return chi2(y_measure, y_predict, errors)/(y_measure.size - number_of_parameters)

def  Voltage0(I, slope): #Define the curve fit with parameters needed to construct a linear trend and y intercept of 0
    return slope*I

#Importing Data
data=np.loadtxt('data.txt')

BV=data[:,0]
BI=data[:,1]
BE=data[:,2]
P6V=data[:,3]
P6I=data[:,4]
P6E=data[:,5]
P10V=data[:,6]
P10I=data[:,7]
P10E=data[:,8]
P15V=data[:,9]
P15I=data[:,10]
P15E=data[:,11]
P20V=data[:,12]
P20I=data[:,13]
P20E=data[:,14]

#Battery Line Of Best Fit
p_optB, p_covB=curve_fit(Voltage, BI , BV , p0=[0,0] ,sigma=BE , absolute_sigma=True) #Call linear best fit function for the 470ohm resistor
plt.figure()
plt.title("Battery Voltage vs Current")
plt.plot(BI, Voltage(BI, p_optB[0], p_optB[1]), label='Line Of Best Fit')
plt.ylabel("Voltage (V)")
plt.xlabel("Current (mA)")
plt.errorbar(BI,BV, yerr=BE, fmt='ro', ecolor='m', label='Measurements')
plt.legend()
plt.savefig('Battery') #Plot all quantites include the line of best fit and the experimental data with error bars

#Power Source 6.5V Line Of Best Fit
p_optP6, p_covP6=curve_fit(Voltage, P6I , P6V , p0=[0,0] ,sigma=P6E , absolute_sigma=True)
plt.figure()
plt.title("DC Power Supply (6.5V) Voltage vs Current")
plt.plot(P6I, Voltage(P6I, p_optP6[0], p_optP6[1]), label='Line Of Best Fit')
plt.ylabel("Voltage (V)")
plt.xlabel("Current (mA)")
plt.errorbar(P6I,P6V, yerr=P6E, fmt='ro', ecolor='m', label='Measurements')
plt.legend()
plt.savefig('DC Power Supply 6,5V') #Plot all quantites include the line of best fit and the experimental data with error bars

#Power Source 10V Line Of Best Fit
p_optP10, p_covP10=curve_fit(Voltage, P10I , P10V , p0=[0,0] ,sigma=P10E , absolute_sigma=True) 
plt.figure()
plt.title("DC Power Supply (10V) Voltage vs Current")
plt.plot(P10I, Voltage(P10I, p_optP10[0], p_optP10[1]), label='Line Of Best Fit')
plt.ylabel("Voltage (V)")
plt.xlabel("Current (mA)")
plt.errorbar(P10I,P10V, yerr=P10E, fmt='ro', ecolor='m', label='Measurements')
plt.legend()
plt.savefig('DC Power Supply 10V') #Plot all quantites include the line of best fit and the experimental data with error bars

#Power Source 15V Line Of Best Fit
p_optP15, p_covP15=curve_fit(Voltage, P15I , P15V , p0=[0,0] ,sigma=P15E , absolute_sigma=True) 
plt.figure()
plt.title("DC Power Supply (15V) Voltage vs Current")
plt.plot(P15I, Voltage(P15I, p_optP15[0], p_optP15[1]), label='Line Of Best Fit')
plt.ylabel("Voltage (V)")
plt.xlabel("Current (mA)")
plt.errorbar(P15I,P15V, yerr=P15E, fmt='ro', ecolor='m', label='Measurements')
plt.legend()
plt.savefig('DC Power Supply 15V') #Plot all quantites include the line of best fit and the experimental data with error bars

#Power Source 20V Line Of Best Fit
p_optP20, p_covP20=curve_fit(Voltage, P20I , P20V , p0=[0,0] ,sigma=P20E , absolute_sigma=True) 
plt.figure()
plt.title("DC Power Supply (20V) Voltage vs Current")
plt.plot(P20I, Voltage(P20I, p_optP20[0], p_optP20[1]), label='Line Of Best Fit')
plt.ylabel("Voltage (V)")
plt.xlabel("Current (mA)")
plt.errorbar(P20I,P20V, yerr=P20E, fmt='ro', ecolor='m', label='Measurements')
plt.legend()
plt.savefig('DC Power Supply 20V') #Plot all quantites include the line of best fit and the experimental data with error bars

#Resistance Values
print("The resistance value for the battery is: ", np.absolute(p_optB[0]), "±", np.sqrt(p_covB[0,0]))
print("The resistance value for the battery is: ", np.absolute((p_optP6[0]+p_optP10[0]+p_optP15[0]+p_optP20[0])/4), "±", np.sqrt(p_covP6[0,0]))

#Chi Squared Values
print('')
print('')
print('The Reduced Chi Squared of the Battery Resistance is:', chi2reduced(BV,Voltage(BI, p_optB[0], p_optB[1]),BE,2))
print('')
print('The Reduced Chi Squared of the Power Supply (6.5V) Resistance is:', chi2reduced(P6V,Voltage(P6I, p_optP6[0], p_optP6[1]),P6E,2))
print('')
print('The Reduced Chi Squared of the Power Supply (10V) Resistance is:', chi2reduced(P10V,Voltage(P10I, p_optP10[0], p_optP10[1]),P10E,2))
print('')
print('The Reduced Chi Squared of the Power Supply (15V) Resistance is:', chi2reduced(P15V,Voltage(P15I, p_optP15[0], p_optP15[1]),P15E,2))
print('')
print('The Reduced Chi Squared of the Power Supply (20V) Resistance is:', chi2reduced(P20V,Voltage(P20I, p_optP20[0], p_optP20[1]),P20E,2))


