
import pandas as pd
import numpy as np
import random

#name=input("Hello sir enter your name please :")
#print("Welcome {} ".format(name))
print("gause 1 is for rock,2 for paper and 3 for scissors")
yourchoice=int(input("please enter  yourchoice the number \n"))
if (yourchoice==1):
      yourchoice="rock"
elif (yourchoice==2):
      yourchoice="paper"
elif (yourchoice==3):
      yourchoice="scissors"
else:
    yourchoice=='NULL'
print("you have gauss ",yourchoice)

otherchoice=np.random.randint(1,4)
if (otherchoice==1):
      otherchoice="rock"     
elif (otherchoice==2):
      otherchoice="paper"
elif (otherchoice==3):
      otherchoice="scissors"
else:
    otherchoice=='NULL'
print("other have been chocien is ",otherchoice)


if (otherchoice==yourchoice):
      print("match tie")    
elif (otherchoice=='rock' and yourchoice=='paper'):
      print("you win")
elif (otherchoice=='scissors' and yourchoice=='paper'):
      print("you loss")
elif (otherchoice=='paper' and yourchoice=='rock'):
      print("you loss")
elif (otherchoice=='scissors' and yourchoice=='rock'):
      print("you win")
elif (otherchoice=='paper' and yourchoice=='scissors'):
      print("you win")
elif (otherchoice=='rock' and yourchoice=='scissors'):
      print("you loss")




