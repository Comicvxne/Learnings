#----------------------------------------# Step 1: Store the current year in a variable
currentYear = 2025
#----------------------------------------Step 2: Define a function to check age based on year of birth
def ageVerification(currentYear, dateOfBirth):
#----------------------------------------Step 3: Calculate age by subtracting year of birth from current year
#Step 4: If the person is older than 18 OR exactly 18, they pass verification
  if currentYear - dateOfBirth > 18 or currentYear - dateOfBirth == 18:
#----------------------------------------Step 5: Print success message if they pass verification
    print("You are passed the verification")
#----------------------------------------Step 6: Print failure message if they fail verification
  else: 
    print("Verification failed")
#----------------------------------------Step 7: Ask the user to enter their year of birth (input always gives string, so convert to int)
dateOfBirth = int(input("What is your year of birth?"))
#----------------------------------------Step 8: Call the function with current year and the user’s input
ageVerification(currentYear, dateOfBirth)
#----------------------------------------
