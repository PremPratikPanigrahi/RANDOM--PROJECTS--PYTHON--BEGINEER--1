import random
b=int(input(f"Enter a number between 1 and 100: "))
a=random.randint(1,100)
while b!=a:
 a=random.randint(1,100)
 b=int(input(f"Enter a number between 1 and 100(previous guess was wrong): "))
 if b==a:break
print(f"Congratulations you have guessed the number correctly.") 
