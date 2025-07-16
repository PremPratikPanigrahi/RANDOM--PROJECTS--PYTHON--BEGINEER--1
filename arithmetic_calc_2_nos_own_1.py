print("arithmetic calculator for 2 numbers")
print(" ")
print("Use the following arithmetic calculators:- ")
print(" ")
print("/ for division")
print("- for subtraction")
print("+ for addition")
print("* for multiplication")
print("// for approx quotient obtained by division")
print("%", "for reminder obtained by dividing ")
print("^ to find exponential form")
z=0
y=1
while z == 0 and y == 1 :
 print(" ")
 
 a = int(input("Enter first number: "))
 if a == ValueError :
  print("Don't enter non integer number !!!")
 else :
  c = str(input("Enter a arithmetic operator: "))
  if c != "-" and c!="+" and c!="*" and c!="/" and c!= "//"and c!="*"and c!="%":
   print("You must enter arithmetic operator only ( + or - or * or / or // or ^ or % )")
  else :
   b = int(input("Enter second number: "))
   print(" ")
   if b == ValueError :
    print("Don't enter non integer number !!!")
   elif c == "+":
    print(a+b)
   elif c == "-":
    print(a-b)
   elif c == "*":
    print(a*b)
   elif c == "/":
    print ("Quotient is",a/b)
    print("Approximate quotient is", a//b)
    print("Remainder is", a%b)
   elif c =="%":
    print(a%b)
   elif c == "//":
    print(a//b)
   elif c == "*":
    print(a**b)
 
 if y >= 0:
  print("Do want more opertions? ")
  print("Press ")
  print("1 for yes ")
  print("2 for no ")
  d=int(input())
  if d == 1:
   z += 0 
   y-=0
  elif d == 2 :
   z+=1
   y-=10
   print("THANK YOU")
  elif d>=3 or d<=0:
   print("Error occured because you pressed number other than 1 and 2 so,restart")
   y-=20
   z-=20