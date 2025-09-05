#String manipulation and string formatting

#String Formatting
print("Hello, Vincent")
print("Hello david")
#Hello {0} replace {0} with Vincent
print("Hello, {}".format("Vincent"))
#{} are placeholders .format () value to replace the placeholder 
print("Hello {0}, {1}, {2}".format("Vincent", 100, 100.1))
print("Names: {0}, {1}".format("Vincent", "Davide"))

#Real life example: Instagram 

# Followers_____|Following____|Likes_____
#Replacing placeholders with values
print("Followers: {0}| Following: {1}| Likes: {2}".format(10000, 1, "1M"))

#We can add variables with values 
followers = 10000
following = 1 
likes = "1M"
#we can replace the placholders number with the variables 
print("Followers: {0}| Following: {1}| Likes: {2}".format(followers, following, likes))
followers *= 10
print("Followers: {0}| Following: {1}| Likes: {2}".format(followers, following, likes))

#String Manipulation
myName = "Vincent"
myName = "David"
#You can use + to add characters to a string
myName = myName + " " + "Vincent"
print(myName)
myName += " Kevin"
print(myName)

myName = "Tas"
myName += " Duh" 
print(myName)

#Multiply

x = "x"
print(x)
#multiply
print(x*10)



