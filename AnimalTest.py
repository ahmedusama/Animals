# -*- coding: utf-8 -*-
"""
Created on Mon May 22 18:05:58 2017

@author: Ahmed Usama Khalifa
"""
from Animal import Dog

Lasse =  Dog(n = ['Lasse'],c = ['Brown'],Ec= ['Red', 'Black'],N= 'Jp',H = 80)
Marf  =  Dog(n = ['Marf'],c = ['Brown'],Ec= ['Red', 'Black'],N= 'US',H= 50,L= 60,W= 70)
Saso  =  Dog(n = ['Saso'],c = ['White'], Ec=['Orange', 'blue'],N= 'Egy',H=40,L= 40)

print (Lasse.Hight)
Lasse.sit ()  
Lasse.come ('NY HAW')            
Marf.come ('Come here')
Saso.come ('Come here')
print (Dog.number_of_dogs)