import random
# colors
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'
# code
print (red+b+"""


 ______                           _____ 
 | ___ \                         |  __ \
 | |_/ /  __ _  ___  ___  ______ | |  \/
 |  __/  / _` |/ __|/ __||______|| | __ 
 | |    | (_| |\__ \\__ \        | |_\ \
 \_|     \__,_||___/|___/         \____/
                                        
                                        


                                                   v 1.0
"""+b+red)

print (gren+b+"              <===[[ coded by SHOAIB ]]===>"+b+gren)
print (" ")
print (yellow+b+"        <---( search on youtube termux hackers )--->"+b+yellow)
print (" ")

length=int(input(cyan+b+"Enter The Length Of The Password: "+b+cyan))
print (" ")
print (yellow+b+"-----> password  generated <----"+b+yellow)
print (" ")
char="abcdefghijklmnopqrstuvwxyz1234567890@#$%&*^"
password= (gren+b+" "+b+gren)
for i in range(length):

     password+=random.choice(char)

print(password)
print (" ")
print (yellow+b+"-----> grab your password <----"+b+yellow)
print (" ")
