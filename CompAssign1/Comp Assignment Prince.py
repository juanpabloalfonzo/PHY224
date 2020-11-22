# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 09:37:41 2020

@author: param
"""

#Parampreet Singh
#1004191457
#parampreet.singh@mail.utoronto.ca

import numpy as np

def AccelerationGravity(length, period): #Define a function to calculate acceleration due to gravity from a pendulum length and period
    g=((4*((np.pi)**2))*length)/(period**2)
    
    return g

def AccelerationGravityError(length2, lengthERROR, period2, periodERROR): #Define a function which calculates the error in the acceleration due to gravity given a pendulums length, error in length, period, and error in period
    lengthERRORpercent=(lengthERROR/length2)*100
    periodERRORpercent=(periodERROR/period2)*100
    g=((4*((np.pi)**2))*length2)/(period2**2)
    gERRORpercent=((lengthERRORpercent**2)+(periodERRORpercent**2))**(1/2)
    gERROR=g*(gERRORpercent/100)
    
    return gERROR

def gpa(num): #Define a function to determine a gpa through a given number mark through simple conditional checks
    if 0<=num<=49:
        return 0
    elif 50<=num<=52:
        return 0.7
    elif 53<=num<=56:
        return 1.0
    elif 57<=num<=59:
        return 1.3
    elif 60<=num<=62:
        return 1.7
    elif 63<=num<=66:
        return 2.0
    elif 67<=num<=69:
        return 2.3
    elif 70<=num<=72:
        return 2.7
    elif 73<=num<=76:
        return 3.0
    elif 77<=num<=79:
        return 3.3
    elif 80<=num<=84:
        return 3.7
    elif 85<=num<=89:
        return 4.0
    elif 90<=num<=100:
        return 4.0
    else:
        return ("ERROR! Please enter a numerical scale of mark in between 0 and 100.")
    
def AgreementCheck(measurement, error, known):
    if np.absolute(measurement-known)<error:
        return ("True")
    elif np.absolute(measurement-known)>=error:
        return ("False")
    
    
    

#Question 1
print("Question 1")


a=1
b=np.array([3.0, 2.3, 1.0])
c=np.array([3, .3, .03])
d=np.array([[2,4], [4,6], [7,8]])
f=[9, 90, 900] #Assign variables

#The sum of a and b
print("The sum of a and b is: ", a+b) #Calculate sum of a and b

#The sum of c and b
print("The sum of c and b is: ", c+b) #Calculate sum of c and b

#The sum of c and d
print("The sum of c and d is: ", c+d[:,0], c+d[:,1]) #Calculate sum of c with each col of d

#The sum of b and f
print("The sum of b and f is: ", b+f) #Calculates sum of b and f

#Type variable stored in d, and in f
print("The type of variable stored in d is: ", type(d[0,0]), "and the type of variable stored in f is: ", type(f[0])) #Checks varable type of the elements d and f

#The length of d and the length of f
print("The length of d is: ", len(d), "and the length of f is: ", len(f)) #Calculates the length of d and f


print("")
print("")


#Question 2
print("Question 2")


t=np.array([0. , 0.1155, 0.2287, 0.3404, 0.4475,0.5546, 0.6607, 0.7753, 0.8871, 1.])
y=np.array([0. , 0.1655, 0.2009, 0.1124, -0.0873, -0.3996, -0.8197, -1.3977,-2.0856, -2.905]) #Assign variables

#The average of all values in y
print("The average of all values in y is: ", np.mean(y)) #Takes the average of the array y

#The sample standard deviation of values in y
print("The sample standard deviation of the values in y is: ", np.std(y)) #Takes the standard deviation of the array y

#The differential dy/dt
DELTAy=np.zeros([1, len(y)-1]) #Create empty array to store Delta y
DELTAt=np.zeros([1, len(t)-1]) #Create an empty array to store Delta t
for i in range (0,len(y)-1): #Calculate Delta y using a simple for loop and store this in DELTAy empty array
    DELTAy[0,i]=y[i+1]-y[i]
    
for i in range (0,len(t)-1): #Calculate Delta t using a simple for loop and store this in DELTAt empty array
    DELTAt[0,i]=t[i+1]-t[i]

DELTAarray=np.zeros([1,9]) #Calculate dy_i/dt_i for each element in DELTAy and DELTAt
for i in range (0, 9):
    DELTAarray[0,i]=DELTAy[0,i]/DELTAt[0,i]
Differentialy=np.mean(DELTAarray) #Take the mean of all dy_i/dt_i to get final answer
print("The differential of y with respect to t (dy/dt) is: ", Differentialy)

#The integral of energy
Integral=np.zeros([1,10]) #Create an empty array to store differentials
for i in range (0, 9): #Calculate all differentials by taking dy_i/dt_i and store this in the empty array defined previously
    Integral[0,i]=((1/2)*((y[i])**2)*(DELTAt[0,i]))
FinalIntegral=np.sum(Integral) #Take the mean of all differentials in order to get the best value possible
print("The integral of energy is: ", FinalIntegral)


print("")
print("")


#Question 3
print("Question 3")


print("The acceleration due to gravity for l=2.50m and T=5.16s is: ", AccelerationGravity(2.50,5.16), "ms^-2") #Call the function defined previously to calculate g
print("The error in the acceleration due to gravity for l=2.40m +/- 0.01m and T=5.0s +/- 0.01s is: +/-", AccelerationGravityError(2.40, 0.01, 5.0, 0.01), "ms^-2") #Call the function defined prevously to calculate the uncertainty in g


print("")
print("")


#Question 4
print("Question 4")


print("The grade point average corresponding to this numerical scale of mark is: ", gpa(89))


print("")
print("")


#Question 5
print("Question 5")


marks=np.array([72, 82, 72, 72, 79, 57, 59, 71, 66, 80, 67, 62, 91, 74, 77, 62, 71, 78, 65, 80, 70, 74, 70, 95, 76, 66, 85, 64, 79, 57, 63, 78, 84, 78, 75, 73, 62, 69, 72, 87])
gpaList=np.zeros([1,len(marks)])
for i in range (0, len(marks)):
    gpaList[0,i]=gpa(marks[i])
AverageGPA=np.mean(gpaList)
print("The average GPA of the PHY224 class in 2019 is: ", AverageGPA)


print("")
print("")


#Question 6
print("Question 6")
print("The result for Trial 1 is: ", AgreementCheck(19.2, 0.1, 19.41))
print("The result for Trial 2 is: ", AgreementCheck(19.5, 0.8, 19.41))
print("The result for Trial 3 is: ", AgreementCheck(19.5, 0.1, 19.41))