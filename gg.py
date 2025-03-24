#Isaac F
#Random number averager
#mar 3/24
#this code will make 100 random numbers average them and print it
#-----------------------------------------------------------------------------------
import random
import math
#make list
def list(): return random.randint(1,100)
biglist = [list() for i in range (100) ]
print(biglist)
#average it quick so i can play geoguessr
averg = sum(biglist) / 100
print(averg)