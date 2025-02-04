import random
sum=1
name=input("Hello, what's ur name?")
sluchainoe=random.randint(1,20)
print("Well, ",name," guess the number between 1 and 20")
a=int(input())
while a!=sluchainoe:
    if a<sluchainoe:
        print("Ur guess is too low.")
    else:
        print("Ur guess is too high")
    a=int(input())
    sum+=1
print("U guesses the number in ",sum," tries.")
