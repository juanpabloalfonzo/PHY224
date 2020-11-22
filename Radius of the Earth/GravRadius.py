import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def  radius(floor, slope, intercept): #Define the curve fit with parameters needed to construct a linear trend
    return slope*floor + intercept

def chi(y_i,y_x,sigmai): #Where y_i are dependent variables, y_x is the line of best fit y values, and sigmai is the error of the the y_i measurement
    a=((y_i-y_x)/sigmai)**2 
    return((1/12)*(np.sum(a)))  #14 trials and 2 parameters define the 1/v in this case v=12

#Importing Data
Data=np.loadtxt("FloorData.txt")
Floors=Data[:,0]
GravRaw1=Data[:,1]
GravRaw2=Data[:,2]
RawError=Data[:,3]


#Conversions
mGalGrav1=0.10155*GravRaw1 #Converts from Div to mGal
Grav1=mGalGrav1/100000
mGalGrav2=0.10155*GravRaw2
Grav2=mGalGrav2/100000
mGalError=0.10155*RawError
Error=mGalError/100000

#Curve Fitting 
p_optR1, p_covR1=curve_fit(radius, Floors , Grav1 , p0=[0,0] ,sigma=Error , absolute_sigma=True) #Call linear best fit function
p_optR2, p_covR2=curve_fit(radius, Floors , Grav2 , p0=[0,0] ,sigma=Error , absolute_sigma=True) #Call linear best fit function

#Plotting Data
plt.title("Day 1 Measurements")
plt.errorbar(Floors,Grav1, yerr=Error, fmt='m.', label='Experimental Measurements (Day 1)')
plt.plot(Floors,radius(Floors,p_optR1[0],p_optR1[1]),label='Line of Best Fit')
plt.xlabel("Floor")
plt.ylabel("Measurement Of Gravity")
plt.legend(loc='upper right')
plt.savefig('Day 1')

plt.figure()
plt.title("Day 2 Measurements")
plt.errorbar(Floors,Grav2, yerr=Error, fmt='m.', label='Experimental Measurements (Day 2)')
plt.plot(Floors,radius(Floors,p_optR2[0],p_optR2[1]),label='Line of Best Fit')
plt.xlabel("Floor")
plt.ylabel("Measurement Of Gravity")
plt.legend(loc='upper right')
plt.savefig('Day 2')


#Reading values of Radius of the Earth 
R=6371*1000
R1=-2*(3.95)*(9.81/p_optR1[0])
R1U=np.abs(((np.sqrt(p_covR1[0,0])/p_optR1[0])*100)*R1) #unceratanty calculation 
print('The Radius of the Earth from the first days measurement is:',R1, '±', R1U)
R2=-2*(3.95)*(9.81/p_optR2[0])
R2U=np.abs(((np.sqrt(p_covR2[0,0])/p_optR2[0])*100)*R2) #unceratanty calculation 
print('The Radius of the Earth from the first days measurement is:',R2, '±', R2U)


#Chi Squared 
print("The value for how good the Day 1 data has been fitted is: ", chi(Grav1,radius(Floors, p_optR1[0], p_optR1[1]),Error)) #chi squared for day 1
print("The value for how good the Day 2 data has been fitted is: ", chi(Grav2,radius(Floors, p_optR2[0], p_optR2[1]),Error)) #chi squared for day 2

