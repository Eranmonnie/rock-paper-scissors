import random

plays=["R","P","S"]

print ("welcome to the rock paper sissors game!!")

x=True

while x:
   P1_choice=input("pick an option between R: Rock, P: paper or S: Sissors:\n")
   
   if P1_choice in plays:
     
     print ("Time for CPU to choose....\n")
     
     CPU_choice = random.choice(plays)
     
     if P1_choice == CPU_choice:
         print ("Player : ("+P1_choice+")\nCPU choice :("+CPU_choice+")\n")
         
         print ("**TIE**")
         x=True
         
     elif (P1_choice== "R" and CPU_choice== "S")or(P1_choice== "P" and CPU_choice== "R")or(P1_choice== "S" and CPU_choice== "P"):
         print ("Player : ("+P1_choice+")\nCPU choice :("+CPU_choice+")\n")
         
         print ("YOU WIN!!!!!!!!")
         x=False
         
     elif (P1_choice== "R" and CPU_choice== "P")or(P1_choice== "P" and CPU_choice== "S")or(P1_choice== "S" and CPU_choice== "R"):
         print ("Player : ("+P1_choice+")\nComputers choice :"+(CPU_choice))
         print("")
         print ("CPU WINS!!!!!!!!")
         x=False
        
   else :
       print ("invalid option")
       