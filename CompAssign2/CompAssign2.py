#Juan Pablo Alfonzo
#1003915132

#Comp Assigment 2: Curve Fitting 

#Importing needed libraries 

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.optimize import curve_fit

#Question 1: Reading and Plotting Data 

#Importing data for rocket data
r=np.loadtxt('rocket.txt')

#Plotting rocket data
plt.errorbar(r[:,0],r[:,1], yerr=r[:,2], fmt='k.')
plt.xlabel('Time(h)')
plt.ylabel('Position(m)')
plt.title('Rocket Position vs Time')
plt.savefig('Rocket Plot.png')

#Question 2: Estimating the Speed
print('Question 2')
rva=np.mean(r[:,1]/r[:,0]) #Taking the mean of all postion_i/t_i
rve=np.std(r[:,1]/r[:,0]) #Taking the standard deviation of all postion_i and t_i

#Note that time for t=0 edit was made to text file to avoid 0/0 division. Both zeores entries
#changed to 0.0001 to allow the code to run without error without changing any statistics 

print('The average speed of the rocket is:',rva, 'm/h','±',rve, 'm/h')
print('')
print('')
#Question 3: Linear Regression 
print('Question 3')

#Define some variables to simpfy things 
tr=r[:,0] #Time column of rocket data array
dr=r[:,1] #Distance column  of rocket data array
er=r[:,2] #Unvertanties column of rocket data array


#Calculating u hat with equation given in assigment 

u=(np.sum((tr-np.mean(tr))*(dr-np.mean(dr)))/np.sum((tr-np.mean(tr))**2))

print('u hat is:', u, 'm/h')

#Calculating s_o hat using equation given in assigment

s_0=np.mean(dr)-(u*np.mean(tr))

print('s_0 hat is given by:', s_0, 'm')

print('')
print('')

#Question 4: Plotting the Prediction

#Function modeling s=s_0+ut
def location(t,d_0,s): #Where t is the time array, d_0 is the intial distance of the rocket, and s is the speed of the rocket
    return(s*t+d_0)

plt.figure()
plt.errorbar(r[:,0],r[:,1], yerr=r[:,2], fmt='k.', label='Data Points with Uncertanties')
plt.plot(tr,location(tr,s_0,u), label='Line of Best Fit')
plt.xlabel('Time(h)')
plt.ylabel('Position(m)')
plt.title('Rocket Position vs Time')
plt.legend(loc='upper left')
plt.savefig('Rocket Line of Best Fit.png')

#Question 5: Characterizing the fit
print('Question 5')

def chi2(y_measure,y_predict,errors):
    #Calculate the chi squared value given a measurement with errors and prediction
    return np.sum( (y_measure - y_predict)**2 / errors**2 )

def chi2reduced(y_measure, y_predict, errors, number_of_parameters):
    #Calculate the reduced chi squared value given a measurement with errors and prediction,
    #and knowing the number of parameters in the model.
    return chi2(y_measure, y_predict, errors)/(y_measure.size - number_of_parameters)

print('The chi squared for the rocket data linear fitting is:', chi2reduced(dr,location(tr,s_0,u),er,2))
print('')
print('')

#Question 6: Curve Fitting
print('Question 6')

#Use curve fit function to create a line of best fit
rocketSY, rocketU = curve_fit(location, tr, dr,sigma=er, absolute_sigma=True, p0=(u,s_0))

print('The slope of the line found using the curvefit function is:', rocketSY[1], 'm/h', '±', np.sqrt(rocketU[1,1]), 'm/h')
print('')
print('The y-intercept of the line found using the curvefit function is:', rocketSY[0], 'm', '±', np.sqrt(rocketU[0,0]), 'm')
print('')
print('The chi squared for the curvefit model is:', chi2reduced(dr,location(tr,rocketSY[0],rocketSY[1]),er,2))

plt.figure()
plt.errorbar(r[:,0],r[:,1], yerr=r[:,2], fmt='k.', label='Data Points with Uncertanties')
plt.plot(tr,location(tr,s_0,u), label='Line of Best Fit')
plt.plot(tr,location(tr,rocketSY[0],rocketSY[1]), label='Line of Best Fit (curvefit)',color='r')
plt.xlabel('Time(h)')
plt.ylabel('Position(m)')
plt.title('Rocket Position vs Time')
plt.legend(loc='upper left')
plt.savefig('Rocket Line of Best Fit (curvefit).png')
print('')
print('')

#Question 7: Feather Drop Expirement 
print('Question 7')

#Importing feather data
f=np.loadtxt('feather.txt')

ft=f[:,0]
fd=f[:,1]
fe=f[:,2]

#Function that gives position of feather above moon surface given time, initial position, initial velocity, and constant acceleration
def position(t,s_0, u, a):
    return(s_0+u*t+(1/2)*a*t**2)

fu=(np.sum((ft-np.mean(ft)*(fd-np.mean(fd)))/np.sum((ft-np.mean(ft))**2))) #prediction of intial velocity using similar equation as before
fs_0=np.mean(fd)-(fu*np.mean(ft)) #prediction of intial distance using similar equation as before

#Use curve fit function to create a line of best fit
featherSYG, featherU = curve_fit(position, ft, fd,sigma=fe, absolute_sigma=True, p0=(fu,fs_0,(1/7)*9.8))

print('The parameter s_0  found by curve fit is:', featherSYG[0], 'm', '±', np.sqrt(featherU[0,0]), 'm')
print('')
print('The parameter u found by curve fit is:',  featherSYG[1], 'm/s', '±', np.sqrt(featherU[1,1]), 'm/s')
print('')
print('The parameter a found by curve fit is:', featherSYG[2], 'm/s^2', '±', np.sqrt(featherU[2,2]), 'm/s^2')
   
#Plotting feather data
plt.figure()
plt.errorbar(f[:,0],f[:,1], yerr=f[:,2], fmt='r.', label='Feather Position')
plt.plot(ft,position(ft,featherSYG[0],featherSYG[1],featherSYG[2]), label='Line of Best Fit')
plt.xlabel('Time(s)')
plt.ylabel('Position(m)')
plt.title('Feather Position vs Time')
plt.legend()
#plt.show()
plt.savefig('featherplot.png') #save figure in the same directory where the .py file is sotred
    


