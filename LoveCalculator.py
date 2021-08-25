# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1=name1.lower()
name2=name2.lower()

T=name1.count('t')
R=name1.count('r')
U=name1.count('u')
E=name1.count('e')
L=name1.count('l')
O=name1.count('o')
V=name1.count('v')
E=name1.count('e')

T1=name2.count('t')
R1=name2.count('r')
U1=name2.count('u')
E1=name2.count('e')
L1=name2.count('l')
O1=name2.count('o')
V1=name2.count('v')
E1=name2.count('e')

score1=T+R+U+E+T1+R1+U1+E1
score2=L+O+V+E+L1+O1+V1+E1

score1=str(score1)
score2=str(score2)

score1+=score2

score=int(score1)

if score<10 or score>90:
             print("Your score is {}, you go together like coke and mentos.".format(score))
elif score>40 or score<50:
             print("Your score is {}, you are alright together.".format(score))
else:
    print("Your score is {}.".format(score))

