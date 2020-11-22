#Juan Pablo Alfonzo
#1003915132

#Comp Assigment 1: Introduction to Scientific Computing 

#Question 1: numpy operations
print('Question 1')
import numpy as np
a=1
b=np.array([3.0,2.3,1.0])
c=np.array([3,.3,.03])
d=np.array([[2,4],[4,6],[7,8]])
f=[9,90,900]

print('The sum of a and b is:', a+b)
print('The sum of c and b is:', c+b)
print('The sum of c and collumns of d', c+d[:,0], c+d[:,1]) #When having an array, a, a[c,d] indicates row c column d  
print('The sum of b and f is', b+f)
print('The type variable stored in d is', type(d[1,0]))
print('The type of variable stored in f is', type(f[1]))
print('The lenght of d is:', len(d))
print('The lenght of f is:', len(f))
print('')
print('')

#Question 2: numpy functions
print('Question 2')
t= np.array([0.    , 0.1155, 0.2287, 0.3404, 0.4475,0.5546, 0.6607, 0.7753, 0.8871, 1.    ])
y=np.array([ 0.    ,  0.1655,  0.2009,  0.1124,-0.0873, -0.3996, -0.8197, -1.3977,-2.0856, -2.905 ])

print('The average of all the values in y is', np.mean(y)) #Where np.mean takes the mean value of all array elements
print('The standard deviation of values in y is', np.std(y)) #Where np.std takes the standard deviation of all array elements

#Finding dy/dt

#Setting up for loop to find delta y

dy=np.zeros([1,len(y)-1]) #empty array to take in calculated values of dy

for i in range(0,len(y)-1): #Setting bounds for the for loop to run over
    dy[0,i]=y[i+1]-y[i] #Computing delta y according to given equation 

#Doing the same as above but for dt
dt=np.zeros([1,len(y)-1]) 

for i in range(0,len(y)-1):
     dt[0,i]=t[i+1]-t[i]

#Now we can calculate the derivative as follows
deri=np.zeros([1,9]) #Empty array to add dy/dt calculations from for loop    

for i in range (0,9):
    deri[0,i]=(dy[0,i])/(dt[0,i]) #Caluclate dy_i/dt_i
    
derivative=np.mean(deri) #Finding average of dy_i/dt_i will give us the differential 

print('This is dy/dt:', derivative)
    
#Finding Integral

#First calculate E(y_i)as follows:

E=np.zeros([1,9]) #Empty array that will store E(y_i) values
for i in range(0,9):
    E[0,i]=0.5*y[i]**2    
    
#Now we mutliply E(y_i) by delta t 
I=np.zeros([1,9])#Empty array that will store area of segments with width dt and height E(y) 
for i in range(0,9):
    I[0,i]=E[0,i]*dt[0,i]
    
Area=np.sum(I) #suming all areas to get integral

print('The Intergral of Energy is:', Area)
print('')
print('')

#Question 3: Implmenting Equations in Python
#Part 1
print('Question 3')
def g(l,t): #Where l is lenght and t is period as inputs
    a=(4*((np.pi)**2)*l)/(t**2) #Writing equation to output value of g
    return(a) #returning above calculated value

#Testing if function works for l=2.5m and t=5.16s
print('The acceleration due to gravity given a pendulum of length 2.50m and and period of oscillation of 5.16s is:', g(2.5,5.16))

#Part 2
def gu(l,lu,t,tu): #where l is lenght, lu is length uncertanty, t is period, and t is period uncertanty 
    b=(lu/l)*100
    c=(tu/t)*100
    d=(c**2+b**2)**(1/2)
    e=g(l,t)*(d/100)
    return(e)

#Testing if function works given conditions in question
print('The uncertainty of g assuming l = 2.40 ± 0.01m and T = 5.0 ± 0.01s is: ±', gu(2.4,0.01,5,0.01), 'm/s^2')
print('')
print('')
#Question 4: Conditionals
print('Question 4')
#Create a function that checks if inputed numerical scale of grade is in a certain range
#if it is not then proceed to check if it is in subsequent range until it finds correct range
#when in corrected range the associated grade point value of the range will be returned by the function

def GPV(NSM):
    global a #Define a globally so it can be accessed outside of function 
    if NSM in range(-1,50):
        a=0
    else:
        if NSM in range(49,53):
            a=0.7
        else: 
            if NSM in range(52,57):
                a=1.0
            else:
                 if NSM in range(56,60):
                     a=1.3
                 else:
                      if NSM in range(59,63):
                          a=1.7
                      else:
                           if NSM in range(62,67):
                               a=2.0
                           else: 
                                if NSM in range(66,70):
                                    a=2.3
                                else:  
                                    if NSM in range(69,73):
                                        a=2.7
                                    else:
                                         if NSM in range(72,77):
                                             a=3.0
                                         else:
                                              if NSM in range(76,80):
                                                  a=3.3
                                              else:
                                                   if NSM in range(79,85):
                                                       a=3.7
                                                   else:  
                                                       if NSM in range(84,101):
                                                           a=4.0
    return(a)

#Testing for some particular grade
print('The Grade Point Value of a 70% Numerical Scale of Grade is:', GPV(72))
print('')
print('')
#Question 5: Loops                                                       
print('Question 5')
marks= np.array([72, 82, 72, 72, 79, 57, 59, 71, 66, 80,
67, 62, 91, 74, 77, 62, 71, 78, 65, 80,
70, 74, 70, 95, 76, 66, 85, 64, 79, 57,
63, 78, 84, 78, 75, 73, 62, 69, 72, 87])

AGPA=np.zeros([1,len(marks)]) #empty array to hold GPAs

#Create a wild loop that runs each element in the marks array 
#through the function GPV to convert the number grades into grade point values

for i in range(0,len(marks)):
    AGPA[0,i]=GPV(marks[i])
    
#Now to find avergae GPA we simply find average of the AGPA array
print('The Average GPA for PHY224 in 2019 was:', np.mean(AGPA))
print('')
print('')
#Question 6: Data Comparison
print('Question 6')
def check(mv,u,ev): #where mv is measured value, u is uncertanty, and ev is expected value
    if np.absolute(mv-ev)<u: #If statement checks if the absolute value of the difference between
        return(True)         #measured and expected value is less then uncertanty, if yes it 
    else:                     #prints true if not it prints false   
        return(False)

print('Trial 1 check:',check(19.2,0.1,19.41))
print('Trial 2 check:',check(19.5,0.8,19.41))
print('Trial 3 check:',check(19.5,0.1,19.41))        



