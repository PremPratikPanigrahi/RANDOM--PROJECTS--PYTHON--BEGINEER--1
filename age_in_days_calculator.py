loop_start=0
while loop_start==0:


 check_month=["January","February","March","April","May","June","July","August","September","October","November","December"]
 dict_date_1={
   "January":31,
   "February":28,
   "March":31,
   "April":30,
   "May":31,
   "June":30,
   "July":31,
   "August":31,
   "September":30,
   "October":31,
   "November":30,
   "December":31
  }

 try:
  iy=int(input(f"Enter your year of birth: "))
  im=(input(f"Enter your month of birth: "))
  while im not in check_month:
    im=(input(f"Enter your month of birth(in letters with first letter capital): "))
  id=int(input(f"Enter your day of birth: "))
  if iy%4==0:dict_date_1["February"]=29
  while "a":
   while id<1:
    id=int(input("\nDay cannot be less than 1\nRe-enter the day: "))
   while dict_date_1[im]<id:
    id=int(input("\nDay must not be more than number of days in the month entered\nRe-enter the day: "))
   if id>=1 and  dict_date_1[im]>=id:
    break

  cy=int(input(f"\nEnter current year: "))
  cm=(input(f"Enter current month: "))
  while cm not in check_month:
   cm=(input(f"Enter current month(in letters with first letter capital): "))
  cd=int(input(f"Enter current day: "))

  if cy%4==0:dict_date_1["February"]=29
  else:dict_date_1["February"]=28
  
  while "a":
   while cd<1:
    cd=int(input("\nDay cannot be less than 1\nRe-enter the day: "))
   while dict_date_1[cm]<cd:
    cd=int(input("\nDay must not be more than number of days in the month entered\nRe-enter the day: "))
   if cd>=1 and  dict_date_1[cm]>=cd:
    break

 except ValueError or TypeError:
  print(f"Error occured .You have to re-enter everything\nRestarting...\n")
  continue

 if (cy%4)==0:
  f1y=(0.75*cy*365)+(0.25*cy*366)
 elif ((cy-1)%4)==0:
  f1y=(0.75*(cy-1)*365)+(0.25*(cy-1)*366)+365
 elif ((cy-2)%4)==0:
  f1y=(0.75*(cy-2)*365)+(0.25*(cy-2)*366)+((365 )*2)
 elif ((cy-3)%4)==0:
  f1y=(0.75*(cy-3)*365)+(0.25*(cy-3)*366)+((365 )*3)

 if (iy%4)==0:
  f2y=(0.75*iy*365)+(0.25*iy*366)
 elif ((iy-1)%4)==0:
  f2y=(0.75*(iy-1)*365)+(0.25*(iy-1)*366)+365
 elif ((iy-2)%4)==0:
  f2y=(0.75*(iy-2)*365)+(0.25*(iy-2)*366)+((365 )*2)
 elif ((iy-3)%4)==0:
  f2y=(0.75*(iy-3)*365)+(0.25*(iy-3)*366)+((365 )*3)


 fy=f1y-f2y 

 fd=cd-id

 if (cy%4)==0:
  dict_month_leap1={
   "January":0,
   "February":31,
   "March":60,
   "April":91,
   "May":121,
   "June":152,
   "July":182,
   "August":213,
   "September":244,
   "October":274,
   "November":305,
   "December":335
   }
  m_1=dict_month_leap1[cm]

 elif (cy%4)!=0:
  dict_month_leap1={
   "January":0,
   "February":31,
   "March":60-1,
   "April":91-1,
   "May":121-1,
   "June":152-1,
   "July":182-1,
   "August":213-1,
   "September":244-1,
   "October":274-1,
   "November":305-1,
   "December":335-1
  }
  m_1=dict_month_leap1[cm]


 if (iy%4)==0:
  dict_month_leap2={
   "January":0,
   "February":31,
   "March":60,
   "April":91,
   "May":121,
   "June":152,
   "July":182,
   "August":213,
   "September":244,
   "October":274,
   "November":305,
   "December":335
   }
  m_2=dict_month_leap2[im]

 elif (iy%4)!=0:
  dict_month_leap2={
   "January":0,
   "February":31,
   "March":60-1,
   "April":91-1,
   "May":121-1,
   "June":152-1,
   "July":182-1,
   "August":213-1,
   "September":244-1,
   "October":274-1,
   "November":305-1,
   "December":335-1
  }
  m_2=dict_month_leap2[im]


 fm=m_1-m_2

 print(f"\nCongratulations, you have already survived {fm+fd+fy} days\n!!!")

 c=input(f"\nDo you want to continue?\n")
 loop_check=["Yes","No"]
 while c not in loop_check:
  c=input(f"Do you want to continue?(Enter only Yes or No with first letter capital)\n")
 if c=="Yes":
  print("\nRestarting...\n")
 elif c=="No":
  print("\nThanks for using our calculator!\nPlease re-visit");loop_start+=100