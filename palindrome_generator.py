import random
import string
import time
print("This is the best python based palindrone checker and generator")


x=1
while x==1:
 Input=int(input("Enter\n1 if you want to check if  a given number is palindrone or not\n2 if you want to generate a palindrone number\n\n")) 
 while Input!=1 and Input!=2:
  Input=int(input("\nEnter\n1 if you want to check if  a given number is palindrone or not\n2 if you want to generate a palindrone number\n\n"))
 
 if Input ==1:
  y=1
  while y==1:
   k = random.randint(1, 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)  

   length_str = random.choice(string.digits[1:])
   if k > 1: 
     length_str += ''.join(random.choices(string.digits, k=k - 1))
  
   num_digits = int(length_str)

   n_1 = random.choice(string.digits[1:]) + ''.join(random.choices(string.digits, k=num_digits - 1))
   a=int(n_1)
   number=str(n_1)

   if number == number[::-1]:
    print(f"\n\n{number} is a palindrome number.") 
    while "a"  :
     d=str(input("\nDo you want to generate another palindrome number?\n(Enter 'y' for yes and 'n' for no)\n\n"))
     while d!="y" and d!="n":
       d=str(input("\nDo you want to generate another palindrome number or check if a number is palindrome or not?\n**Enter 'y' for yes and 'n' for no**\n\n"))
     if d=="y" :
      print("\nRestarting...\n")   
      time.sleep(1)
      y+=1
      break
      
     else:print("Thank you for using the palindrome checker and generator\n");x+=1;y+=1;break
 else:
  try:
   q=input("Enter the number: ")
  except ValueError:
   print("\nYou have entered something other then a integer number.Restarting...\n")
   time.sleep(2)
  if  q == q[::-1]:
   print(f"{q} is a palindrone number.")
  else: print(f"{q} is not a palindrone number.")
  while "a"  :
     d=str(input("\nDo you want to generate another palindrome number?\n(Enter 'y' for yes and 'n' for no)\n\n"))
     while d!="y" and d!="n":
       d=str(input("\nDo you want to generate another palindrome number or check if a number is palindrome or not?\n**Enter 'y' for yes and 'n' for no**\n\n"))
     if d=="y" :
      print("\nRestarting...\n")   
      time.sleep(1)
      break
     else:print("Thank you for using the palindrome checker and generator\n");x+=1;break