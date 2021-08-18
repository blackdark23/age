#systemImport

import os 
import sys
import time 
from os import system
from time import sleep
import requests

#clrnumber

R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'

##### LOGO #####
logo = """
\033[1;96m==============================================
\033[1;96m     
\033[1;96m    ____    __  __   ____    _   _
\033[1;92m   / ___|  |  \/  | / ___|  | | | |
\033[1;96m   \___ \  | |\/| | \___ \  | |_| |
\033[1;92m    ___) | | |  | |  ___) | |  _  |
\033[1;96m   |____/  |_|  |_| |____/  |_| |_|
 
\033[1;93m     Facebook : www.facebook.com/smsh.me
\033[1;96m=============================================
"""

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
        
        
#mainpage

def myage():
    yourname = input(C+" Your Name:"+ Y + " ")
    
    print('')
    
    hp(G+ "Hello,"+C+(yourname)+"!")
    
    sleep(1)
    
    hp(C + (yourname)+ G +" Please Enter Your age... ")
    
    print('')
        
    yourage = input(C+ " Your Age:"+ Y +" ")
        
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
        hp(R +"Sorry system is maybe down!")
        
#text
def wrtt():
    print('')
    hp(G+ "                Allah Hafez          ")
    
    
#rightOrWorng

def right():
    rslt = input(C +"Am I right?(yes/no): ")
    
    
    rslt = rslt.lower()


    if 'yes' in rslt:
        print('')
        yess = rslt.replace('yes','')
        hp(Y + " Welcome.")
        hp(C + " Thank you so much.Pray for me.And a game made with your age will tell me how you felt?")
        hp(C + " Good luck to you.God bless you.")
        wrtt()
        
        
    elif "no" in rslt:
        no = rslt.replace('no','')
        print('')
        hp(Y + " System maybe down.Try to Again.Thank you")
        
    else:
        print('')
        hp(R + "Invalid type.Write yes or no .Try Again.Thank you.Contract me...")
        os.system('xdg-open https://facebook.com/smsh.me')
        right()
       
       
#allFuntion
def pono():
    print('')
    myage()
    print('')
    right()
    print('')
       
       
#playagain 
        
def pag():
    print('')
    playagain = input(C + "Do you want play Again?(yes/no):")
    playagain = playagain.lower()
    
    if 'yes' in playagain:
        print('')
        ye = playagain.replace('yes','')
        sleep(1)
        system("clear")
        print("Play Again...")
        pono()
        print('')
        pag()
        
    elif 'no' in playagain:
        
        print('')
        na = playagain.replace('no','')
        hp(Y + " Please,Type CTRL + C for cancle.Thank you.")
    else:
        print('')
        hp(R + " Invalid type.Write yes or no .Try Again.Thank you.Contract me...")
        os.system('xdg-open https://facebook.com/smsh.me')
        print('')
        pag()



        

system("clear")

print('')
hp('')
print(G + " Hello!I am S M Shakib Hasan ")
hp(logo)

print('')

hp(R + ' If you want to do the job.')
hp(G + ' And if you love your job.' )
hp(R + ' Then one day you will be successful.')
hp(C + ' Inshallah.')
hp(G +  '                  --SMSH')

print('')
h('')
hp(Y + " Going To next page......")

sleep(2)


system("clear")

print('')

hp(R + 'Today I want play your age!')

print('')

hp(Y + "Yeah!Are you ready? ")
hp(W+'')

hp(G + "==============> Let's Start <============")

print('')

hp(G +"Please,Submit your name...")

print('')

myage()

print('')
right()
print('')
sleep(1)
pag()

sleep(60)

print('')

