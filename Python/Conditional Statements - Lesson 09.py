#Conditional Statements: which is basically is a statement of the form! 
# if _____ then ________ 
#if __🌧️__then __☂️__
#we can think as asking a simple yes or no question, we in the programong instead of using yes or a no we use true of false which is a type of boolean 


#---------------------------------------------------------------------------------
#Combining multiple statement with and or or
weather = "snowing" 

if weather == "snowing":
   print("snowing")
elif weather == "raining":   
   print("raining")
else:
  print("Else case")

#result will be snowing because weather = snowing
#now lets change weather to sunny
weather = "sunny"
if weather == "snowing":
  print("snowing")
elif weather == "raining":
  print("raining")
else:
  print("Else case")
#now the result will be Else case because weather is not = snowing amd the if statement is not true
#---------------------------------------------------------------------------------
#Putting this code into a function so we do not need to repeat the code over and over again

def whatIsTheWeather(weather):

   if weather == "sunny":
    print("sunny")
   elif weather == "raining":
     print("raining")
   else:
     print("Else case")
whatIsTheWeather("sunny")
#---------------------------------------------------------------------------------
#Lets enchance this code by adding input function





   
   



    



  
  
