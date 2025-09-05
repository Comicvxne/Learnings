#Using multiple if statements to check weather and rating
#---------------------------------------------------------------------------------
def whatIsTheWeather(weather, rating):
  if weather == "snowing":
    print("snowing")
    if rating > 2:
      print("happy")
    else:
      print("sad")
  elif weather == "sunny" and rating > 2:
    print("sunny and good day")
  elif weather == "sunny" or rating == 1:
    print("sunny and bad day")
  else:
    print("else case")

weather = input("What is the weather?")
#converting str into int with the int() function
rating = int(input("What is the rating from 1 to 5?"))
whatIsTheWeather(weather, rating)
#---------------------------------------------------------------------------------
#Cheat Sheet
#--------------
#Conjunction all to be true -> and
#Union at least one to be true -> or
#Negation not true flips the true to falls and falls to true -> not
