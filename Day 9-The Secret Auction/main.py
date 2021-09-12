from replit import clear
from art import logo
print(logo)
print("Welcome to the secret auction program.")
max=0
temp="yes"
dict={}
while(temp=="yes"):
        name=input("What is your name?: ")
        bid=int(input("What's your bid?: $"))
        if(bid>max):
                max=bid
                dict["bid"]=max
                dict["Bidders_name"]=name    
        temp=input("Are there any other bidders? Type 'yes'or 'no'.")
        if(temp=='yes'):
          clear()
clear()
print("The winner is {} with a bid of ${}.".format(dict["Bidders_name"],dict["bid"]))
