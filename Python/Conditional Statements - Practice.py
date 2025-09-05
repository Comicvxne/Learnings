#----------------------------------------creating multiple statemnts in one line
def whatIsTheWeatherLike(weather, rating):
  if weather == "snowing":
      print("snowing")
      if rating > 2:
          print("happy")
      else: 
          print("sad")
  elif weather == "sunny" and rating > 2:
      print("sunny and happy")
  elif weather == "sunny" and rating == 1:
    print("sunny but saf")
  else:
    print("else case")
#----------------------------------------

#----------------------------------------using input() for user choice
weather = input("What is the weather?")
#----------------------------------------

#----------------------------------------using int() to convert string to integer 
rating = int(input("How was your day 1 -5?"))
#----------------------------------------

#----------------------------------------calling the function to get result based on user input
whatIsTheWeatherLike(weather, rating)
#----------------------------------------
