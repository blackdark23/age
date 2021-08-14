import os
import sys
import time
from os import system
from time import sleep

import requests

#clrnumbr
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'

#fortextdesign
def hp(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8.0 / 70)
        
def h(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8.0 / 8)
        

system("clear")
print('')
hp('')
print(G + "Hello!I am S M Shakib Hasan ")
print('')
hp(R + 'If you want to do the job.')
hp(G + 'And if you love your job.' )
hp(R + 'Then one day you will be successful.')
hp(C + 'Inshallah.')
hp(G +  '                  --SMSH')

print('')

hp(R + 'Today I want play your age!')
print('')
hp(Y + "Yeah!Are you ready? ")
hp(W+'')
hp(G + "--------> Let's Start <-------")
print('')

#stuctr

yourname = input(C+"Your Name:"+ Y + " ")

print('')

sleep(1)

hp(C + (yourname)+ G +" Please Enter Your age... ")

print('')
    
yourage = input(C+ "Your Age:"+ Y +" ")
    
print('')

hp(R + "Your age is Multiplying... " )

print(R + "Please Wait...")

print('')

sleep(1)

h(W + "1...25...50...75...85...90...100")

print('')

sleep(2)

hp(G + "Multiplying successfully Done...!")

sleep(1)

age = int(yourage)

if(age <= 12):
    print('')
    hp(C + (yourname)+ G + " You are kid!")
        
elif(age <= 18):
    print('')
    hp(C + (yourname)+ G + " You are teenager!")
        
elif(age >= 18):
    print('')
    hp(C + (yourname)+ G +" You are adult!")
    
else:
    hp(G +"Sorry system is down!")
    
    
print('')




hp(Y + "Welcome.Thanks you so much.And pray for me.")

print('')


hp(G + "          Allah Hafez         ")

print('')
