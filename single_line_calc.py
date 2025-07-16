print(f"You're currently seeing the best calculator of the world\n\nUse the following operators:\n\t/  : Division\n\t-  : Subtraction+  : Addition\n\t*  : Multiplication\n\t// : Integer (approximate) quotient\n\t%  : Remainder\n\t** : Exponentiation\n\t() : For brackets operations")
a=0
while a == 0:
 try:
     d = int(eval(input("Enter: ")))
     print(f"Answer = {d}")
 except Exception as e:
     print(f"Error: {e}")
     print("You entered something invalid. Restarting...")
     continue 
 c=1
 while c ==1:
  b=int(input(f"Enter 1 to continue and 2 to stop: "))
  if b==1:a+=0;c+=1
  elif b==2:print("Thanks for using the calculator");a+=1;c+=1
  elif b<1 or b>2:print (f"Please follow the instructions") 