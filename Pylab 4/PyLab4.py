
#Importing needed modules
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.optimize import curve_fit

#Importing Data
data=np.loadtxt('PositionTime.txt')

T=data[:,0] #Time values imported 
P=data[:,1] #Position values imported
E=data[:,2] #Error data values imported

plt.figure()
plt.plot(T,P)
plt.title('Raw Data')
plt.xlabel('Time (s)')
plt.ylabel('Position (cm)')
plt.show()
plt.savefig('Raw Data')


#Simulation 
deltat=0.01 #Setting time step
omega_0=7.66 #Omega found using inverse of period
v_0=0 #Initial velocity at start of motion 
y_0=(np.max(P)-np.min(P))/2 #Amplitude of motion
t_0=0 #Intial time at start of motion 

Time=np.zeros([1,1000])  #Empty array to put in time values 

for i in range(0, 1000): #For loop to calculate time intervals
    Time[0,i]=t_0+deltat
    t_0=t_0+deltat




    
#Forward Euler Method
FYTheoretical=np.zeros([1,1000]) #Empty array to store y values
FVTheoretical=np.zeros([1,1000]) #Empty array to store v values
FYTheoretical[0,0]=y_0
FVTheoretical[0,0]=v_0
for i in range (0, 999):
    FYTheoretical[0,i+1]=FYTheoretical[0,i]+deltat*FVTheoretical[0,i]
    FVTheoretical[0,i+1]=FVTheoretical[0,i]-deltat*(omega_0**2)*FYTheoretical[0,i]
    
#Plotting Position vs Time
plt.figure()    
plt.plot(Time[0,:],FYTheoretical[0,:])
plt.title('Forward Euler Theoretical Position vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Position (cm)')
plt.show()
plt.savefig('Forward Euler Theoretical Position vs Time')

#Plotting Velocity vs Time
plt.figure()    
plt.plot(Time[0,:],FVTheoretical[0,:])
plt.title('Forward Euler Theoretical Speed vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Speed (cm/s)')
plt.show()
plt.savefig('Forward Euler Theoretical Speed vs Time')

#Plotting Position vs Velocity 
plt.figure()    
plt.plot(FYTheoretical[0,:],FVTheoretical[0,:])
plt.title('Forward Euler Theoretical Position vs Velocity')
plt.xlabel('Positions (cm)')
plt.ylabel('Speed (cm/s)')
plt.show()
plt.savefig('Forward Euler Theoretical Position vs Velocity')

#Adding Energy to each step in the y and v for loop
m=0.2004 #Adding the mass of the bob
k=m*(omega_0**2) #Adding spring constant
FEYTheoretical=np.zeros([1,1000]) #Empty array to store y values
FEVTheoretical=np.zeros([1,1000]) #Empty array to store v values
FEYTheoretical[0,0]=y_0
FEVTheoretical[0,0]=v_0
FETheoretical=np.zeros([1,1000]) #Empty array to store energy values
for i in range (0, 999):
   FEYTheoretical[0,i+1]=FEYTheoretical[0,i]+deltat*FEVTheoretical[0,i]
   FEVTheoretical[0,i+1]=FEVTheoretical[0,i]-deltat*(omega_0**2)*FEYTheoretical[0,i]
   E=(1/2)*((m*(FEVTheoretical[0,i]/100)**2)+(k*(FEYTheoretical[0,i]/100)**2)) 
   FETheoretical[0,i]=E #Storing Energy value
    
FETheoretical[0,999]=2.07 
#Plotting Energy vs Time 
plt.figure()    
plt.plot(Time[0,:],FETheoretical[0,:])
plt.title('Forward Euler Theoretical Energy vs Time')
plt.xlabel('Time(s)')
plt.ylabel('Energy (J)')
plt.show()
plt.savefig('Forward Euler Theoretical Energy vs Time')





#Symplectic Euler Method     
YTheoretical=np.zeros([1,1000]) #Empty array to store y values
VTheoretical=np.zeros([1,1000]) #Empty array to store v values
YTheoretical[0,0]=y_0
YTheoretical[0,1]=FYTheoretical[0,1]
VTheoretical[0,0]=v_0
VTheoretical[0,1]=FVTheoretical[0,1]
for i in range (0, 999):
    YTheoretical[0,i+1]=YTheoretical[0,i]+deltat*VTheoretical[0,i]
    VTheoretical[0,i+1]=VTheoretical[0,i]-deltat*(omega_0**2)*YTheoretical[0,i+1]
    
#Plotting Position vs Time
plt.figure()    
plt.plot(Time[0,:],YTheoretical[0,:])
plt.title('Symplectic Method Theoretical Position vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Position (cm)')
plt.show()
plt.savefig('Symplectic Method Theoretical Position vs Time')

#Plotting Velocity vs Time
plt.figure()    
plt.plot(Time[0,:],VTheoretical[0,:])
plt.title('Symplectic Method Theoretical Speed vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Speed (cm/s)')
plt.show()
plt.savefig('Symplectic Method Theoretical Speed vs Time')

#Plotting Position vs Velocity 
plt.figure()    
plt.plot(YTheoretical[0,:],VTheoretical[0,:])
plt.title('Symplectic Method Theoretical Position vs Velocity')
plt.xlabel('Positions (cm)')
plt.ylabel('Speed (cm/s)')
plt.show()
plt.savefig('Symplectic Method Theoretical Position vs Velocity')

