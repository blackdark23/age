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
        time.sleep(8.0 / 60)
        
def h(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8.0 / 9)
        

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
hp(G + "========> Let's Start <=======")
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
    hp(G +"Sorry system is maybe down!")
    
print('')

rslt = input(C +"Am I right?(yes/no)[without Space]: ")
yess = ("yes")
noo = ("no")
y = str(yess)
n = str(noo)


if (rslt == y):
    print('')
    hp(Y + "Welcome.")
    hp(C + "Thank you so much.Pray for me.And a game made with your age will tell me how you felt?")
    hp(C + "Good luck to you.God bless you.")

elif (rslt == n):
    print('')
    hp(Y + "System maybe down.Try to Again.Thank you")

else:
    print('')
    hp(R + "Invalid type.Write yes or no without space.Try Again.Thank you.Contract me...")
    os.system('xdg-open https://facebook.com/smsh.me')
    os.system('reload')



print('')


hp(G + "          Allah Hafez         ")

print('')
