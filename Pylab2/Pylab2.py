#importing needed libraries according to lab handout
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.optimize import curve_fit

#Defining model functions for curve fit as mentioned in lab handout
def model_function1(x, a, b): 
    return a*x+b      

def model_function2(x,a,b):
    return b*(np.e)**(a*x)


#Importing Background and Decay data from text files
D=np.loadtxt('Decay18.txt')
B=np.loadtxt('Background18.txt')



#Linear Fit
C=D[:,1]-(np.mean(B[:,1])) #Corrected data where each entry in decay has the mean background subtracted

CSD1=np.sqrt(C)/20  #Find standard deviation of the corrected data set 


CSD=np.absolute(CSD1/C)




CR=C/20 #Dividing count rates by delta t (count rate/second)

LogCR=np.log(CR) #Take the log of all count rate/second data points (y_i)

p_optL , p_covL = curve_fit(model_function1, D[:,0] , LogCR , p0=[0,0] ,sigma=CSD , absolute_sigma=True) #Create a line of best fit for log of output


#Plotting the line of best over the experimental data
plt.subplot(221)
plt.title('Linear Best Fit')
plt.xlabel('Trial Number')
plt.ylabel('log(Count Rate/Second)')
plt.plot(D[:,0], LogCR, 'r.', label='Experimental Data')    
plt.plot(D[:,0], model_function1(D[:,0],p_optL[0],p_optL[1]), label= 'Line of Best Fit')
plt.legend(loc='upper right')
plt.errorbar(D[:,0],LogCR, yerr=CSD, fmt='none', ecolor='k')
plt.show()


#NonLinear Best Fit