#Adding Energy to each step in the y and v for loop
m=0.2004 #Adding the mass of the bob
k=m*(omega_0**2) #Adding spring constant
EYTheoretical=np.zeros([1,1000]) #Empty array to store y values
EVTheoretical=np.zeros([1,1000]) #Empty array to store v values
EYTheoretical[0,0]=y_0
EVTheoretical[0,0]=v_0
ETheoretical=np.zeros([1,1000]) #Empty array to store energy values
for i in range (0, 999):
   EYTheoretical[0,i+1]=EYTheoretical[0,i]+deltat*EVTheoretical[0,i]
   EVTheoretical[0,i+1]=EVTheoretical[0,i]-deltat*(omega_0**2)*EYTheoretical[0,i+1]
   E=(1/2)*((m*(EVTheoretical[0,i]/100)**2)+(k*(EYTheoretical[0,i]/100)**2)) 
   ETheoretical[0,i]=E #Storing Energy value
    
ETheoretical[0,999]=0.00620   
#Plotting Energy vs Time 
plt.figure()    
plt.plot(Time[0,:],ETheoretical[0,:])
plt.title('Symplectic Method Theoretical Energy vs Time')
plt.xlabel('Time(s)')
plt.ylabel('Energy (J)')
plt.show()
plt.savefig('Symplectic Method Theoretical Energy vs Time')













#PART 2 of LAB

#Importing Damped Data
datad=np.loadtxt('Damping PositionTime.txt')
TD=datad[:,0] #Time values imported 
PD=datad[:,1] #Position values imported
ED=datad[:,2] #Error data values imported


#Plotting Raw Data
plt.figure()
plt.plot(TD,PD)
plt.title('Raw Data (Damped)')
plt.xlabel('Time (s)')
plt.ylabel('Position (cm)')
plt.show()
plt.savefig('Raw Data (Damped)')



#Simulation 
deltat=0.01 #Setting time step
omega_0=8.72 #Omega found using inverse of period
gamma=0.01653 #Gamma found 
v_0=0 #Initial velocity at start of motion 
y_0=(np.max(PD)-np.min(PD))/2 #Amplitude of motion
t_0=0 #Intial time at start of motion

DTime=np.zeros([1,12000])  #Empty array to put in time values 

for i in range(0, 12000): #For loop to calculate time intervals
    DTime[0,i]=t_0+deltat
    t_0=t_0+deltat


#Sympletic Euler Method
DFYTheoretical=np.zeros([1,12000]) #Empty array to store y values
DFVTheoretical=np.zeros([1,12000]) #Empty array to store v values
DFYTheoretical[0,0]=y_0
DFVTheoretical[0,0]=v_0
for i in range (0, 11999):
    DFYTheoretical[0,i+1]=DFYTheoretical[0,i]+deltat*DFVTheoretical[0,i]
    DFVTheoretical[0,i+1]=DFVTheoretical[0,i]-deltat*(omega_0**2)*DFYTheoretical[0,i+1]-deltat*gamma*DFVTheoretical[0,i]

#Plotting Position vs Time
plt.figure()    
plt.plot(DTime[0,:],DFYTheoretical[0,:])
plt.title('Symplectic Method Theoretical Position vs Time (Damped)')
plt.xlabel('Time (s)')
plt.ylabel('Position (cm)')
plt.show()
plt.savefig('Symplectic Method Theoretical Position vs Time (Damped)')    

#Energy Calculation
#Adding Energy to each step in the y and v for loop
m=0.2178 #Adding the mass of the bob
k=m*(omega_0**2) #Adding spring constant
DEYTheoretical=np.zeros([1,12000]) #Empty array to store y values
DEVTheoretical=np.zeros([1,12000]) #Empty array to store v values
DEYTheoretical[0,0]=y_0
DEVTheoretical[0,0]=v_0
DETheoretical=np.zeros([1,12000]) #Empty array to store energy values
for i in range (0, 11999):
   DEYTheoretical[0,i+1]=DEYTheoretical[0,i]+deltat*DEVTheoretical[0,i]
   DEVTheoretical[0,i+1]=DEVTheoretical[0,i]-deltat*(omega_0**2)*DEYTheoretical[0,i+1]-deltat*gamma*DFVTheoretical[0,i]
   E=(1/2)*((m*(DEVTheoretical[0,i]/100)**2)+(k*(DEYTheoretical[0,i]/100)**2)) 
   DETheoretical[0,i]=E #Storing Energy value

DETheoretical[0,11999]=0.00057
#Plotting Energy vs Time 
plt.figure()    
plt.plot(DTime[0,:],DETheoretical[0,:])
plt.title('Symplectic Method Theoretical Energy vs Time (Damped)')
plt.xlabel('Time(s)')
plt.ylabel('Energy (J)')
plt.show()
plt.savefig('Symplectic Method Theoretical Energy vs Time (Damped)')

#Plotting Energy vs Time (Over Plot of Both Methods)
plt.figure()    
plt.plot(Time[0,:],ETheoretical[0,:],label='Symplectic Method')
plt.plot(Time[0,:],FETheoretical[0,:], label='Forward Euler Method')
plt.title('Symplectic Method vs Forward Euler Method (Energy vs Time)')
plt.xlabel('Time(s)')
plt.ylabel('Energy (J)')
plt.legend()
plt.show()
plt.savefig('Symplectic vs Forward Euler Method Theoretical Energy vs Time')


#Plotting Position vs Velocity (Over Plot of Both Methods)
plt.figure()    
plt.plot(YTheoretical[0,:],VTheoretical[0,:], label='Sympletic Method')
plt.plot(FYTheoretical[0,:],FVTheoretical[0,:], label='Forward Euler Method')
plt.title('Symplectic vs Forward Euler Method Theoretical Position vs Velocity')
plt.xlabel('Positions (cm)')
plt.ylabel('Speed (cm/s)')
plt.legend()
plt.show()
plt.savefig('Symplectic Method vs Forward Euler Theoretical Position vs Velocity')