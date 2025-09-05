#----------------------------------------Importing current date from datetime module
#----------------------------------------
from datetime import date
#----------------------------------------Creating a variable for today's date
#----------------------------------------
today = date.today()
#----------------------------------------Asking the user for their birth details: year, month, day
#----------------------------------------
birthYear= int(input("Enter your birth year:"))
birthMonth= int(input("Enter your birth month:"))
birthDay= int(input("Enter your birth day:"))
#----------------------------------------Creating a variable called dateOfBirth to store the birth details in date format
#----------------------------------------
dateOfBirth = date(birthYear, birthMonth, birthDay)
#----------------------------------------Creating a variable called userAge to calculate the user's age
#----------------------------------------
userAge = today.year - dateOfBirth.year

if (today.month < dateOfBirth.month) or (today.month == dateOfBirth.month and today.day <= dateOfBirth.day):
  #subtracting one if they haven't had their birthday yet this year
  userAge -=1
#----------------------------------------Age Verification check:
#----------------------------------------
if userAge >= 18:
  print("Your verification passed ✅")
if userAge < 18:
  print("Your verification failed ❌")


