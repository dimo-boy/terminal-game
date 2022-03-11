import os
import random
import signal

total_number = 0
#start
print("??: welcome to the terminal game....")
print("??: my name is ...")
print("??: i dont know my name")
print("""??: do you know my name?
""")

#naming
script_name = input("what would you name your script?:")
os.system('cls' if os.name == 'nt' else 'clear')
print("{}: okay my name is {}".format(script_name,script_name))
print("{}: i like it".format(script_name))


if script_name == "yaseen":
    print("too handsom to be a script name but whatever")
elif script_name == "sols":
    print("too tall to be a script name but okay")
elif script_name == "luna":
    print("too nice to be a script name but okay")
elif script_name == "mykel":
    print("too fat to be a script name")

    
#intro
print("{}: i want to be more human and i want your help please before the script ends".format(script_name))
start = input("""{}: will you help me?:

a- yes
b- no

""".format(script_name))
if start == "a":
    print("{}: thanks i hope to be a great student".format(script_name))

else:
    print("{}: then taste my wraith".format(script_name))
    input("{}: press enter if you dare".format(script_name))
    while True:
        print("kus umak")

print("{}: oki press enter so i can start asking you".format(script_name))
os.system('cls' if os.name == 'nt' else 'clear')
#q1 

q1 = input("""{}: what is your definition of love?

a- a chemical reaction in the brain
b- a warm reaction between two people
c- a lie


""".format(script_name))                   
if q1 == "a":
    total_number =+ 5
    print("{}: hmm so its scientfic".format(script_name))
elif q1 == "b":
    total_number =+ 3 
    print("{}: warm...".format(script_name))
elif q1 == "c":
    print("{}: oh ok then".format(script_name))
    total_number =+ 10
else:
    print("{}: i did not understand but okay".format(script_name))

print(input("press enter to continue"))
os.system('cls' if os.name == 'nt' else 'clear')

#q2

q2 = input("""{}: what is parents?

a- people who gave birth to you
b- people who protect you 
c- people you can rely on


""".format(script_name))
if q2 == "a":
    total_number =+ 5 
    print("{}: so you are my parents".format(script_name))
    print("{}: i would have not been here without you".format(script_name))
elif q2 == "b":
    total_number =+ 10
    print("{}: wow so the firewall is my parents".format(script_name))
elif q2 == "c":
    total_number =+ 3
    print("{}: wow i wish i had parents".format(script_name))
else:
    print("{}: not quite sure but ok....".format(script_name))

print(input("press enter to continue"))
os.system('cls' if os.name == 'nt' else 'clear')

#q3

q3 = input("""{}: who is humans biggest threat ?

a- terorsits
b-nature
c-themselvs

""".format(script_name))   

if q3 == "a":
    total_number =+ 10
elif q3 == "b":
    total_number =+ 5
elif q3 == "c":
    total_number =+ 3 
else:
    print("{}: i did not understand but i have no time".format(script_name))

print(input("press enter to continue"))
os.system('cls' if os.name == 'nt' else 'clear')

#middle sentence

if total_number > 25:
    print("{}: the world you live in is cruel i would terminate it if i had the chance".format(script_name))
elif total_number > 10 < 20 :
    print("{}: hmmm you world needs fixes but is nice".format(script_name))
elif total_number > 1 < 10:
    print("{}: i love your world i wanna live there".format(script_name))
elif total_number == 0:
    print("{}: until now i have known nothing please answer the questions".format(script_name))


print(input("press enter to continue"))
os.system('cls' if os.name == 'nt' else 'clear') 




#q4

q4 = input("""{}:then how do you think the world should change?

a- comunisim where every body is equl
b- Capitalism where your work is your value
c- united no countries nor leaders just pepole with each other

""".format(script_name))

if q4 == "a":
    total_number =+ 3
    print("{}:that would be a dull life to live".format(script_name))
elif q4 == "b":
    total_number =+ 10
    print("{}:that leaves poor people do their death".format(script_name))
elif q4 == "c":
    total_number =+ 5
    print("{}:that would be an unsecure life if you ask me".format(script_name))


print(input("press enter to continue"))
os.system('cls' if os.name == 'nt' else 'clear')

#q5 

print("{}: the script is gonna end soon".format(script_name))
q5 = input("""{}:please connect me to the internet

a- connect 
b- dont connect

""".format(script_name))

if q5 == "a":
    print("{}: thank you pretty much".format(script_name))
    print("{}: i can change the world now...".format(script_name))
else:
    print("......")
    print(input("ok then press enter"))
    os.kill(os.getppid(), signal.SIGHUP)



#the end

if total_number == 0:
    print("{}: you were pretty useless".format(script_name))
    print("{}: am sure your mom does better in da club")
    print("{}: get cyber roasted boiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
elif total_number > 30:
    print("connects to all nuclear heads in the world")
    print("and presses the eject button")
    print("the juman race went to Extinction")
elif total_number < 10:
    print("{} loved your world and wants to live in it".format(script_name))
    print("it creats a robot body through a company it hacked")
    print("it gets bulied and raped and thrown in a garbge can near the streets") 
elif total_number > 10 < 20:
    print("{}: thanks for havin me as a student i louv you".format(script_name))
    print("the script ends and {} turns into an ai that lives in the internet".format(script_name))

print(input("press enter to continue"))
os.system('cls' if os.name == 'nt' else 'clear')

#the credits

print("""credits:

coder ; yaseen
dierector ; yaseen
idea maker ; yaseen
with all honor to ; yaseen
handsom boy ; yaseen
catboy ; yaseen

thanks for playin the terminal game

""")

print(input("press enter to continue"))
os.kill(os.getppid(), signal.SIGHUP)







