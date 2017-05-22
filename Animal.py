
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 18:05:58 2017

@author: Ahmed Usama Khalifa
"""
# create name of class 
class Dog :
    number_of_dogs = 0  #shared variable 
    def __init__(self, n, c, Ec, N, H, L=50, W=30) : 
        Dog.number_of_dogs += 1  
        self.name      =  n    
        self.color     =  c   
        self.Eyecolor  =  Ec  
        self.National  =  N   
        self.Hight     =  H    
        self.Length    =  L    
        self.Weight    =  W    
       
  
# create Methods (functions)
    def come (self,command): # sit function
         if  command == 'NY HAW' and self.National == 'Jp':
              print (self.name,"is comming Now !")
         elif self.National == 'Egy' and command == 'T3ala hena':
              print (self.name,"is comming Now !")
         elif self.National == 'US' and command == 'Come here':
              print (self.name,"is comming Now !")
         else:
              print (self.name,"didn't got it")
  
    def sit (self): 
             print (self.name,"is sitting Now !")          





 
            
            