import os
import sys
import time
from os import system
from time import sleep

import requests

R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'

def hp(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8.0 / 70)
        
        
system("clear")
print('')
hp('')
print(G + "Hello!I am S M Shakib Hasan ")
print('')
hp(R + 'If you want to do the job')
hp(G + 'And if you love your job.' )
hp(R + 'Then one day you will be successful.')
hp(C + 'Inshallah')
hp(G +  '                  --SMSH')

print('')

hp(R + 'Today I want play your age!')
print('')
hp(Y + "Yeah!Do not afraid.")
hp(W+'')
hp(G + "--------Let's Stat-------")
print('')

kidage = 12+1
kage =str(kidage)
age =14+4
agee =str(age)
yourage = 'true'
while (yourage == 'true'):
    yourage = input(C+ "You Age: ")
    
    if(yourage <= kage):
        hp(G + "You are kid!")
        
    elif(yourage <= agee):
        hp(G + "You are teenager!")
            
    else:
        hp(G +"You are adult!")
print('')


hp(Y + "Welcome.Thanks you so much.And pray for me.")

hp('')

hp(G +          "Allah Hafez         ")
