print(f"NOTE: This corrency converter converts currency as per xx,xx,xxxx ")
loop_start=0
while loop_start==0:
 
 expected_input=["1","2","3"]
 
 user_input_a=str(input(f"Enter the 1st currency:\n\t1 for INR\n\t2 for USD\n\t3 for EURO\n"))
 while user_input_a not in expected_input:
  user_input_a=input(f"You entered an unavailable option\nRe-enter: ")
 
 user_input_b =str(input(f"Enter the 2nd currency:\n\t1 for INR\n\t2 for USD\n\t3 for EURO\n"))
 while user_input_b not in expected_input:
  user_input_b=input(f"You entered an unavailable option\nRe-enter: ")
 
 user_input_num=float(input(f"Enter the amount: "))
 
 
 
 if user_input_a == "1" and user_input_b=="1":
  print(f"{user_input_num} INR = {user_input_num*1} INR ")
 if user_input_a == "1" and user_input_b=="2":
   print(f"{user_input_num} INR = {user_input_num*0.012} USD ")
 if user_input_a == "1" and user_input_b=="3":
   print(f"{user_input_num} INR = {user_input_num*0.01} EURO ")


 if user_input_a == "2" and user_input_b=="1":
  print(f"{user_input_num} USD = {user_input_num*85.76} INR ")
 if user_input_a == "2" and user_input_b=="2":
   print(f"{user_input_num} USD = {user_input_num*1} USD ")
 if user_input_a == "2" and user_input_b=="3":
   print(f"{user_input_num} USD = {user_input_num*0.85} EURO ")
  
  
 if user_input_a == "3" and user_input_b=="1":
  print(f"{user_input_num} EURO = {user_input_num*100.35} INR ")
 if user_input_a == "3" and user_input_b=="2":
   print(f"{user_input_num} EURO = {user_input_num*1.17} USD ")
 if user_input_a == "3" and user_input_b=="3":
   print(f"{user_input_num} EURO = {user_input_num*1} EURO ")

 
 loop_check=str(input(f"Do you want to restart?\n"))
 loop__check=["yes","no"]
 while loop_check not in loop__check:
  loop_check=str(input(f"Enter only yes or no (it must only be in lower case)\n"))
 if loop_check=="yes" :
  print(f"Restarting...")
 elif loop_check == "no":
  print(f"Thanks for using my calculator.")
  break
#PLESASE DON'T COPY